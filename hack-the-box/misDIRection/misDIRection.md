# Level Easy

After unzipping the archive I got a hierachy of folders labeled with character from the set {0..9a..zA..Z}.
Some folders were containing files named using numbers(e.g. u/20).
I listed the files using: 

```sh
ls ./*/*
```

Then I eliminated unnecessary information from output and got a mapping { <folder_name>: <filename> }. After parsing this I obtained
a string of 36 characters which was a base64 encoding that represented the flag without the final bracket `}`:

```sh
HTB{DIRxxxxxxxxxxxxxxxxxxx}
```

