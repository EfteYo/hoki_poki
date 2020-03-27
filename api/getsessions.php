<?php


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