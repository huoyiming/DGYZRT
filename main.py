import random
import json
import time
import os
import platform


print('幸运大抽奖v2.0.1')
list=[]#初始化抽奖列表
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

#尝试读取n2n.json（名单字典）
try:
	file=open("n2n.json",'r',encoding='utf8')
	n2n = json.load(file)
	save_log('名单加载成功')
except:
	print('跳过读取名单')
	save_log('名单加载失败')

num=input('中奖人数:')#设置中奖人数
save_log('中奖人数设置为'+num)
print('现可使用del [学号]删除参与者')
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
		save_log('抽奖名单设置完毕，参与学号:'+"、".join(list))
		break
	#del命令
	elif a.startswith('del') == True:
		a=a.replace('del ','')
		if (a in list) == True:#判断要删除的参与者是否在名单内
			list.remove(a)
			print('已删除'+a+n2n[a])
			save_log('已删除'+a+n2n[a])
		else:
			print('删除失败: 没有这个参与者')
	#添加抽奖名单
	else:
		a=a.replace(' ','')#删除所有空格，减少出错概率
		#开启严格模式时
		if strict_mode == 'on':
			result=a in list
			if result == True:
				print('此人已存在')
			elif result == False:
				list.append(a)
				try:#尝试在字典中查找学号
					print('已添加:'+a+n2n[a])
					save_log('抽奖名单添加'+a+n2n[a])
				except:
					print('已添加:'+a)
					save_log('抽奖名单添加'+a)
		#关闭严格模式时
		else:
			list.append(a)
			try:
				print('已添加:'+a+n2n[a])
				save_log('抽奖名单添加'+a+n2n[a])
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
	lucky=random.choice(list)
	list.remove(lucky)
	try:
		print(lucky+n2n[lucky])
		save_log('参与者'+lucky+n2n[lucky]+'中奖')
	except:
		print(lucky)
		save_log('参与者'+lucky+'中奖')
save_log('本次抽奖结束')
exit=input('按回车退出')