This is a reverse engineered API wrapper for [Minecraft-Monitroing.ru](https://monitoringminecraft.ru), which allow you automate the process.

## Features:
------------
- Log in with token (authautologin cookie)
- Add new server
- Remove exist server
- Edit exist server
- Display server list
- Support markdown
- Helpful params

## Documentation:
-----------------
Examples can be found in the /examples directory. To run these examples, replce `auth_token` in your token.

```python
client = Client('your_auth_token_here')
```

### Finding Your Token:
Log into [Minecraft-Monitroing.ru](https://monitoringminecraft.ru) on any browser, then open your browser's developer tools (also known as "inspect") and look for the value of the `authautologin` cookie in the following menus:
- Chromium: Devtools > Application > Cookies > monitoringminecraft.ru
- Firefox: Devtools > Storage > Cookies
- Safari: Devtools > Storage > Cookies

### Using the Client:
To use this library, simply import mmonitoring and create a mmonitoring.Client instance. The Client class accepts the following arguments:
```
authautologin - The token to use.

user_agent - The user agent.
```

Regular Example:
```python 
from mmonitoring import Client

client = Client('auth_token')
```

<!-- ## Copyright:
------------- -->