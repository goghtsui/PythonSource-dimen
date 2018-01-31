#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

LANGUAGE = 0

dialog_title = "选取文件"

dialog_init_path = "C:/"

dialog_file_type = "Xml Files (*.xml);;All Files (*)"

root_path = os.path.dirname(os.getcwd())

INSTRUCTIONS = '\n 1. 通过【选项】或者手动填写 [scale] [scale density] [xdpi] 设置被适配机型的参数' \
               '\n 2. 选择默认的 dimens.xml 文件' \
               '\n 3. 选择【开始】' \
               '\n\n' \
               '\ndensity、scale density、xdpi 通过API获取为准，参考如下：' \
               '\n|  等级   | 分辨率（px）| 屏幕密度（dpi）| 换算（px/dp）| 比例 |' \
               '\n|  ldpi    |   240x320    |         120         |   1dp=0.75px  |   3   |' \
               '\n|  mdpi  |   320x480    |         160         |   1dp=1px      |   4   |' \
               '\n|  hdpi   |   480x800    |         240         |   1dp=1.5px    |   6   |' \
               '\n|  xhdpi  |   720x1280  |         320         |   1dp=2px      |   8   |' \
               '\n|  xxhdpi |  1080x1920 |         480         |   1dp=3px      |  12  |' \


AUTHOR = '作者：xiaofeng' \
         '\n邮箱：xiaofeng355@sina.com'

AUTHOR_ALL = '作者：xiaofeng' \
         '\n邮箱：xiaofeng355@sina.com' \
         '\n主页：http://xiaofeng.site'

ICON_ANDROID = 'img/android.png'

ICON_BOOK = 'img/book.png'

ICON_BOY = 'img/boy.png'

ICON_PENCIL = 'img/pencil.png'

ICON_SAVE = 'img/save.png'

ICON_LANG = 'img/recycling.png'
