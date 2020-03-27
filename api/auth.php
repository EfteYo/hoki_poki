<?php

/*
*   Simplymanage Copyright 2020 All Rights Reserved
*
*   Description
*/

chdir(dirname(__DIR__));

require_once('vendor/autoload.php');
require_once('config.php');
require('dbh.inc.php');

use Firebase\JWT\JWT;


header('Content-Type: application/json');

if (!empty(file_get_contents('php://input')) && $_SERVER['REQUEST_METHOD'] == "POST") {
    $request_body = json_decode(file_get_contents('php://input'), true);
    $company = $request_body['company'];
    $username = $request_body['username'];
    $password = $request_body['password'];
    $tablename = $company.'_users';
} elseif ($_SERVER['REQUEST_METHOD'] == "OPTIONS") {
    header('Access-Control-Allow-Origin: http://localhost:4200');
    header("Access-Control-Allow-Headers: Content-Type");
    header("Access-Control-Allow-Methods: POST, OPTIONS");
    exit();
} else {
    header('HTTP/1.0 400 Bad Request');
    exit();
}

if (!empty($username) && !empty($password)) {
    $sql = "SELECT * FROM $tablename WHERE `UID`=?";
    $stmt = mysqli_stmt_init($conn);
    if (mysqli_stmt_prepare($stmt, $sql)) {
        mysqli_stmt_bind_param($stmt, "s", $username);
        mysqli_stmt_execute($stmt);
        $result = mysqli_stmt_get_result($stmt);
        if (!empty($result)) {
            if ($row = mysqli_fetch_assoc($result)) {
                $credentialsAreValid = password_verify($password, $row['PWD']);
            } else {
                echo json_encode(array("error" => "Error - User cannot be found"));
            }
        } else {
            echo json_encode(array("error" => "Error - User cannot be found"));
        }   
    } else {
        echo json_encode(array("error" => mysqli_stmt_error_list($stmt)));
    }
    mysqli_stmt_close($stmt);
    mysqli_close($conn);
} else {
    header('HTTP/1.0 400 Bad Request');
    exit();
}


if ($credentialsAreValid) {

    $tokenId    = base64_encode(openssl_random_pseudo_bytes(32)); 
    $issuedAt   = time();
    $notBefore  = $issuedAt;             ///Adding 10 seconds
    $expire     = $notBefore + 900;            // Adding 15 minutes
    $serverName = $server_name;
    
    /*
     * Create the token as an array
     */
    $data = [
        'iat'  => $issuedAt,         // Issued at: time when the token was generated
        'jti'  => $tokenId,          // Json Token Id: an unique identifier for the token
        'iss'  => $serverName,       // Issuer
        'nbf'  => $notBefore,        // Not before
        'exp'  => $expire,           // Expire
        'data' => [                  // Data related to the signer user
            'userId'   => $row['ID'], // userid from the users table
            'userName' => $username, // User name
        ]
    ];
    
    /*
     * Encode the array to a JWT string.
     * Second parameter is the key to encode the token.
     * 
     * The output string can be validated at http://jwt.io/
     */
    $jwt = JWT::encode(
        $data,      //Data to be encoded in the JWT
        $secret_key,    // The signing key
        'HS512'     // Algorithm used to sign the token, see https://tools.ietf.org/html/draft-ietf-jose-json-web-algorithms-40#section-3
        );
        
    $unencodedArray = [
        'id' => $row['ID'],
        'username' => $username,
        'company' => $company,
        'properties' => json_decode($row['PROPERTIES'], true),
        'status' => $row['STATUS'],
        'token' => $jwt];

    echo json_encode($unencodedArray);
} else {
    header('HTTP/1.0 401 Unauthorized');
}

exit();