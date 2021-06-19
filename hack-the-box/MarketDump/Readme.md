# MarketDump - Medium

Being given the following file `MarketDump.pcapng`, I used `Wireshark` to analyze various streams.
And I found that the attacker fas targeting a sql database. This one contained multiple entries which
matching `American Express,<some_integer>`. Except for one that contained the flag encrypted in
some base which I found on [cyber chef](https://gchq.github.io/CyberChef/).

```sh
HTB{DonTxxxxxxxxxxxxxxxxxxxxxxxx}
```
