# -*- coding: utf-8 -*-

# !!! # Crawl responsibly by identifying yourself (and your website/e-mail) on the user-agent
USER_AGENT = 'TweetScraper'

# settings for spiders
BOT_NAME = 'TweetScraper'
LOG_FILE='log.txt'
LOG_LEVEL = 'WARNING'
DOWNLOAD_HANDLERS = {'s3': None,} # from http://stackoverflow.com/a/31233576/2297751, 

SPIDER_MODULES = ['TweetScraper.spiders']
NEWSPIDER_MODULE = 'TweetScraper.spiders'
ITEM_PIPELINES = {
    'TweetScraper.pipelines.JsonLinesPipeline':1,
    #'TweetScraper.pipelines.SaveToMongoPipeline':100, # replace `SaveToFilePipeline` with this to use MongoDB
    #'TweetScraper.pipelines.SavetoMySQLPipeline':100, # replace `SaveToFilePipeline` with this to use MySQL
}
FEED_FORMAT = 'jsonlines'
FEED_EXPORTERS = {
        'jsonlines': 'scrapy.contrib.exporter.JsonLinesItemExporter',
}
COMMANDS_MODULE = 'TweetScraper.commands'
# 크롤 결과를 저장할 디렉토리 지정
SAVE_TWEET_PATH = './Tweets/UserTweet/user'
SAVE_USER_PATH = './Tweets/UserTweet/user'

# settings for mongodb
# MONGODB_SERVER = "127.0.0.1"
# MONGODB_PORT = 27017
# MONGODB_DB = "TweetScraper"        # database name to save the crawled data
# MONGODB_TWEET_COLLECTION = "tweet" # collection name to save tweets
# MONGODB_USER_COLLECTION = "user"   # collection name to save users


