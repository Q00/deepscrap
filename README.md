# Introduction

`DeepScrap` can get tweets from Hackers who are in Hacker list.
It is built on [Scrapy](http://scrapy.org/) without using [Twitter's APIs](https://dev.twitter.com/rest/public).
The benefits that you can get when you use DeepScrap are you can get rid of the API's rate limits and restrictions. Ideally, you can get all the data from Twitter Search.

# Environment

`DeepScrap` is fully tested in Ubuntu 18.04.2 LTS and macOS 10.14.5.
This prgram use Scrapy 1.7.2.

# Installation

```
    $ git clone https://bigbase.seoultech.ac.kr:8443/r/Project/NSR_2019.git
    $ cd NSR_2019/intermediate/src/DataCollection/DeepScrap
    $ pip3 install -r requirements.txt
    $ cd Deepscrap
	  $ ./start.sh
```

# Usage

1.  Change the `SAVE_USER_PATH` in `Deepscrap/settings.py` to store hacker tweet data.

        SAVE_USER_PATH= 'your path'

2.  Change `number` in `start.sh` file to change number of crawling hacker at once.

        number=20

3.  Change search_list.txt content to Crawl users. It's structure is tuple.
    Also you can put other things(e.g. keyword(search term)) in search_list.txt

### Other module

-   `command module` allow to crawl parallely. You can change  structure and hooking in `crawl_many.py` of command module   
-   `spiders module`, if you want to crawl other information of tweet in HTML document and change a way to crwal informations, change spiders/TweetCrawler.py.
-   `pipelines module`, if you want to change a way to store json, change pipelines.py.
-   `item module`, if you want to change json structure, change itemps.py and add object also you have to put crwaling code in `spiders module`.

# used library

-   [Scrapy](https://scrapy.org/)
