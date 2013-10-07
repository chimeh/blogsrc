#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://hmean.github.io'
RELATIVE_URLS = False 

FEED_RSS = 'feeds/rss.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
DELETE_OUTPUT_DIRECTORY = False # must be False, for i create git repo in output dir

#发布时启动压缩
PLUGIN_PATH = '../pelican-plugins'
PLUGINS = [ 'sitemap',
            'multi_part',
#           'gzip_cache',            
          ]
# Following items are often useful when publishing

DISQUS_SITENAME = "hmean"
GOOGLE_ANALYTICS = "UA-42963057-1"

#统计  cnzz, 以下代码会直接插入每个页面
OTHER_STATISTICS = '''
<script type="text/javascript">var cnzz_protocol = 
(("https:" == document.location.protocol) ? " https://" : " http://");
document.write(unescape("%3Cspan id='cnzz_stat_icon_1000097912'%3E%3C/span%3E%3Cscript src='"
+ cnzz_protocol + "s22.cnzz.com/z_stat.php%3Fid%3D1000097912%26show%3Dpic' type='text/javascript'%3E%3C/script%3E"));</script>
'''
