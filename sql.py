#coding:utf-8

import MySQLdb as mdb
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


con = mdb.connect(host="rdsybz38qh9lu992j3b6.mysql.rds.aliyuncs.com",user="gogo",passwd="ab24562660",db="seo_data",charset='utf8');
# query_file = open('/Users/sunjian/Desktop/ceshi/query_file','w')
query_file = open('/SEO_DATA/ceshi/query_file','w')

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


for k,v in class_dict.items():

	'''判断是读取company表还是job表'''
	if '公司' in k:
		table = 'company'
	else:
		table = 'job'

	with con:
		cur = con.cursor(mdb.cursors.DictCursor)
		cur.execute("select * from %s order by rand() limit 100" % table)
		rows = cur.fetchall()

		print '-----------提取%s的关键词，输出至文件' % k
		for row in rows:
			query = '%s%s,%s' % (row['name'],v,k)
			query_file.write(query + "\n")
			print query