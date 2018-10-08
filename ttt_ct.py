import bluetooth
import time
import sys
import urllib2
import math
from datetime import datetime

def is_ascii(s):
	return all(ord(c)<128 for c in s)

bd_addr = "98:D3:32:20:A9:A4"  # here need to modify. use hciconfig to get address
port = 1

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))
print ('Connected')
#sock.settimeout(1.0)	
temp=''
print ('1. On')
print ('2. Off')
print ('3. wait how much hours?')
print ('4. 23:50 off & 11:00 on')
while 1:	
	tosend = raw_input()
	if tosend == '4':
		while 1:
			nowtime=datetime.now().strftime('%H:%M:%S')
			time.sleep(0.5)
			print(nowtime)
			if nowtime=="11:00:00" :
				sock.send('0')  #On
				data = sock.recv(1)
				print(data)
				time.sleep(0.5)
			elif nowtime=="23:50:00" :
				sock.send('1')  #Off
				data = sock.recv(1)
				print(data)
				time.sleep(0.5)
	elif tosend == '3':
		times= float(raw_input());
		print("wait ")
		print(times)
		print("hours")
		timess=times*60*60
		time.sleep(timess)
		print("turn on")
		sock.send('0')
	elif tosend == '2':
		sock.send('1')
		print('sent 1-off')
	elif tosend == '1':
		sock.send('0')
		print('sent 0-on')
	else:
		print('error')
	#################################
	
	while(1):
		data = sock.recv(1)
		if is_ascii(data):
			
			print(data)
			temp=''	
			break
	
	


