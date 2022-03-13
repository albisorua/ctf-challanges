Running dirb on the server:

```
dirb http://35.198.93.134:30918/
```

We get the following:

```
-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Fri Dec 10 17:33:48 2021
URL_BASE: http://35.198.93.134:30918/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612                                                          

---- Scanning URL: http://35.198.93.134:30918/ ----
+ http://35.198.93.134:30918/flag (CODE:200|SIZE:60)                                                                                                       
+ http://35.198.93.134:30918/index.php (CODE:302|SIZE:0) 
```
The flag was:
```
UNR{26ym3y-aqqqep-idhz4s-boxxwi-o5enrq-tpviyj-sp5wjw-dszds3}
```
