<?php
$data_url = $_POST['imgData'];

list($type, $data) = explode(';', $data_url);
list(, $data) = explode(',', $data);
$data = base64_decode($data);

file_put_contents("../snapshots/sign.png", $data);
?>