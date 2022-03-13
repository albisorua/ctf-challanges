When you access the page you are welcomed by a message that says the following:

```
External Access Denied!
```

Using `dirb` I didn't notice anything. I tried setting some values for cookies
like `loggedon=true`, but didn't work. I started to altering the HTTP headers of
the request. What did the trick was setting the `Host` header to `localhost`:

```
curl -v -H "Host: localhost" "http://<ip>:<port>/"
```

The flag was:

```
ctf{1a140efcxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}
```
