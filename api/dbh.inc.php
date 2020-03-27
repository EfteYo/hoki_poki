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