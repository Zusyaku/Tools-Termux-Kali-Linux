# Admin Panel Finder
[![Python3.x](https://img.shields.io/badge/python-3.x-FADA5E.svg?logo=python)](https://www.python.org/) [![PEP8](https://img.shields.io/badge/code%20style-pep8-red.svg)](https://www.python.org/dev/peps/pep-0008/) 
![](https://img.shields.io/badge/platform-linux%20%7C%20windows%20%7C%20osx-lightgrey.svg)

* A script of easy way to find admin panel of a site written in Python3.
The script actually bruteforce the possible directories and returns the HTTP response code.
You can add your own directories by editing "admin_panels.txt" file.

## Installation & Usage
```
git clone https://github.com/CyberCommands/Admin-finder.git
```
```
cd Admin-finder/
```
```
pip install -r requirements.txt
```
```
python3 finder.py <Target Url>

For example
python3 finder.py http://example.com
```
