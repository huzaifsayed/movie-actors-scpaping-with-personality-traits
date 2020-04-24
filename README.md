Project Scrapes IMDB Website for collecting data of movie actors. After Scraping we apply Personality Prediction to Prediction the Personality of the actors.

I have build this project using Scrapy, Flask and IBM Watson Personality Insights

## How to Run
This app is divided into two parts
1. scraper folder - where all web scraping is done and data is store in database (SQLite3)
2. personality folder - where data is displayed on browser using Flask and Personality Prediction is done using IBM Watson - Personality Insights

#### Install all libraries
`pip install -r requirements.txt`

#### To run Scrapy 
`cd scraper`

`scrapy crawl actors`

#### To run Flask app
`cd personality`

`python flask_app.py`

I recommend you to run this application in virtualenv

Useful Link - https://www.ibm.com/watson/services/personality-insights/

Scraping Link - https://www.imdb.com/list/ls068010962/
