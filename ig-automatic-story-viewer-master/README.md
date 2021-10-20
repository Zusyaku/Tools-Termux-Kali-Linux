IG Automatic Story Viewer
========
<a href="https://www.instagram.com/sinha.py/"><img src="https://cdn.thenewstack.io/media/2017/06/eabeb0f2-f897a954-instagramheartspython.jpg" alt="Auto Story Viewer"/></a>

## Before Running `story_viewer.py`

* Open DMer.py File and Edit The Following Lines:

1) `usrnames = ['psinha_09']  # Account on which You want to send views` [line:07]

2) `usrname = ['USERNAME1', 'USERNAME2', 'USERNAME3', 'USERNAME4', 'USERNAME5']  # Enter your usernames here` [line:14]

3) `password = 'PASSWORD'  # Enter your password here` [line:15]

Ensure that you have Chrome installed and the
[`chromedriver` ](https://chromedriver.chromium.org/downloads) that matches
your Chrome version available on your `$PATH`. You may have to update this from time to time.

## Requirements
 
* [Python](https://www.python.org/)
* `python` on the PATH
* [The Requests Library](http://python-requests.org) for Python: `pip install requests`
* Install Selenium:

```bash
pip install selenium
```

## Run

* Run the program using:

```bash
python story_viewer.py
```
