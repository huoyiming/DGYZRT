import random
import json
import time
import os


print('幸运大抽奖v1.0')
list=[]#初始化抽奖列表
strict_mode='on'#默认开启严格模式


#创建落鸽函数
if not os.path.exists('落鸽'):
    os.makedirs('落鸽')
def save_log(log_text):
	time_date=time.strftime("%Y-%m-%d", time.localtime()) 
	time_hms=time.strftime("%H:%M:%S", time.localtime()) 
	log_name="落鸽/"+time_date+'.log'
	with open(log_name,'a',encoding='utf8') as log_file:
		log_file.write(time_hms+'  '+log_text+'\n')

#尝试读取n2n.json（名单字典），成功则设定error为False，反之亦然
try:
	file=open("n2n.json",'r',encoding='utf8')
	n2n = json.load(file)
	error='False'
	save_log('名单加载成功')
except:
	print('跳过读取名单')
	error='True'
	save_log('名单加载失败')

num=input('中奖人数:')
save_log('中奖人数设置为'+num)
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
	#添加抽奖名单
	else:
		#开启严格模式时
		if strict_mode == 'on':
			result=a in list
			if result == True:
				print('此人已存在')
			elif result == False:
				if error == 'False':
					if (a in n2n) == True:
						list.append(a)
						print('已添加:'+a+n2n[a])
						save_log('抽奖名单添加'+a+n2n[a])
					else:
						print('查无此人')
				elif error == 'True':
					list.append(a)
					print('已添加:'+a)
					save_log('抽奖名单添加'+a)
		#关闭严格模式时
		else:
			#判断输入值是否在字典中存在
			if (a in n2n) == True:
				list.append(a)
				print('已添加:'+a+n2n[a])
				save_log('抽奖名单添加'+a+n2n[a])
			else:
				list.append(a)
				print('已添加:'+a)
				save_log('抽奖名单添加'+a)
			
print('恭喜这'+num+'位同学')
for i in range(int(num)):
	lucky=random.choice(list)
	list.remove(lucky)
	if error == 'False':
		print(lucky+n2n[lucky])
		save_log('参与者'+lucky+n2n[lucky]+'中奖')
	else:
		print(lucky)
		save_log('参与者'+lucky+'中奖')
exit=input('按回车退出')