<?php

error_reporting(0);
(isset($_GET['source']) AND show_source(__FILE__) AND die()); 

if(isset($_REQUEST['p'])){
    echo $_REQUEST['p'];
    $p = preg_replace('/[^\x21-\x7e]/','', $_REQUEST['p']);
    echo $p;
    $p = str_replace("flag", "", $p);
    echo $p;
    $p = substr($p,0,9);
    echo $p;
    
    system("wget -qO - " . $p . " 2>&1");

}

?>
