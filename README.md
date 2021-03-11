# PGA Tour Website Scraper

Created a small web scraper to collect the stats from the pgatour.com website for the 2020 season.  

If you want to modify the scraper for another season, modify pga_scrapy/spiders/pga_stats_v2.py line 25.

## Setup

Install the requirements

> pip install -r "requirements.txt"

run the spider
> scrapy crawl pga_stats_v2

## Process

1) The web crawler extracts the links for each of the 'stats' landing pages.  
   * I excluded the page for "All-Time Records" from the web scraper as that was not relevant for what I was doing.  
2) The spider parses the "stats" landing page to gather all the links for the individual stats
3) The spider crawls through each of those links and yields the name of the stat and the html table
4) The item is passed to a pipeline where the `pandas` `read_html` function is used to parse out the table. 
5) The item is written to a csv file with `to_csv` and named the name of the stat. 

## Be Nice!

Do not ping the pgatour.com that often!
