# Katak
This tool is an open source software login brute-forcer toolkit and hash decrypter.

- Hash Killer 80%
- Hash Detection 75%
- Brute Force 90%
- Big Wordlist 100%
- Support Threading 100%

## Installation and Usage
```sh
$ apt-get update && apt-get upgrade
$ apt-get install git python python-requests python-progressbar
$ git clone https://github.com/Gameye98/Katak
$ cd Katak
$ python katak.py
```

For Android termux environment

```sh
$ apt update && apt upgrade
$ apt install git python2
$ pip2 install requests progressbar
$ git clone https://github.com/Gameye98/Katak
$ cd Katak
$ python2 katak.py
```

### Example usage of Hash Killer
```python
from katak import hash_kill
hash_kill('hash')
```

### Example usage of Brute-Forcer
```python
from katak import brute_force
brute_force( 'url', 'params', 'wordlist', 'match_word', 'method', thread=None, timeout=None)
```

License  
-------  
MIT