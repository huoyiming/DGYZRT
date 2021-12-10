import random
import json
print('幸运大抽奖v1.0')
list=[]#初始化抽奖列表
strict_mode='on'#默认开启严格模式
#尝试读取n2n.json（名单字典），成功则设定error为False，反之亦然
try:
	file=open("n2n.json",'r',encoding='utf8')
	n2n = json.load(file)
	error='False'
except:
	print('跳过读取名单')
	error='True'

num=input('中奖人数:')
while True:
	a=input('学号:')
	#严格模式开启、关闭
	if a.startswith('strict') == True:
		if a.replace('strict ','').startswith('on') == True:
			strict_mode='on'
			print('严格模式已开启')
		elif a.replace('strict ','').startswith('off') == True:
			strict_mode='off'
			print('严格模式已关闭')
		else:
			print('参数错误')
	#当直接回车时退出循环
	elif a == '':
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
					else:
						print('查无此人')
				elif error == 'True':
					list.append(a)
		#关闭严格模式时
		else:
			#判断输入值是否在字典中存在
			if (a in n2n) == True:
				list.append(a)
				print('已添加:'+a+n2n[a])
			else:
				list.append(a)
				print('已添加:'+a)
			
print('恭喜这'+num+'位同学')
for i in range(int(num)):
	lucky=random.choice(list)
	list.remove(lucky)
	if error == 'False':
		print(lucky+n2n[lucky])
	else:
		print(lucky)

exit=input('按回车退出')