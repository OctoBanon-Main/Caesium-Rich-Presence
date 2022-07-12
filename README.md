<div align="center">

# Caesium Rich Presence
</div>
<div align="center">

# A simple rich presence client for Discord
</div>

<div align="center">
    <a href="https://gitlab.com/OctoBanon/Caesium-Rich-Presence/-/issues">Send bug report</a>
    •
    <a href="https://gitlab.com/OctoBanon/Caesium-Rich-Presence#how-use-this">Usage</a>
    •
    <a href="https://gitlab.com/OctoBanon/Caesium-Rich-Presence#something-is-broken-right-now">Broked features</a>
    •
    <a href="https://gitlab.com/OctoBanon/Caesium-Rich-Presence#special-thanks">Special thanks</a>
    •
    <a href="https://gitlab.com/OctoBanon/Caesium-Rich-Presence#licenses">Licenses</a>
</div>


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
```bash
python main.py --help or -h
```
```bash
python main.py create --help or -h
```

## Something is broken right now
Nothing is broken

## How I can help?
Feel free to fork this repo and make a pull request or create an issue, if you encountered a problem!

## Special thanks
[.ZΞRO](https://gitlab.com/kostya-zero) - For helping with code and bug fixing

vnpleo - For helping with text correction in this readme

## Licenses
The project is licensed under the [GNU General Public License 3.0](https://gitlab.com/OctoBanon/Caesium-Rich-Presence/-/blob/main/LICENSE).
