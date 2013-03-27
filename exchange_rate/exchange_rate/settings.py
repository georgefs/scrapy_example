# Scrapy settings for exchange_rate project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'exchange_rate'

SPIDER_MODULES = ['exchange_rate.spiders']
NEWSPIDER_MODULE = 'exchange_rate.spiders'

#DOWNLOAD_DELAY = 5
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'exchange_rate (+http://www.yourdomain.com)'
