# Introduction

`DeepScrap` can get tweets from Hackers who are in Hacker list.
It is built on [Scrapy](http://scrapy.org/) without using [Twitter's APIs](https://dev.twitter.com/rest/public).
The benefits that you can get when you use DeepScrap are you can get rid of the API's rate limits and restrictions. Ideally, you can get all the data from Twitter Search.

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

3.  Change name.txt content to Crawl users. It's structure is tuple.

### Other module

-   `command module` allow to crawl parallely. You can change command structure and hooking.
-   `spiders module`, if you want to crawl other things, change spiders/TweetCrawler.py.
-   `pipelines module`, if you want to change a way to store json, change pipelines.py.
-   `itemp module`, if you want to change json structure, change itemps.py and add object.

# used library

-   [Scrapy](https://scrapy.org/)
