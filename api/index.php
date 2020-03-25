<?php
  $host_name = 'db5000341346.hosting-data.io';
  $database = 'dbs331875';
  $user_name = 'dbu383605';
  $password = 'shalfasfun8Z/N(znaosizd';
  $conn = mysqli_connect($host_name, $user_name, $password, $database);

  if (mysqli_connect_errno()) {
    die('<p>Verbindung zum MySQL Server fehlgeschlagen: '.mysqli_connect_error().'</p>');
  } else {
    mysqli_query($conn,"SET NAMES 'utf8'");
  }


  function insertSession($session, $conn) {
    $sql = "INSERT INTO `sessions`(`ID`, `PROPERTIES`) VALUES (NULL, ?)";
    $stmt = mysqli_stmt_init($conn);
    if (mysqli_stmt_prepare($stmt, $sql)) {
        mysqli_stmt_bind_param($stmt, "s", $session);
        mysqli_stmt_execute($stmt);
        return json_encode(["success" => "Session inserted"]);
    } else { 
        header('HTTP/1.0 500 Internal Server Error');
        header('Content-Type: application/json');
        echo json_encode(["error" => mysqli_stmt_error_list($stmt)]); 
        exit();
    }
  }

  function getSession($id, $conn) {
    $sql = "SELECT * FROM `sessions` WHERE `ID`=?";
    $stmt = mysqli_stmt_init($conn);
    if (mysqli_stmt_prepare($stmt, $sql)) {
        mysqli_stmt_bind_param($stmt, "s", $session);
        mysqli_stmt_execute($stmt);
        $result = mysqli_stmt_get_result($stmt);
        if ($row = mysqli_fetch_assoc($result)) {
            return json_encode($row["PROPERTIES"]);
        } else {
            header('HTTP/1.0 500 Internal Server Error');
            header('Content-Type: application/json');
            echo json_encode(["error" => "Session not found"]);
            exit();
        }
    } else {
        header('HTTP/1.0 500 Internal Server Error');
        header('Content-Type: application/json');
        echo json_encode(["error" => mysqli_stmt_error_list($stmt)]); 
        exit();
    }
  }

  function getSessions($from, $to, $conn) {
    $sql = "SELECT * FROM `sessions`";
    $stmt = mysqli_stmt_init($conn);
    if (mysqli_stmt_prepare($stmt, $sql)) {
        //mysqli_stmt_bind_param($stmt, "s", $session);
        mysqli_stmt_execute($stmt);
        $result = mysqli_stmt_get_result($stmt);
        if ($row = mysqli_fetch_assoc($result)) {
            return json_encode($row["PROPERTIES"]);
        } else {
            header('HTTP/1.0 500 Internal Server Error');
            header('Content-Type: application/json');
            echo json_encode(["error" => "Session not found"]);
            exit();
        }
    } else {
        header('HTTP/1.0 500 Internal Server Error');
        header('Content-Type: application/json');
        echo json_encode(["error" => mysqli_stmt_error_list($stmt)]); 
        exit();
    }
  }
  if (!empty(file_get_contents('php://input'))) {
    $request_body = json_decode(file_get_contents('php://input'), true);
    if ($request_body["operation"] == "insertSession") {
        header('Content-Type: application/json');
        echo insertSession($request_body["session"], $conn);
    }
    else if ($request_body["operation"] == "getSession") {
        header('Content-Type: application/json');
        echo getSession($request_body["id"], $conn);
    }
    else if ($request_body["operation"] == "getSessions") {
        header('Content-Type: application/json');
        echo getSessions($request_body["from"], $request_body["to"], $conn);
    }
} else {
    header('HTTP/1.0 400 Bad Request');
    echo "No Request Body";
    exit();
}

?>