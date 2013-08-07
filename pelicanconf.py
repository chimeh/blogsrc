#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from time import gmtime, strftime
#this satting according to the document in
#https://github.com/getpelican/pelican/blob/master/docs/settings.rs
import os
import sys
sys.path.append(os.curdir)
from notices import *

AUTHOR = u"jim"
SITENAME = u"hmean\'s blog, note life"

SITE_DESCRIPTION = 'hmean\'s blog 博客 记录 技术 生活 linux 嵌入式 半导体 互联网'


TIMEZONE = 'Asia/Shanghai'
COPYRIGHT_FROM = 1998
COPYRIGHT_UNTIL = 2013
DEFAULT_LANG = 'zh'
SITEURL = ''
RELATIVE_URLS = False
#base setting
DEFAULT_DATE_FORMAT =('%Y-%m-%d/%a')
#DEFAULT_DATE_FORMAT =strftime('%Y-%m-%d/%a')
#DEFAULT_DATE_FORMAT =' %Y-%B-%d-%a' #sun Jul 29 2013strftime('%Y-%B-%d/%a')
#FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'

    
LOCALE = ('zh_CN', 'zh_CN.UTF-8',  # On Windows
    'zh_CN', 'zh_CN.UTF-8'     # On Unix/Linux
    )
###########################feed setting########################################
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
#########################Translations and Orderfing content####################
#TRANSLATION_FEED_ATOM = 'feeds/all-en.atom.xml'
TRANSLATION_FEED_RSS = None
#NEWEST_FIRST_ARCHIVES = True
REVERSE_CATEGORY_ORDER = False
###############################################################################
MD_EXTENSIONS = ['codehilite' , 'extra' , 'toc' , 'fenced_code' , 'footnotes']
MARKUP = ( 'md' ,'markdown', 'rst', 'html', ) #byjim 必须为小括号，不能为中括号


#template pages
TEMPLATE_PAGES = None
DIRECT_TEMPLATES = ('index', 'archives','tags','categories') #与下面的如TAGS_URL TAGS_SAVE_AS很大关系
#PAGINATED_DIRECT_TEMPLATES = ('index',)
EXTRA_TEMPLATES_PATHS =[]
#TEMPLATE_PAGES = {'../pelican-themes/0tingtx/welcome.html': 'welcome/welcome.html'}
#                 'src/resume.html': 'dest/resume.html',
#                  'src/contact.html': 'dest/contact.html'}

#############################################################################
DISPLAY_PAGES_ON_MENU = True  #think its redundancy, 合并到MENUITEMS，在0tingtx没有实现
MENUITEMS = (('Welcome'), ('Aboutme'),) #菜单过滤器，这些页面一般放在pages下且同名,URL SAVE_AS由pages里显式指定,否则有page url规则

#<DIRECT_TEMPLATE_NAME>_SAVE_AS =  注意这一行 
# WELCOME_SAVE_AS = 'index.html'
# WELCOME_URL = '/'
INDEX_URL = 'allarticles' 
INDEX_SAVE_AS = 'allarticles/index.html'
CATEGORIES_URL = 'categories/'
CATEGORIES_SAVE_AS = 'categories/index.html'
CATEGORY_URL = 'categories/{slug}/'
CATEGORY_SAVE_AS = 'categories/{slug}/index.html'

USE_FOLDER_AS_CATEGORY=False
TAGS_URL = 'tags/'
TAGS_SAVE_AS = 'tags/index.html'
TAG_URL = 'tags/{slug}/'           #这里到底是tags的url还是各个子tag的，测试是子tag的
TAG_SAVE_AS = 'tags/{slug}/index.html' #tags下各个tag

ARCHIVES_URL = 'archives/' 
ARCHIVES_SAVE_AS = 'archives/index.html' 
YEAR_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/index.html' 
MONTH_ARCHIVE_SAVE_AS = False
DAY_ARCHIVE_SAVE_AS = False
#url setting
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}-{date:%d}/{slug}-{lang}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}-{date:%d}/{slug}-{lang}/index.html'
ARTICLE_LANG_URL = 'posts/{date:%Y}/{date:%m}-{date:%d}/{slug}-{lang}/'
ARTICLE_LANG_SAVE_AS = 'posts/{date:%Y}/{date:%m}-{date:%d}/{slug}-{lang}/index.html'
PAGE_URL = 'pages/{title}-{lang}/'
PAGE_SAVE_AS = 'pages/{title}-{lang}/index.html'
PAGE_LANG_URL = 'pages/{title}-{lang}/'
PAGE_LANG_SAVE_AS = 'pages/{title}-{lang}/index.html'
AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'



#input setting
IGNORE_FILES = ['#_*.*']
PATH = 'content'
OUTPUT_PATH = "output/"
DELETE_OUTPUT_DIRECTORY = False # must be False, for i create a git repo in output dir
PAGE_DIR = ('pages/')
PAGE_EXCLUDES = ()
ARTICLE_DIR = ('posts/')
ARTICLE_EXCLUDES= ('pages',)
# this pelican version rm this value in favor of STATIX_PATHS and EXTRA_PATH_METADATA
FILES_TO_COPY = (('CNAME', 'CNAME'),('baidu_verify_SWIfxtHzAF.html','baidu_verify_SWIfxtHzAF.html'))
STATIC_PATHS = ['images' , 'slides', 'pdf', ] #"archives", 
# Take advantage of the following defaults
# STATIC_SAVE_AS = '{path}'
# STATIC_URL = '{path}'
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    }
#PATH_METADATA =  ' '



#############################THEME#############################################
DEFAULT_PAGINATION = 4
SUMMARY_MAX_LENGTH = 150
THEME_STATIC_PATHS = ['static']
#目前测过的只有ruxlite_tbs支持图片太大自适应
THEME = '../pelican-themes/0tingtx' #Just-Read 0tingtx html5-dopetrope gum bootstrap tuxlite_tbs


SOCIAL = (('zhihu', 'http://www.zhihu.com/people/basemeaning'),
          ('weibo', 'http://weibo.com/'),
          ('github', 'http://github.com/hmean'),
          ('flickr', 'http://www.flickr.com/'),)

#########################Plugins###############################################
PLUGIN_PATH = '../pelican-plugins'
PLUGINS = [ 'sitemap',
            'multi_part',
          ]
#            'better_figures_and_images'
#           'gzip_cache',            
#RESPONSIVE_IMAGES = True
DISQUS_SITENAME = '' #reconfig at publish.py 

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.6,
        'pages': 0.9
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'daily'
    }
}