#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from time import gmtime, strftime
#this satting according to the document in
#https://github.com/getpelican/pelican/blob/master/docs/settings.rs

AUTHOR = u"jim"
SITENAME = u"jim\'s blog, note life"

SITE_DESCRIPTION = '个人网站'
#DEFAULT_DATE="2013-09-28"


TIMEZONE = 'Asia/Shanghai'
COPYRIGHT_FROM = 1998
COPYRIGHT_UNTIL = 2013
DEFAULT_LANG = 'zh_CN.UTF-8'
SITEURL = ''
RELATIVE_URLS = False
#base setting
DEFAULT_DATE_FORMAT ='%a %B %d %Y' #sun Jul 29 2013
#FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'

    
LOCALE = ('usa', 'cn',  # On Windows
    'en_US', 'zh_cn'     # On Unix/Linux
    )
###########################feed setting########################################
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
#########################Translations and Orderfing content####################
DEFAULT_LANG = 'en'
#TRANSLATION_FEED_ATOM = 'feeds/all-en.atom.xml'
TRANSLATION_FEED_RSS = None
#NEWEST_FIRST_ARCHIVES = True
REVERSE_CATEGORY_ORDER = False
###############################################################################
MD_EXTENSIONS = ['codehilite' , 'extra' , 'toc' , 'fenced_code' , 'footnotes']
MARKUP = ( 'md' , 'rst' ) #byjim 必须为小括号，不能为中括号


#template pages
TEMPLATE_PAGES = None
DIRECT_TEMPLATES = ('index','archives','tags','categories') #与下面的如TAGS_URL TAGS_SAVE_AS很大关系
PAGINATED_DIRECT_TEMPLATES = ('index',)
EXTRA_TEMPLATES_PATHS =[]
#TEMPLATE_PAGES = {'/e/workspace/workspace_v5_1/pelican-blog/pelican-themes/0tingtx/templates/archives.html': 'archives.html'}
#                 'src/resume.html': 'dest/resume.html',
#                  'src/contact.html': 'dest/contact.html'}

#############################################################################
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
#FILES_TO_COPY = (('CNAME', 'CNAME'),)
STATIC_PATHS = ["images" , "slides"] #"archives", 
#EXTRA_PATH_METADATA = 
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2}).*'
#PATH_METADATA =  ' '

#url setting
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}-{date:%d}/{slug}-{lang}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}-{date:%d}/{slug}-{lang}/index.html'
ARTICLE_LANG_URL = 'posts/{date:%Y}/{date:%m}-{date:%d}/{slug}-{lang}/'
ARTICLE_LANG_SAVE_AS = 'posts/{date:%Y}/{date:%m}-{date:%d}/{slug}-{lang}/index.html'
PAGE_URL = 'pages/{slug}-{lang}/'
PAGE_SAVE_AS = 'pages/{slug}-{lang}/index.html'
PAGE_LANG_URL = 'pages/{slug}-{lang}/'
PAGE_LANG_SAVE_AS = 'pages/{slug}-{lang}/index.html'
AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'

#<DIRECT_TEMPLATE_NAME>_SAVE_AS =  注意这一行 
CATEGORIES_URL = 'categories/'
CATEGORIES_SAVE_AS = 'categories/index.html'
CATEGORY_URL = 'categories/{slug}/'
CATEGORY_SAVE_AS = 'categories/{slug}/index.html'

TAGS_URL = 'tags/'
TAGS_SAVE_AS = 'tags/index.html'
TAG_URL = 'tags/{slug}/'           #这里到底是tags的url还是各个子tag的，测试是子tag的
TAG_SAVE_AS = 'tags/{slug}/index.html' #tags下各个tag

ARCHIVES_URL = 'archives/' 
ARCHIVES_SAVE_AS = 'archives/index.html' 
YEAR_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/index.html' 
MONTH_ARCHIVE_SAVE_AS = False
DAY_ARCHIVE_SAVE_AS = False

#############################THEME#############################################
MENUITEMS = (('Home', '/'),('life', '/author/jim'))
DISPLAY_PAGES_ON_MENU = True
DEFAULT_PAGINATION = 4
SUMMARY_MAX_LENGTH = 50
THEME_STATIC_PATHS = ['static']
#目前测过的只有ruxlite_tbs支持图片太大自适应
THEME = '../pelican-themes/0tingtx' #Just-Read 0tingtx html5-dopetrope gum bootstrap tuxlite_tbs
LINKS = (('Biologeek', 'http://biologeek.org'),
         ('Filyb', "http://filyb.info/"),
         ('Libert-fr', "http://www.libert-fr.com"),
         ('N1k0', "http://prendreuncafe.com/blog/"),
         ('Tarek Ziadé', "http://ziade.org/blog"),
         ('Zubin Mithra', "http://zubin71.wordpress.com/"),)

SOCIAL = (('zhihu', 'http://www.zhihu.com/people/basemeaning'),
          ('weibo', 'http://weibo.com/'),
          ('github', 'http://github.com/hmean'),
          ('flickr', 'http://www.flickr.com/'),)

#########################Plugins###############################################
PLUGIN_PATH = '../pelican-plugins'
PLUGINS = [ 'sitemap',
            'multi_part',
#            'better_figures_and_images'
          ]
#           'gzip_cache',            'disqus_static'
#RESPONSIVE_IMAGES = True
          

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