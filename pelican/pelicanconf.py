#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Leonardo Giordani'
SITENAME = u'The Digital Cat'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'atom.xml'
TAG_FEED_ATOM = 'categories/%s/atom.xml'
CATEGORY_FEED_ATOM = 'category/%s/atom.xml'
# FEED_ALL_ATOM = None
# TAG_FEED_ATOM = None
# CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
DISPLAY_FEEDS_ON_SIDEBAR = True
DISPLAY_TAGS_ON_SIDEBAR = False


JINJA_EXTENSIONS = ['jinja2.ext.with_', 'jinja2.ext.do']

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'

CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = CATEGORY_URL + 'index.html'

TAG_URL = 'categories/{slug}/'
TAG_SAVE_AS = TAG_URL + 'index.html'

ARCHIVES_URL = 'archives/'
ARCHIVES_SAVE_AS = ARCHIVES_URL + 'index.html'

PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ['related_posts', 'series', 'sitemap', 'tag_cloud']

GOOGLE_ANALYTICS_UNIVERSAL = 'UA-38715090-1'

SITEMAP = {
    'format': 'xml',
}

SLUG_SUBSTITUTIONS = [("c++","cpp")]

DEFAULT_DATE_FORMAT = '%d/%m/%Y'

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),)

# Social widget
SOCIAL = (
        ('Twitter', 'https://twitter.com/tw_lgiordani'),
        ('Google+', 'http://plus.google.com/+LeonardoGiordani?rel=author'),
        ('GitHub', 'https://github.com/lgiordani'),
    )

DEFAULT_PAGINATION = 10
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
    )

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
STATIC_PATHS = ['images', 'code', 'notebooks', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
TWITTER_USERNAME = 'tw_lgiordani'

THEME = "laces3"

LACES_CONTENT_BOOTSWATCH_THEME = 'spacelab'

LACES_PYGMENTS_STYLE = 'monokai'

# LACES_NAVBAR_BRAND = {
#     'show_site_name': True,
#     'file':'images/TheDigitalCat_favicon_32.png',
#     'width':24
# }

LACES_FAVICON = 'images/TheDigitalCat_favicon_32.png'

LACES_ARTICLE_INFO_LIST = {
    'fields': ['date', 'tags']
}

LACES_ARTICLE_INFO_PAGE = {
    'fields': ['date', 'tags', 'series']
}

LACES_SERIES = {
    'display_on_header': True,
    'display_on_footer': True
}

LACES_BANNER = {
    'file': 'images/TheDigitalCat_favicon_32.png',
    'all_pages': False,
    'subtitle': "Adventures of a curious cat in the land of programming"
}

LACES_NAVBAR_BRAND = {
    'title': SITENAME,
    'icon': 'paw'
}

LACES_SIDEBAR = {
    'fields': ['tags', 'tags_inline', 'series', 'social', 'feeds'],
    'recent': True,
    'recent_num': 4,
}

LACES_LICENSE = {
    'cc_short': 'CC-BY-SA'
}

# LACES_GITHUB = {
#     'user': 'lgiordani',
#     'repo_count': 4,
#     'show_user_link': True
# }

LACES_ADDTHIS = {
    'profile': 'ra-552391e122c8506c'
}

LACES_TWITTER_CARDS = True

LACES_OPEN_GRAPH = {
    'image': 'images/TheDigitalCat_logo_200.jpg'    
}

LACES_COOKIECONSENT = True
