What stand out for this challenges was the last section called `.pot`.
And also the hints that were suggesting find the pot at the end of the
rainbow. There was a function that started at that section. To do that
we put a break on `puts` and start executing. After that we print
the mapped memory areas with `vmmap` and identify our target that was
located in the area mapped from `0x555555601000` to `0x555555602000`.
Printing the code we see that we have to call the address `0x555555601010`:

```
call (void)(0x555555601010)()
```

Since we were given the flag format I tried my luck at this point
and used `find UNR` command in gdb and there was the flag mapped in memory:

```
UNR{doubxxxxxxxxxxxxxxxxxxx}
```
