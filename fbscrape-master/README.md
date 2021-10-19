# FBScraper

This is a simple tools to scrape facebook fanspage post information and save the data to existing database without any APIKEY.

<p><img src="https://i.ibb.co/hD7xjs3/Screen-Shot-2021-09-23-at-13-26-10.png"/></p>

## Installation

1. git clone https://github.com/yusriltakeuchi/fbscrape.git
2. Install requirements library
```
pip3 install -r requirements.txt
```
3. Create database with name '**fbscrape**' and setup your database credentials in file **config/database.json**:
```json
{
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "fbscrape"
}
```
4. Write your fanspage target to scrape in file **config/targets.json**:
```json
{
  "targets": [
    {
      "username": "Jokowi",
      "count": 10
    },
    {
      "username": "gojekindonesia",
      "count": 10
    }
  ]
}
```
**count** define how much data you want to collect from the fanspage

5. Run the python script using
```
python3 fbscrape.py
```