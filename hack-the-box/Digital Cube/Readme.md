# Digital Cube - Medium

So the archive contained `.txt` file that had a string formed from `0s` and `1s`. First I tried to convert it to hexa and then to a binary file
using the following [link](https://tomeko.net/online_tools/hex_to_file.php?lang=en). Since it was yelling that the hexa string looks weird I had
another look on the challenge description which was stating `TIME ELAPSED: 50:50`. At a closer look that string had a length of `2500=50x50`, so
the next step was to split it on 50 lines and than I was able to see that it was describing a QR code. I used [this](https://www.dcode.fr/binary-image) to convert the pattern to
a black and white image and [this link](https://zxing.org/w/decode) to read it afterwards.
