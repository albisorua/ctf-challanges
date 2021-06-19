# Debugging Interface - Very Easy

The downloaded archive contained a file with extension `.sal`. First I tried `binwalk` on it and I found 2 files: `digital-0.bin` and `meta.json`.
I used the following command on `digital-0.bin` to see if I can find any clues related to the task:

```sh
strings digital-0.bin
```

The output in general consisted in the following characters: `L`, `A` and `Y`. At the beginning of file was a tag `<SALEAE>`. After googling it I found
a software that was able to load the `.sal` file, which was an analyzer for logic signals. After trying different analyzer I found the flag using the
one called Midi.

```sh
HTB{d38u991n9xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}
```
