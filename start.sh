#!/bin/bash
# ====================================================
#   Copyright (C)2020 All rights reserved.
#
#   Author        : shaohu
#   Email         : shaohu@pinduoduo.com
#   File Name     : start.sh
#   Last Modified : 2022/9/1 16:46
#   Describe      :
#
# ====================================================
set -x
set -e

pt='2020-12-01'
pt=`date -d "-1 days" +%F`


scrapy crawl useragent