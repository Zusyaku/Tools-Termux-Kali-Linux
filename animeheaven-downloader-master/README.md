**Anime Heaven Downloader**  
**NOTICE!**
- [Site](http://animeheaven.eu) will go down by 25th Dec. 😞 so this may no longer works after that period.
- But I will switch to another anime site in the future to prolong the life of this script.

![closure](https://raw.githubusercontent.com/the-robot/animeheaven-downloader/master/Closure.png)

---

> **README:** this is not official, and dev for this script is nothing related with Anime Heaven team. It was written by myself  just to download anime episodes easily. Anime episodes credit go to [Anime Heaven](http://animeheaven.eu/).  

- If you want on-schedule automated downloader with episode sync, go check "[Anime On Schedule Downloader](https://github.com/the-robot/anime-onschedule-downloader)"

**Changes**
- codebase is refactored
- add logger methods, modularized the code so it can be reused in other automated scripts (see [WHY](https://github.com/the-robot/animeheaven-downloader/blob/master/README.md#why-the-heck-did-he-refactor-the-code) at the bottom)
- add animeheaven request blocked handling
- remove the use of progressbar2, and use custom simple progressbar
- way of using the program changed, see [How To Use](https://github.com/the-robot/animeheaven-downloader/blob/master/README.md#how-to-use)

---

### Run with Python3
- Minimum python requirement Python 3.6

**Lib Requirements**  
- [BeautifulSoup](https://pypi.python.org/pypi/beautifulsoup4)
- [Selenium](https://pypi.python.org/pypi/selenium)
- [PhantomJS](http://phantomjs.org/)

**Lib Installation for Ubuntu**
- `sudo pip3 install beautifulsoup4 selenium`
- `npm -g install phantomjs-prebuilt`

---

### How To Use

- go to [Anime Heaven](http://animeheaven.eu/), and simply copy the anime overview page
	- i.e. [http://animeheaven.eu/i.php?a=Bakuman.](http://animeheaven.eu/i.php?a=Bakuman.)
- python app.py --anime={ANIME URL} --episode={1-10}

> --episode: can be either single episode (1) or range (1-10)

> --download: optional parameter to set download path. i.e. --download='/Users/anime/Desktop'

---

### WHY THE HECK DID HE REFACTOR THE CODE

- First of all, the whole purpose of writing this is to save my time from browsing the site and clicking episodes one by one
- After few weeks, people from Anime Heaven added **Abuse Blocking Method** ¯\\_(ツ)_/¯
	
