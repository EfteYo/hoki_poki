<?php
require_once('dbh.inc.php');
//require('getinput.php');

if (!empty(file_get_contents('php://input')) && $_SERVER['REQUEST_METHOD'] == "POST") {
    $request_body = json_decode(file_get_contents('php://input'), true);
} elseif ($_SERVER['REQUEST_METHOD'] == "OPTIONS") {
    header('Access-Control-Allow-Origin: http://localhost:4200');
    header("Access-Control-Allow-Headers: Content-Type");
    header("Access-Control-Allow-Methods: POST, OPTIONS");
    exit();
} elseif (!empty($_POST)) {
    $request_body = json_decode($_POST, true);
} else {
    header('HTTP/1.0 400 Bad Request');
    header('Content-Type: application/json');
    echo json_encode(["error" => "no args", "POST" => json_encode($request_body)]); 
    exit();
}


if (!empty($request_body['session'])) {
    $sql = "INSERT INTO `efte_sessions`(`ID`, `PROPERTIES`) VALUES (NULL, ?)";
    $stmt = mysqli_stmt_init($conn);
    if (mysqli_stmt_prepare($stmt, $sql)) {
        mysqli_stmt_bind_param($stmt, "s", $request_body['session']);
        mysqli_stmt_execute($stmt);
        header('Content-Type: application/json');
        echo json_encode(["success" => "Session inserted"]);
    } else { 
        header('HTTP/1.0 500 Internal Server Error');
        header('Content-Type: application/json');
        echo json_encode(["error" => mysqli_stmt_error_list($stmt)]); 
        exit();
    }
} else {
    header('HTTP/1.0 400 Bad Request');
    echo json_encode(["error" => "session is empty"]); 
    exit();
}
