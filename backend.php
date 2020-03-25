<?php

/*
*   Hoki Poki Copyright 2020 All Rights Reserved
*
*   Backend for Hoki Poki
*/


$servername = 'db5000256604.hosting-data.io';
$dbusername = 'dbu12076';
$dbpassword = '';
$dbname = 'dbs250417';

// connects to the server
$conn = mysqli_connect($servername, $dbusername, $dbpassword, $dbname);

if (!$conn) {
  die("Connection failed: ".mysqli_connect_error());
} else {
  mysqli_query($conn,"SET NAMES 'utf8'");
}