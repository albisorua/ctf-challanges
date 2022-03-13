The idea with combined was to notice in the validator function an interesting
string located at the address of `verify` initially I though that was the flag
in a hex format but it wasn't. Then I looked at the operations realised by
the function itself and I noticed that from 9 in 9 elements were found the
characters of the flag. Partsing that string the flag was:

```
CTF{fe402183xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}
```
