<?php
header('Access-Control-Allow-Origin: *');
$data_url = $_POST['imgData'];

list($type, $data) = explode(';', $data_url);
list(, $data) = explode(',', $data);
$data = base64_decode($data);
$filename = uniqid(rand()) . '.png';

file_put_contents("../snapshots/" . $filename, $data);
echo $filename
?>