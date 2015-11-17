#coding:utf-8

'''
readme

主程序  --->
1、从阿里云RDS中随机抽取关键词（按词类循环）
2、根据当前要查询的关键词类型，将从RDS中抽取的词拼接成对应的Query，并输出至固定文件
3、Scrapy读取固定文件，查询结果写入RDS
4、分析程序（analytics.py）读取RDS中查询结果，输出与JS图标相匹配的字段及数据，写入aoyouhost的mysql中

'''

import MySQLdb as mdb
import sys,os,time
from email.mime.text import MIMEText
import smtplib

reload(sys)
sys.setdefaultencoding('utf-8')

'''爬虫抓取百度PC端搜索结果'''
os.system(" scrapy crawl dmoz ")

'''提取当日抓取的排名数据'''
mysql_time = time.strftime('%Y-%m-%d',time.localtime(time.time()))

class_list = ['公司简介','公司工资','公司待遇','公司面试','公司怎么样','公司招聘','岗位职责','职位就业前景','职位工资','职位面试','职位招聘','职位待遇']

con = mdb.connect(host="rdsybz38qh9lu992j3b6.mysql.rds.aliyuncs.com",user="gogo",passwd="ab24562660",db="seo_data",charset='utf8');
cur = con.cursor(mdb.cursors.DictCursor)

for CLASS in class_list:
	with con:
		
		cur.execute(" select lading,CLASS,query from baidu_pc_rank where `update` = '%s' " % mysql_time )
		rows = cur.fetchall()

		query_file = open('jieguo','w')

		for row in rows:
			line = '%s,%s,%s' % (row['lading'],row['CLASS'],row['query'])
			query_file.write(line + "\n")

'''计算看准及竞品网站排名'''
result_dict = {}
for CLASS in class_list :
	number = int(os.popen(' cat jieguo|grep "%s"|awk -F"," \'!a[$3]++\'|wc -l ' % CLASS).read().strip())

	kanzhun_rank = int( os.popen(' cat jieguo|grep "%s"|grep "kanzhun.com"|awk -F"," \'!a[$3]++\'|wc -l ' % CLASS ).read().strip() )
	jobui_rank = int(os.popen(' cat jieguo|grep "%s"|grep "jobui.com"|awk -F"," \'!a[$3]++\'|wc -l ' % CLASS ).read().strip())			
	wealink_rank = int(os.popen(' cat jieguo|grep "%s"|grep "jobui.com"|awk -F"," \'!a[$3]++\'|wc -l ' % CLASS ).read().strip())

	if kanzhun_rank == 0:
		kanzhun = 0
	else:
		kanzhun = str(format(float(int(kanzhun_rank))/number,'.0%')).replace('%','')

	if jobui_rank == 0:
		jobui = 0
	else:
		jobui = str(format(float(int(jobui_rank))/number,'.0%')).replace('%','')

	if wealink_rank == 0:
		wealink = 0
	else:
		wealink = str(format(float(int(wealink_rank))/number,'.0%')).replace('%','')

	print kanzhun,jobui,wealink

	result_dict['%s' % CLASS] = {'kanzhun':kanzhun,'jobui':jobui,'wealink':wealink} 

'''排名结果写入mysql'''
sql = '''INSERT INTO baidu_pc_sql VALUES ("%s",%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''' % (
	mysql_time,
	result_dict['公司简介']['kanzhun'],
	result_dict['公司简介']['wealink'],
	result_dict['公司简介']['jobui'],
	result_dict['公司工资']['kanzhun'],
	result_dict['公司工资']['wealink'],
	result_dict['公司工资']['jobui'],
	result_dict['公司待遇']['kanzhun'],
	result_dict['公司待遇']['wealink'],
	result_dict['公司待遇']['jobui'],
	result_dict['公司面试']['kanzhun'],
	result_dict['公司面试']['wealink'],
	result_dict['公司面试']['jobui'],
	result_dict['公司怎么样']['kanzhun'],
	result_dict['公司怎么样']['wealink'],
	result_dict['公司怎么样']['jobui'],
	result_dict['公司招聘']['kanzhun'],
	result_dict['公司招聘']['wealink'],
	result_dict['公司招聘']['jobui'],
	result_dict['岗位职责']['kanzhun'],
	result_dict['岗位职责']['wealink'],
	result_dict['岗位职责']['jobui'],
	result_dict['职位就业前景']['kanzhun'],
	result_dict['职位就业前景']['wealink'],
	result_dict['职位就业前景']['jobui'],
	result_dict['职位工资']['kanzhun'],
	result_dict['职位工资']['wealink'],
	result_dict['职位工资']['jobui'],
	result_dict['职位面试']['kanzhun'], 
	result_dict['职位面试']['wealink'],
	result_dict['职位面试']['jobui'], 
	result_dict['职位招聘']['kanzhun'],
	result_dict['职位招聘']['wealink'],
	result_dict['职位招聘']['jobui'],
	result_dict['职位待遇']['kanzhun'],
	result_dict['职位待遇']['wealink'],
	result_dict['职位待遇']['jobui']
	)

print 'Import：%s' % sql
try:
	cur.execute(sql)
	con.commit()
	print 'done'
except:
    con.rollback()

con.close()


'''邮件发送'''
mailto_list=['sunjian@kanzhun.com']
mail_host="smtp.kanzhun.com"  #设置服务器
mail_user="sunjian@kanzhun.com"    #用户名
mail_pass="qwer!asdf"   #口令
mail_postfix="kanzhun.com"  #发件箱的后缀
mail_title = "%s_排名查询进度报告" % resultname     #邮件发送标题

def send_mail(to_list,sub,content):
    #me="hello"+"<"+mail_user+"@"+mail_postfix+">"
    me="sunjian@kanzhun.com"
    msg = MIMEText(content,_subtype='plain',_charset='gb2312')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user,mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False

if __name__ == '__main__':
    if send_mail(mailto_list,mail_title,"查询完毕，请登陆RDS验收"):
        print "发送成功"
    else:
        print "发送失败"
