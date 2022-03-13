The first thing you had to find about dizzy was to see the `robots.txt` file this
was showing you that the only `User-Agent` that is allowed is `unbreakable-ctf/1.0`
using this in combination with dirb:

```
dirb <url> -a <agent>
```

We find that there exists a route called `/pages`. From this point I started working
with `burp` and found a chain of `redirected` pages. You had to identify the beginning
that was `/pages/p.php` and then observer that each page contained a commented string:

```
<!-- ABC -->
```

Taking those from the first page and until the last one you get a string that represented
a `bas64` encoding:

```
Q1RGezNmYzc2MTRmY2Q4MDAwNWQ4MTRjMzJjMTIyMjYyYjc5NGY2NjE1ZTBlMWVlM2Y5ZmRiZDJkOTQ2ZjM5MGY4OGN9
```

After we decode it we get the flag:

```
CTF{3fc7614fxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}
```
