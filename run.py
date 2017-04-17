import requests
from config import *
import time
import os

shipped = 0
while shipped == 0:
	try:
		r = requests.get('https://wwwapps.ups.com/WebTracking/processInputRequest?loc=en_US&Requester=MCDP&tracknum=' + trackNum + '&returnTo=https://wwwapps.ups.com/mcdp?loc=en_US')
		if (r.text.find('Louisville,')>0):
			print('found')
			os.system(foundCommand)
			shipped = 1
		else:
			print('not found')
	except requests.exceptions.RequestException as e:
		print(e)
	time.sleep(60)
