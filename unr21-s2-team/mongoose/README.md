We look at the page's html:

```
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Mongoose</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" type="text/css" href="/static/css/login.css">
</head>

<body>
  <div class="login-page">
    <div class="content-section">
    <div class="head-section">
       <h3>Admin Login</h3>
    </div>
    <div class="body-section">
    <div class="form-input">
      <form class="login-form" id="login">
        <input type="text" placeholder="username" name="username"/>
        <input type="password" placeholder="password" name="password"/>
        <button type="submit" class="btn-submit">login</button>
        <p id="response"></p>
      </form>
      </div>
      </div>
    </div>
  </div>
  <script src="/static/js/login.js"></script>
</body>
</html>
```

We noticed the `login.js` file. In that file we have this:

```
const login    = document.getElementById('login');
const response = document.getElementById('response');

login.addEventListener('submit', e => {
    response.style.display = "none";
	e.preventDefault();
    console.log(new FormData(e.target));
	fetch('/api/login', {
		method: 'POST',
		body: new URLSearchParams(new FormData(e.target))
	})
        .then(resp => resp.json())
        .then(data => {
            if (data.logged) {
                login.remove();
                response.innerHTML = data.message;
                response.style.display = "block";
                window.setTimeout(function() {
                        window.location.href = '/congrats_d130ca6ea8c05c8cf7dcf76dae146f2fcfd62be082e9acb9aa2f0a5934e4eee1';
                    }, 500);
                return;
            } else {
                response.style.display = "block";
                response.innerHTML = data.message;
            }
	});
});
```

The part after `congrats_` was the flag:

```
CTF{d130ca6ea8c05c8cf7dcf76dae146f2fcfd62be082e9acb9aa2f0a5934e4eee1}
```
