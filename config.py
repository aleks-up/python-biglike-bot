"""

СКРИПТ ПИСАЛСЯ НА СКОРУЮ РУКУ, ПОЭТОМУ:
ВЫПОЛНЯЕМ 1 ЗАДАНИЕ НА САЙТЕ  - СМОТРИМ ЗАПРОСЫ - ЗАПОЛНЯЕМ ЭТОТ ФАЙЛ РУКАМИ (1 РАЗ) !!! 

		//	делать сразу как положено - лень п***ц
		
1) логинишься вк
2) логинишься в biglike
3) логинишься в инсте
4) Выполняешь 1 задание ручками - смотришь отправляемые куки 
5) Все, что необходимо поменять - помечено ниже

"""
def vk():
	return ''								#access_token vk
	
def hash():
		return 1490025061557				#нажми "проверить задание" - смотри '_=' в GET запросе 
def bl():
	PHPSESSID = ''							#обнови http://biglike.org/earn - смотри отправляемые куки 
	hash = ''								#обнови http://biglike.org/earn - смотри отправляемые куки 
	fermer = ''								#обнови http://biglike.org/earn - смотри отправляемые куки 
	
	headers = {
	'Host': 'biglike.org',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
	'Accept-Encoding': 'gzip, deflate',
	'Referer': 'http://biglike.org/earn',
	'Cookie': 'PHPSESSID=' + PHPSESSID + '; hash=' + hash + '; fermer=' + fermer,
	'Connection': 'keep-alive',
	'Upgrade-Insecure-Requests': '1',
	'Cache-Control': 'max-age=0'
			}
	return headers 		

def inst(_a):
	headers = {
	'Host': 'www.instagram.com',
	'Accept': '*/*',
	'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
	'Accept-Encoding': 'gzip, deflate, br',
	'X-Instagram-AJAX': '1',
	'Content-Type': 'application/x-www-form-urlencoded',
	'X-Requested-With': 'XMLHttpRequest',
	'X-CSRFToken' : '',						# поставь лайк в инсте - смотри отправляемые куки
	'Cookie': '',							# поставь лайк в инсте - смотри отправляемые куки
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0',
	'Referer': _a
	}
	return headers
