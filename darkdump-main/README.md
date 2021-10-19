# Darkdump - Search The Deep Web Straight From Your Terminal
<p align="center">
  <img src="https://github.com/josh0xA/darkdump/blob/main/imgs/darkdumplogo.png?raw=true">
</p>

## About Darkdump
Darkdump is a simple script written in Python3.9 in which it allows users to enter a search term (query) in the command line and darkdump will pull all the deep web sites relating to that query. Darkdump wraps up the darksearch.io API. 
## Installation
1) ``git clone https://github.com/josh0xA/darkdump``<br/>
2) ``cd darkdump``<br/>
3) ``python3 -m pip install -r requirements.txt``<br/>
4) ``python3 darkdump.py --help``<br/>
## Usage 
Example 1: ``python3 darkdump.py --query programming``<br/>
Example 2: ``python3 darkdump.py --query="chat rooms"``<br/>
Example 3: ``python3 darkdump.py --query hackers --page 2``<br/>
 - Note: The 'page' argument filters through the inputted page number of the results that the darksearch engine returns<br/>
## Menu
```

     ____          _     _
    |    \ ___ ___| |_ _| |_ _ _____ ___
    |  |  | .'|  _| '_| . | | |     | . |
    |____/|__,|_| |_,_|___|___|_|_|_|  _|
                                    |_|

        Developed By: Josh Schiavone
        https://github.com/josh0xA
            joshschiavone.com

usage: darkdump.py [-h] [-v] -q QUERY [-p PAGE]

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         returns darkdump's version
  -q QUERY, --query QUERY
                        the keyword or string you want to search on the deepweb
  -p PAGE, --page PAGE  the page number to filter through the results that the search engine returns (default=1).

```
## Visual
<p align="center">
  <img src="https://github.com/josh0xA/darkdump/blob/main/imgs/darkdump_example_output.png?raw=true">
</p>

## Ethical Notice
The developer of this program, Josh Schiavone, is not resposible for misuse of this data gathering tool. Do not use darkdump to navigate websites that take part in any activity that is identified as illegal under the laws and regulations of your government. May God bless you all. 

## License 
MIT License<br/>
Copyright (c) Josh Schiavone
