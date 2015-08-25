#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://caimaoy.github.io'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = 'caimaoygithubio'
GOOGLE_ANALYTICS = "UA-58273323-2"

AUTHOR = u'caimaoy'
SITENAME = u"caimaoy's blog"
TIMEZONE = 'Asia/Shanghai' # 时区设置

PATH = 'content'

DEFAULT_LANG = u"zh" # 默认语言设置
# DATE_FORMAT={"zh":("zh_CN","%Y-%m-%d,%a"),}#日期格式设置，可按自己喜好设定
# LOCALE = "C"

# path-specific metadata
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/CNAME': {'path': 'CNAME'},
}

# static paths will be copied without parsing their contents
STATIC_PATHS = [
    'extra/robots.txt',
    'extra/CNAME',
]

# Feed generation is usually not desired when developing
'''
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
'''

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
        )

# Social widget
'''
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)
'''
SOCIAL = (
    ('RSS', '/feeds/all.atom.xml'),
    ('github', 'http://github.com/caimaoy'),
    ('weibo', 'http://weibo.com/caimaoy'),)

DEFAULT_PAGINATION = 7

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#
DISQUS_SITENAME = 'caimaoygithubio'

FEED_RSS = u"feeds/all.rss.xml"
CATEGORY_FEED_RSS=u"feeds/%s.rss.xml"#为分类添加Feed

# ARTICLE_URL = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
# ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

USE_FOLDER_AS_CATEGORY = True

# plugin config
# PLUGIN_PATHS = ['./plugins']
PLUGIN_PATHS = [r'./pelican-plugins']
PLUGINS = [
    #'pandoc_reader',
    #'gzip_cache',
    #'update_date',
    #'extract_headings',
    'sitemap',
    #'summary',
    #'niux2_lazyload_helper',
    #'niux2_hermit_player',
    #'minify',
]

# PLUGIN_PATH = u'pelican-plugins'  # 设置插件路径
# PLUGINS = ['sitemap', 'related_posts', 'random_article',               'neighbors']  # 设置启用的插件

# 配置sitemap 插件
SITEMAP = {
     "format": "xml",
     "priorities": {
        "articles": 0.7,
        "indexes": 0.5,
        "pages": 0.3,
        },
     "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly",
        }
     }

# THEME = r'.\pelican-themes\bootstrap2-dark'
# THEME = r'.\pelican-themes\SoMA'
THEME = r'./pelican-themes/pelican-bootstrap3'
