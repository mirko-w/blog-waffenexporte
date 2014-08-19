# -*- coding: utf-8 -*-

# Scrapy settings for waffenexporte project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'waffenexporte'

SPIDER_MODULES = ['waffenexporte.spiders']
NEWSPIDER_MODULE = 'waffenexporte.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'waffenexporte (+http://www.datenprospektor.de)'

AUTOTHROTTLE_ENABLED = True
