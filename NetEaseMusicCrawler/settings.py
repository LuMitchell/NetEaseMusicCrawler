# -*- coding: utf-8 -*-

# Scrapy settings for NetEaseMusicCrawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
import os
import tempfile

BOT_NAME = 'NetEaseMusicCrawler'

SPIDER_MODULES = ['NetEaseMusicCrawler.spiders']
NEWSPIDER_MODULE = 'NetEaseMusicCrawler.spiders'

# 默认的下载器
# DOWNLOAD_HANDLERS_BASE = {
#     'file': 'scrapy.core.downloader.handlers.file.FileDownloadHandler',
#     'http': 'scrapy.core.downloader.handlers.http.HttpDownloadHandler',
#     'https': 'scrapy.core.downloader.handlers.http.HttpDownloadHandler',
#     's3': 'scrapy.core.downloader.handlers.s3.S3DownloadHandler',
# }

# 自定义下载器会覆盖上面的
# DOWNLOAD_HANDLERS = {
#     'http': 'NetEaseMusicCrawler.misc.handler.PhantomJSDownloadHandler',
#     'https': 'NetEaseMusicCrawler.misc.handler.PhantomJSDownloadHandler',
# }
DOWNLOAD_HANDLERS = {
    'http': 'NetEaseMusicCrawler.misc.downloadhandlers.PhantomJSDownloadHandler',
    'https': 'NetEaseMusicCrawler.misc.downloadhandlers.PhantomJSDownloadHandler',
}

# MONGODB
MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
MONGO_DB = 'neteasemusic'
MONGO_COLLECTION = 'profile'

# Phantomjs
PHANTOMJS_OPTIONS = {
    'executable_path': '/usr/local/bin/phantomjs',
    'service_args': [
        '--load-images=false',
        '--disk-cache=true',
        '--local-storage-path=%s' % os.path.join(tempfile.gettempdir(), 'phantomjs')
    ],
}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'NetEaseMusicCrawler.misc.downloadmiddlewares.UserAgentMiddleware': 543
}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'NetEaseMusicCrawler.pipelines.MongodbStorePipeline': 300,
}

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'NetEaseMusicCrawler (+http://www.yourdomain.com)'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'NetEaseMusicCrawler.middlewares.MyCustomSpiderMiddleware': 543,
# }


# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }



# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
