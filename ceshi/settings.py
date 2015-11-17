# -*- coding: utf-8 -*-

# Scrapy settings for ceshi project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

import random

BOT_NAME = 'ceshi'

SPIDER_MODULES = ['ceshi.spiders']
NEWSPIDER_MODULE = 'ceshi.spiders'

USER_AGENTS = [
	"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
	"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
	"Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
	"Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
	"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
	"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
	"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
	"Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
	"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
	"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
	"Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
	"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
	"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]

def getCookie():
    cookie_list = [
    'BAIDUID=791ED7F86F43AF44A3808AB244404E1A:FG=1; PSTM=1443524661; BIDUPSID=4B0DC2F54860625BA83681F98C507951; BDUSS=VdqVXZlaHNPVE1jRzlRU3BEMlBFcFVDQTBGV3ZGcEZTSW90Sn5vZHFQT2pvVFJXQVFBQUFBJCQAAAAAAAAAAAEAAAAJkstJv7TXvMTj1NnM-AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKMUDVajFA1WL; MCITY=-%3A; ispeed_lsm=2; SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a01942858111; H_WISE_SIDS=100043_100288; BDSFRCVID=tAAsJeC627DsPNr4QNLk-qjWNeK2EJ7TH6ao_taMbqNtTyotFjlwEG0PJ3lQpYD-gGLkogKK0mOTHUcP; H_BDCLCKID_SF=JbAjoKK5tKvbfP0kh-QJhnQH-UnLqMrZJT7Z0lOnMp05flToM6OGhP0WQqQaJ-RULIbEXqbLBnRvOKO_e6t5D5J0jN-s-bbfHDJK0b7aHJOoDDvO2j35y4LdLp7xJb5AWKLJbR7wbnj0hpcR3p3s2RIv24vQBMkeWJLfoIP2JCPMbP365ITSMtCfbfO02D62aKDs-lnx-hcqEpO9QT-aLq-gjbQgKPIL-CoObDTe5bOo8Ro6yjOsDUThDHt8J50OfR3fL-08bPoEqbjg54r5hnjH-UIS26uDJJFeo6Q2bnOHDtJpMtJ_Htu32q32DJ3J55ryL4tBan7JDTQm5bOBK-QK5MoO-TPDt5neaJ5n0-nnhn0wDj_M0tuqBnjetlQ4Q5RWhDJR2UJ2en-Ry6C-D5v0jatDq-TtHDjLQ-bqbTrjDnCr34FWKUI8LPbO05Jq5aPe_UjytUTBfMcDW-6vKfu-Ma7OKMcAt2LEoCtXJIL2MDKr5nJbq4uehU6X2D62aKDsLpjp-hcqEIL4jUO50MCXjbQwWPPL-CQU2J5ctq5kMUbSj4QoBn0_Xf5DWJ3nMCOJKJcsbh5nhMJ_DPvGKhFvqfJxWPny523ion6vQpnlHUtu-n5jHjJBjG8J3f; BDRCVFR[ltbVPlNi2ac]=mk3SLVN4HKm; BD_UPN=123253; H_PS_645EC=8871KezGVuec0l6U03EckUIiztA%2Be7LttD91u%2FB6ntENY5ucpQaoGsil%2BFmSqHBO; sug=3; sugstore=1; ORIGIN=0; bdime=21110; BDRCVFR[skC-pcPB0g_]=mk3SLVN4HKm; BD_CK_SAM=1; BDSVRTM=91; H_PS_PSSID=',
        'BAIDUID=0236A7F2BA57EAD085EEDE626343CB91:FG=1; PLUS=1; BIDUPSID=0236A7F2BA57EAD085EEDE626343CB91; PSTM=1444372071; BDRCVFR[skC-pcPB0g_]=mk3SLVN4HKm; BD_CK_SAM=1; BDSVRTM=64; H_PS_PSSID='
    ]
    cookie = random.choice(cookie_list)
    return cookie

# PROXIES = [
#	 {'ip_port': '111.11.228.75:80', 'user_pass': ''},
#	 {'ip_port': '120.198.243.22:80', 'user_pass': ''},
#	 {'ip_port': '111.8.60.9:8123', 'user_pass': ''},
#	 {'ip_port': '101.71.27.120:80', 'user_pass': ''},
#	 {'ip_port': '122.96.59.104:80', 'user_pass': ''},
#	 {'ip_port': '122.224.249.122:8088', 'user_pass': ''},
# ]

'''降低log级别，取消注释则输出抓取详情'''
LOG_LEVEL = 'INFO'

'''禁止cookie'''
COOKIES_ENABLED = False

'''启用cookie debug'''
# COOKIES_DEBUG=True

'''下载中间件设置'''
DOWNLOADER_MIDDLEWARES = {
	# 'ceshi.middlewares.CustomDownloaderMiddleware': 543,
	'ceshi.middlewares.RandomUserAgent': 1,
	# 'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
	# 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
	# 'ceshi.middlewares.ProxyMiddleware': 100,
	'scrapy_crawlera.CrawleraMiddleware': 600 	#crawlera设置
}

'''设置默认request headers'''
DEFAULT_REQUEST_HEADERS = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Host':'www.baidu.com',
    'RA-Sid':'7739A016-20140918-030243-3adabf-48f828',
    'RA-Ver':'3.0.7',
    'Upgrade-Insecure-Requests':'1',
    'Cookie':'%s' % getCookie()
}

# '''下载延时，即下载两个页面的等待时间'''
# DOWNLOAD_DELAY = 0.5

# '''并发最大值'''
# CONCURRENT_REQUESTS = 100

# '''对单个网站并发最大值'''
# CONCURRENT_REQUESTS_PER_DOMAIN = 100

'''启用AutoThrottle扩展，默认为False'''
AUTOTHROTTLE_ENABLED = False

'''设置下载超时'''
DOWNLOAD_TIMEOUT = 10

'''crawlera账号、密码'''
CRAWLERA_ENABLED = True
CRAWLERA_USER = '88aa8b802a7f4626b659dae926ee445b'
CRAWLERA_PASS = 'ab24562660'

MYSQL_HOST = 'rdsybz38qh9lu992j3b6.mysql.rds.aliyuncs.com'
MYSQL_DBNAME = 'seo_data'
MYSQL_USER = 'gogo'
MYSQL_PASSWD = 'ab24562660'

ITEM_PIPELINES = {
    'ceshi.pipelines.CeshiPipeline': 300,
    'ceshi.pipelines.MySQLCeshiPipeline': 400,
}

