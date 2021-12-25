import random
import json
import time
import os
import platform


print('幸运大抽奖v2.1.1')
list1=[]#初始化抽奖列表
strict_mode='on'#默认开启严格模式

#创建落鸽函数
if not os.path.exists('落鸽'):
    os.makedirs('落鸽')#当落鸽文件夹不存在时新建落鸽文件夹
def save_log(落鸽):
	time_date=time.strftime("%Y-%m-%d", time.localtime())#当前时间（年月日）
	time_hms=time.strftime("%H:%M:%S", time.localtime())#当前时间（时分秒）
	log_name="落鸽/"+time_date+'.log'
	with open(log_name,'a',encoding='utf8') as log_file:
		log_file.write(time_hms+'  '+落鸽+'\n')#写入落鸽内容

save_log('==========日志开始==========')
#尝试读取n2n.json（名单字典）
try:
	file=open("n2n.json",'r',encoding='utf8')
	n2n = json.load(file)
	print('名单加载成功')
	save_log('名单加载成功')
except:
	print('跳过读取名单')
	save_log('名单加载失败')

try:
	num=input('中奖人数:')#设置中奖人数
	save_log('中奖人数设置为'+num)
	print('输入del 学号删除参与者\n输入all进行批量抽奖')
	while True:
		a=input('学号:')
		#严格模式开启、关闭
		if a.startswith('strict') == True:
			if a.replace('strict ','').startswith('on') == True:
				strict_mode='on'
				print('严格模式已开启')
				save_log('严格模式被开启')
			elif a.replace('strict ','').startswith('off') == True:
				strict_mode='off'
				print('严格模式已关闭')
				save_log('严格模式被关闭')
			else:
				print('参数错误')
		#当直接回车时退出循环
		elif a == '':
			save_log('抽奖名单设置完毕，参与学号:'+"、".join(list1))
			break
		#del命令
		elif a.startswith('del') == True:
			a=a.replace('del ','')
			if (a in list1) == True:#判断要删除的参与者是否在名单内
				list1.remove(a)
				try:
					print('已删除'+a+'-'+n2n[a])
					save_log('已删除'+a+'-'+n2n[a])
				except:
					print('已删除'+a)
					save_log('已删除'+a)
			else:
				print('删除失败: 没有这个参与者')
		#批量抽奖
		elif a.startswith('all') == True:
			save_log('使用批量抽奖')
			list1=[]#清空列表，防止作弊
			startnum=input('起始值: ')
			endnum=input('结束值: ')
			startnum=startnum.replace(' ','')
			endnum=endnum.replace(' ','')#删除所有空格，减少出错概率
			save_log('起始值设置为'+startnum+'，结束值设置为'+endnum)
			try:
				list1=list(range(int(startnum),int(endnum)+1))
			except:
				print('请输入数字!')
				continue
			list1=[str(x) for x in list1]#将列表中的int全部转化为str
			print('请输入排除值（回车开始抽奖）')
			exceptlist=' '
			while True:
				exceptlist=input('排除值: ')
				save_log('已排除: '+exceptlist)
				if exceptlist == '':
					break
				else:
					list1.remove(exceptlist)
			break
		#添加抽奖名单
		else:
			a=a.replace(' ','')#删除所有空格，减少出错概率
			#开启严格模式时
			if strict_mode == 'on':
				result=a in list1
				if result == True:
					print('此人已存在')
				elif result == False:
					list1.append(a)
					try:#尝试在字典中查找学号
						print('已添加:'+a+'-'+n2n[a])
						save_log('抽奖名单添加'+a+'-'+n2n[a])
					except:
						print('已添加:'+a)
						save_log('抽奖名单添加'+a)
			#关闭严格模式时
			else:
				list1.append(a)
				try:
					print('已添加:'+a+'-'+n2n[a])
					save_log('抽奖名单添加'+a+'-'+n2n[a])
				except:
					print('已添加:'+a)
					save_log('抽奖名单添加'+a)
	#清屏
	if platform.system().lower() == 'windows':
		os.system("cls")
	elif platform.system().lower() == 'linux':
		os.system("clear")
	#输出
	print('恭喜这'+num+'位同学')
	for i in range(int(num)):
		lucky=random.choice(list1)
		list1.remove(lucky)
		try:
			print(lucky+'-'+n2n[lucky])
			save_log('参与者'+lucky+'-'+n2n[lucky]+'中奖')
		except:
			print(lucky)
			save_log('参与者'+lucky+'中奖')
	save_log('本次抽奖结束')
except:
	if platform.system().lower() == 'windows':
		os.system("cls")
	elif platform.system().lower() == 'linux':
		os.system("clear")
	print('程序出现异常')
	save_log('程序炸了嘤嘤嘤')
save_log('==========日志结束==========\n')
exit=input('按回车退出')
