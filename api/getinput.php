
<?php
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
    exit();
}