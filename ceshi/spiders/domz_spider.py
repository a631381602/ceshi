#coding:utf-8

import scrapy,re,urllib,os,time,sys
from ceshi.items import CeshiItem
import MySQLdb as mdb

reload(sys)
sys.setdefaultencoding('utf-8')

current_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))

def search(req,html):
     text = re.search(req,html)
     if text:
         data = text.group(1)
     else:
         data = 'no'
     return data

class_dict = {	
				'公司简介':'',
				'公司工资':'工资',
				'公司待遇':'待遇',
				'公司面试':'面试',
				'公司怎么样':'怎么样',
				'公司招聘':'招聘',
				'岗位职责':'岗位职责',
				'职位就业前景':'就业前景',
				'职位工资':'工资',
				'职位面试':'面试',
				'职位招聘':'招聘',
				'职位待遇':'待遇'

				}

con = mdb.connect(host="rdsybz38qh9lu992j3b6.mysql.rds.aliyuncs.com",user="gogo",passwd="ab24562660",db="seo_data",charset='utf8');
# query_file = open('/Users/sunjian/Desktop/ceshi/query_file','w')
query_file = open('/SEO_DATA/ceshi/query_file','w')

for k,v in class_dict.items():

	'''判断是读取company表还是job表'''
	if '公司' in k:
		table = 'company'
	else:
		table = 'job'

	with con:
		cur = con.cursor(mdb.cursors.DictCursor)
		cur.execute("select * from %s order by rand() limit 1000" % table)
		rows = cur.fetchall()

		print '-----------提取%s的关键词，输出至文件' % k
		for row in rows:
			query = '%s%s,%s' % (row['name'],v,k)
			query_file.write(query + "\n")

query_file.close()

class DmozSpider(scrapy.Spider):
	name = "dmoz"
	allowed_domains = ["www.baidu.com"]

	# start_urls = ['http://www.baidu.com/s?q=&tn=baidulocal&ct=2097152&si=&ie=utf-8&cl=3&wd=%s' % urllib.quote('华为工资') ]

	start_urls = []
	for line in open('/SEO_DATA/ceshi/query_file'):
		line = line.strip()

		try:
			word = line.split(',')[0]
			CLASS = line.split(',')[1]
		except:
			print 'error'

		url = 'http://www.baidu.com/s?q=&tn=baidulocal&ct=2097152&si=&ie=utf-8&cl=3&wd=%s&class=%s' % (urllib.quote(word),urllib.quote(CLASS) )
		start_urls.append(url)

	def __get_url_query(self, url):
		m =  re.search("wd=(.*?)&", url).group(1)
		return m

	def __get_url_class(self, url):
		m =  re.search("class=(.*)", url).group(1)
		return m

	def parse(self,response):
		n = 0

		for sel in response.xpath('//td[@class="f"]'):

			query = urllib.unquote(self.__get_url_query(response.url))
			CLASS = urllib.unquote(self.__get_url_class(response.url))

			item = CeshiItem()

			title = re.sub('<[^>]*?>','',sel.xpath('.//a/font[@size="3"]').extract()[0])
			lading = sel.xpath('.//a[1]/@href').extract()[0]
			time = sel.xpath('.//font[@color="#008000"]/text()').re('(\d{4}-\d{1,2}-\d{1,2})')[0]
			size = sel.xpath('.//font[@color="#008000"]/text()').re('(\d+K)')[0]

			n += 1

			item['rank'] = n
			item['title'] = title.encode('utf8')
			item['lading'] = lading.encode('utf8')
			item['time'] = time.encode('utf8')
			item['size'] = size.encode('utf8')
			item['query'] = query
			item['update'] = current_date
			item['CLASS'] = CLASS
			yield item
