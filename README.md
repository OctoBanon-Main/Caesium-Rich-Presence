<div align="center">

# Caesium Rich Presence
</div>
<div align="center">

# A simple rich presence client for Discord
</div>

<div align="center">
    <a href="https://gitlab.com/OctoBanon/Caesium-Rich-Presence/-/issues">Send bug report</a>
    •
    <a href="https://gitlab.com/OctoBanon/Caesium-Rich-Presence#usage">Usage</a>
    •
    <a href="https://gitlab.com/OctoBanon/Caesium-Rich-Presence#things-to-fix">Things to fix</a>
    •
    <a href="https://gitlab.com/OctoBanon/Caesium-Rich-Presence#special-thanks">Special thanks</a>
    •
    <a href="https://gitlab.com/OctoBanon/Caesium-Rich-Presence#license-information">License Information</a>
</div>

## Warning
This version no longer be supported.


## Prepare Python
- Install pypresence with command:
```bash
pip install pypresence
```

Or on linux
```bash
pip3 install pypresence
```
## Usage
Firstly, you need to create application on [Discord Developer Portal](https://discord.com/developers/applications).
Then, take you application ID. 
It will be used as `client-id` to create profile in Caesium.
- Create profile:
```bash
python main.py create --client-id ID --name "NAME" --details "TEXT" --state "TEXT"
```
- Load created profile:
```bash
python main.py load --name "NAME"
```
- Call help message:
```bash
python main.py -h     
python main.py --help # Alternative
```

## Things to fix
Nothing is broken

## How I can help?
Feel free to fork this repo and make a pull request or create an issue, if you encountered a problem!

## Special thanks
[.ZΞRO](https://gitlab.com/kostya-zero) - For helping with code and bug fixing

[Snaky1](https://github.com/Snaky1) - For PEP8 fixes

vnpleo - For helping with text correction in this readme


## License Information
The project is licensed under the [GNU General Public License 3.0](https://gitlab.com/OctoBanon/Caesium-Rich-Presence/-/blob/main/LICENSE).
