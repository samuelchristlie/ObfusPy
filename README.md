<div align="center">
<div>
  
```
   ___  _      __           ____        
  / _ \| |__  / _|_   _ ___|  _ \ _   _ 
 | | | | '_ \| |_| | | / __| |_) | | | |
 | |_| | |_) |  _| |_| \__ \  __/| |_| |
  \___/|_.__/|_|  \__,_|___/_|    \__, |
                                  |___/ `
```
</div>

# ObfusPy
## Protect your Python codes from prying eyes

![github stars badge](https://badgen.net/github/stars/samuelchristlie/ObfusPy?icon=github)
![github forks badge](https://badgen.net/github/forks/samuelchristlie/ObfusPy?icon=github)
![github issues badge](https://badgen.net/github/open-issues/samuelchristlie/ObfusPy?icon=github)

![github last commit badge](https://badgen.net/github/last-commit/samuelchristlie/ObfusPy?icon=github)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

[github stars link]: https://github.com/invoke-ai/InvokeAI/stargazers
</div>

**ObfusPy** is a blazing fast obfuscator for Python, making it more challenging to read the source code. **ObfusPy** is designed to be reliable and suitable for almost every kind of code. Please note that the obfuscated file can still be decrypted as the key included in the file. For better protection, it is recommended to use tools like [PyArmor](https://github.com/dashingsoft/pyarmor) instead.

## Features 💪
- **High Performance**: ObfusPy is optimized for speed and efficiency, ensuring minimal impact to on your application's performance.
- **Fernet Encryption**: Industry-standard symmetric encryption makes it more challenging to read the source code.
- **Easy Integration**: ObfusPy can obfuscate entire folder in one go which makes it suitable to use on large projects.
- **Open Source**: ObfusPy is fully open source, open for collaboration and contribution from thriving community of developers.

## Table of Contents 📝
1. 💻 [Installation](#installation)
2. ▶ [Usage](#usage)
3. 📃 [License](#license)
4. 🙏 [Acknowledgements](#acknowledgements)

## 💻 Installation
Clone this repository
```
git clone https://github.com/samuelchristlie/ObfusPy
cd ObfusPy
```

## ▶ Usage
To run **ObfusPy** on the current folder (i.e. example.py)
```
python obfus.py
```
You can also use `--help` to see the available options

```
usage: obfus.py [-h] [-i I]

   ____  __    ____           ____
  / __ \/ /_  / __/_  _______/ __ \__  __
 / / / / __ \/ /_/ / / / ___/ /_/ / / / /
/ /_/ / /_/ / __/ /_/ (__  ) ____/ /_/ /
\____/_.___/_/  \__,_/____/_/    \__, /
                                /____/

[Obfuspy] Python script to encrypt other scripts
[https://github.com/samuelchristlie/ObfusPy]

options:
  -h, --help  show this help message and exit
  -i I        Folder to be encrypted.
              If none given, current folder will be used

```
## 📃 License
This project is licensed under the GNU GPL v3 License - see the [LICENSE](LICENSE) file for more details.

## 🙏 Acknowledgements
Thanks to Patrick Gillespie for creating the ASCII text art tool used in this project
https://patorjk.com/software/taag/
