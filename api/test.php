<?php
$request_body = json_decode(file_get_contents('php://input'), true);


header("Content-Type: application/json");
echo json_encode(["success" => "running", "request_body" => json_encode($request_body), "POST" => json_encode($_POST)]);