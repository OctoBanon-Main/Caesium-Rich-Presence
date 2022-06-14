<div align="center">

# Simple DRPС
</div>
<div align="center">

# Simple Discord Rich Presence client
</div>

<p align="center">
    <a href="https://gitlab.com/OctoBanon/discord-rpc/-/issues">Send bug report</a>
    •
    <a href="https://gitlab.com/OctoBanon/discord-rpc#how-use-this">Usage</a>
    •
    <a href="https://gitlab.com/OctoBanon/discord-rpc#something-is-broken-right-now">Broked features</a>
    •
    <a href="https://gitlab.com/OctoBanon/discord-rpc#special-thanks">Special thanks</a>
    •
    <a href="https://gitlab.com/OctoBanon/discord-rpc#licenses">Licenses</a>
</p>


## Warning
Argument parser will be rewrited in next update and old arguments maybe will unavalible or renamed


## How use this?
- Install pypresence with command:
```bash
pip install pypresence
```

Or on linux
```bash
pip3 install pypresence
```

- Create application in [Discord Developer Portal](https://discord.com/developers/applications)

- Take application id from your created app and paste this in client-id argument

- Create profile with command:
```bash
python main.py create --client-id ID --name "NAME" --details "TEXT" --state "TEXT"
```

- And load this with command
```bash
python main.py load --name "NAME"
```

Addictional arguments will be in help
```
python main.py --help or -h
```

```
python main.py create --help or -h
```


## Something is broken right now
Nothing is broken


## How I can help?
Feel free to fork this repo and make a pull request or create an issue, if you encountered a problem!


## Special thanks
[.ZΞRO](https://github.com/kostya-zero) - For helping with code and bug fixing

vnpleo - For helping with text correction in this readme


## Licenses
The project is licensed under the GNU General Public License 3.0.
