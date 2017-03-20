import pprint
import code
import json
import requests
import sys
import random
import re
import vk
from datetime import datetime, date
import time
import config

_t = config.vk()
_h= config.hash()

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)  #переводим спец.символы в читаемые
session = vk.Session()
api = vk.API(session) 

def vklike():
	r = requests.post('http://biglike.org/vklike',headers = config.bl(),data={'': ''}).text.translate(non_bmp_map)
	point = r.split('id="points"',1)[1].split('</font>',1)[0].split('px;">',1)[1]
	r = r.split('proverka(',1)[1].split('"',1)[0]
	task_id =  r.split(', ',1)[0]
	link =  r.split(';',4)[3].split('&',1)[0]

	screen_name = link.split('.com/',1)[1]

	if "wall" in screen_name:type_ob = "post"
	elif "photo" in screen_name:type_ob = "photo"
	elif "video" in screen_name:type_ob = "video"

	owner_id =  str(re.findall('\d+',screen_name.split('_',1)[0])).replace('\'','').replace('[','').replace(']','')

	if "-" in screen_name: owner_id = '-'+str(owner_id)
	item_id =  str(re.findall('\d+',screen_name.split('_',1)[1])).replace('\'','').replace('[','').replace(']','')

	#выполняем задание
	api.likes.add (access_token=_t,type=type_ob,owner_id=owner_id,item_id=item_id)

    #берем заслуженные баллы
	url = 'http://biglike.org/ajax.php?divid='+task_id +'&taskid='+task_id+'&task=vklike&_='+ str(_h+1)
	r = requests.post(url,headers = config.bl(),data={'': ''}).text.translate(non_bmp_map)

	if '<font size="6" >' in r:
		print (datetime.now().strftime("%H:%M:%S")+ '|Монет: '  +point  + ' VK like: ' + type_ob + owner_id +'_' + item_id + ' заработано баллов:' + r.split('<font size="6" >',1)[1].split('<',1)[0])
	else: print('problemes.../' + screen_name)
	time.sleep(random.randint(2, 5))


def vkfollow():
	r = requests.post('http://biglike.org/vkgroup',headers = config.bl(),data={'': ''}).text.translate(non_bmp_map)
	point = r.split('id="points"',1)[1].split('</font>',1)[0].split('px;">',1)[1]
	r = r.split('proverka(',1)[1].split('"',1)[0]
	task_id =  r.split(', ',1)[0]
	link =  r.split(';',4)[3].split('&',1)[0]
	screen_name = link.split('.com/',1)[1]

    #выполняем задание
	group_id = api.utils.resolveScreenName (screen_name=screen_name)['object_id']
	api.groups.join(access_token=_t,group_id=group_id)
	#берем заслуженные баллы
	url = 'http://biglike.org/ajax.php?divid='+task_id +'&taskid='+task_id+'&task=vkgroup&_='+ str(_h+2)

	r = requests.post(url,headers = config.bl(),data={'': ''}).text.translate(non_bmp_map)
	balls = r.split('<font size="6" >',1)[1].split('<',1)[0]
	print (datetime.now().strftime("%H:%M:%S")+ '|Монет: '  +point  + ' VK follow: ' + str(group_id) + ' заработано баллов:' + balls)
	time.sleep(random.randint(3, 7))

def instalike():
	r = requests.post('http://biglike.org/instalike',headers = config.bl(),data={'': ''}).text.translate(non_bmp_map)
	point = r.split('id="points"',1)[1].split('</font>',1)[0].split('px;">',1)[1]
	r = r.split('proverka(',1)[1].split('"',1)[0]
	task_id =  r.split(', ',1)[0]
	inst_link =  r.split(';',4)[3].split('&',1)[0]

	screen_name = inst_link.split('.com/',1)[1].split('?',1)[0]
	get_media_id = 'https://www.instagram.com/' + screen_name + '?__a=1'
	refer = 'https://www.instagram.com/' + screen_name
	_inst = config.inst(refer)
	r = requests.get(get_media_id,headers = _inst,data={'': ''}).json()
	media_id = r['media']['id'] 

	setLike = 'https://www.instagram.com/web/likes/' + media_id + '/like/'
	r = requests.post(setLike,headers = _inst ,data={'': ''}).json()
	time.sleep(random.randint(4, 6))        
	#берем заслуженные баллы
	url = 'http://biglike.org/ajax.php?divid='+task_id +'&taskid='+task_id+'&task=instalike&_='+ str(_h+2)
	r = requests.get(url,headers = config.bl(),data={'': ''}).text.translate(non_bmp_map)

	#исключение
	def waiting():
		time.sleep(random.randint(20, 26))
		r = requests.get(url,headers = config.bl(),data={'': ''}).text.translate(non_bmp_map)
	try:
		balls = r.split('<font size="6" >',1)[1].split('<',1)[0]
		print (datetime.now().strftime("%H:%M:%S")+ '|Монет: '  +point  + ' instagram like: ' + task_id + '_' +media_id + ' заработано баллов:' + balls)
	except IndexError:
		waiting()

def instafollow():
	r = requests.get('http://biglike.org/instasub',headers = config.bl(),data={'': ''}).text.translate(non_bmp_map)
	point = r.split('id="points"',1)[1].split('</font>',1)[0].split('px;">',1)[1]
	r = r.split('proverka(',1)[1].split('"',1)[0]
	task_id =  r.split(', ',1)[0]
	inst_link =  r.split(';',4)[3].split('&',1)[0]
	screen_name = inst_link.split('.com/',1)[1].split('?',1)[0]
	get_user_id = 'https://www.instagram.com/' + screen_name + '?__a=1'
	refer = 'https://www.instagram.com/' + screen_name
	_inst = config.inst(refer)
	r = requests.get(get_user_id,headers = _inst,data={'': ''}).json()
	user_id = r['user']['id'] 

	follow = 'https://www.instagram.com/web/friendships/' + user_id + '/follow/'
	r = requests.post(follow,headers = _inst,data={'': ''}).json()

	time.sleep(random.randint(4, 6))        
	#берем заслуженные баллы
	url = 'http://biglike.org/ajax.php?divid='+task_id +'&taskid='+task_id+'&task=instasub&_='+ str(_h+2)
	r = requests.get(url,headers = config.bl(),data={'': ''})
	r = r.text.translate(non_bmp_map)

	def waiting():
		time.sleep(random.randint(20, 26))
		r = requests.get(url,
		headers = config.bl(),
		data={'': ''})
		r = r.text.translate(non_bmp_map)
	try:
		balls = r.split('<font size="6" >',1)[1].split('<',1)[0]
		print (datetime.now().strftime("%H:%M:%S")+ '|Монет: '  +point  + ' instagram following: ' + task_id + '_' +user_id + ' заработано баллов:' + balls)
	except IndexError:
		waiting()


for i in range(1, 30):		#выполняет за раз по 30 заданий
    vklike()				#ставит лайк вк
    vkfollow()				#подписывается вк
    instafollow()			#подписывается в инсте
    instalike()				#ставит лайк в инсте
    _h = _h + 4*i


input("\n\nНажмите Enter чтобы выйти .")
