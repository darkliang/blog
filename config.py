# -*- coding: utf-8 -*-
"""Sample Configuration
"""

# For Maverick
site_prefix = "/"
source_dir = "./src/"
build_dir = "./dist/"
template = "Galileo"
index_page_size = 10
archives_page_size = 30
fetch_remote_imgs = False
enable_jsdelivr = {
    "enabled": True,
    "repo": "darkliang/darkliang.github.io@gh-pages"
}
locale = "Asia/Shanghai"
category_by_folder = False

# For site
site_name = "Leeeung"
site_logo = "${static_prefix}android-chrome-512x512.png"
site_build_date = "2019-12-06T12:00+08:00"
author = "AlanDecode"
email = "hi@imalan.cn"
author_homepage = "https://www.leeeung.com"
description = "This is Maverick, Theme Galileo."
key_words = ["Maverick", "AlanDecode", "Galileo", "blog"]
language = 'english'
background_img = '${static_prefix}bg/The_Great_Wave_off_Kanagawa.jpg'
external_links = [
    
]
nav = [
    {
        "name": "Home",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "Archives",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "About",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "GitHub",
        "url": "https://github.com/darkliang",
        "icon": "gi gi-github"
    }
]

valine = {
    "enable": True,
    "el": '#vcomments',
    "appId": "IKRAfuPq0zrz6Wfje8ahHAIP-gzGzoHsz",
    "appKey": "lFaCWkd4xCs0Ng5UWs1eHNwU",
    "visitor": True,
    "recordIP": True,
    "placeholder": ""
}

head_addon = ''

footer_addon = ''

body_addon = ''
