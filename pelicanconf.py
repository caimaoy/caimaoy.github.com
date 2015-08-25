#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'caimaoy'
SITENAME = u"caimaoy's blog"
SITEURL = ''
TIMEZONE = 'Asia/Shanghai'#时区设置

PATH = 'content'

# DEFAULT_LANG = u'en'

DEFAULT_LANG = u"zh"#默认语言设置
# DATE_FORMAT={"zh":("zh_CN","%Y-%m-%d,%a"),}#日期格式设置，可按自己喜好设定
# LOCALE = "C"

# Feed generation is usually not desired when developing
'''
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
'''

# path-specific metadata
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/CNAME': {'path': 'CNAME'},
    # 'extra/404.html': {'path': '404.html'},
}

# static paths will be copied without parsing their contents
STATIC_PATHS = [
    'extra/robots.txt',
    'extra/CNAME',
    # '404.html',
    # 'extra'
]


# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

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
DISQUS_SITENAME = u'caimaoygithubio'

GITHUB_URL = u'github.com/caimaoy'

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
