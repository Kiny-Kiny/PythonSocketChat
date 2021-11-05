# Client
import socket
from threading import Thread
from os import system, path
from datetime import datetime
Stop=False
def receive():
	global Stop
	while True:
		if Stop:
			break
		try:
			message =client.recv(1024).decode('ascii')
			if message == 'NICK':
				client.send(nickname.encode('ascii'))
				
				Next=client.recv(1024).decode('ascii')
				if Next=='PASS':
					client.send(password.encode('ascii'))
					if Next =='REFUSE':
						print('[ X ] SENHA INCORRETA!');break
				elif Next == 'BAN':
					print('Você foi banido.');exit();Stop=True
			else: print(message)
		except Exception as e: print(str(e) + '\n[ X ] Erro de conexão');client.close();break
		
def write():
	while True:
		if Stop:
			break
		message='%s > %s'%(nickname,input(''))
		if len(message.split('>')[1])+1 > 250: print('[ ! ] Quantidade muito grande de caracteres.')
		elif len(message.split('>')[1])+1 < 1: print('[ ! ] Quantidade muito pequena de caracteres.')
		else:
			if message[len(nickname)+3:].startswith('/'):
				if nickname in ['Kiny','N3X0']:
					if message[len(nickname)+3:].startswith('/kick'):
						client.send(str('KICK %s'%message[len(nickname)+2+6:]).encode('ascii'))
					elif message[len(nickname)+3:].startswith('/ban'):
						client.send(str('BAN %s'%message[len(nickname)+2+6:]).encode('ascii'))
				else:
					print('[ ! ] Este comando só pode ser executado por um Admin.')
			else:
				time=datetime.now().strftime('%H:%M:%S')
				message=f'[ {time} ] - '+message
				try:
					client.send(message.encode('ascii'))
				except:
					pass
			

system('clear')
global password
print('===========\nBem-Vindo ao KinyChat 0.5\n===========')
if path.exists('login')==True:
	with open('login','r') as f:
		nickname=f.read()
		if nickname in ['Kiny','N3X0']:
			password=str(input('Digite a senha do Admin >>> '))
else:
	nickname=str(input('Digite seu nome >>> '))
	if nickname in ['Kiny','N3X0']:
		password=str(input('Digite a senha do Admin >>> '))
	while int(len(nickname)) < 4:
		nickname=str(input('Seu nome deve conter ou ter mais de quatro dígitos >>> '))
	while int(len(nickname)) >16:
		nickname=str(input('Seu nome deve conter 15 caracteres ou menos >>> '))
		nickname=nickname.replace(' ','_')
	with open('login','w+') as c:
		c.write(nickname)
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
	client.connect(('20.188.109.156',3309))
except:
	print('[ X ] Erro, verifique sua conexão à internet.');exit()
Thread(target=receive).start();Thread(target=write).start()
