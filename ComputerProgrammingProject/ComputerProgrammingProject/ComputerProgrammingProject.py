#Welcome to my computer programming project

import time
import csv


def numType(): 
	global num
	num = input()
	count = len(num)
	if (count != 4):
		print ('Only 4 digits!')
		numType()
	else: 
		settingMain()	
		return(num)

def encryption(num):


	a = num[0]
	b = num[1]
	c = num[2]
	d = num[3]
	

	a = int(a)+7
	b = int(b)+7
	c = int(c)+7
	d = int(d)+7
	
	a = a % 10
	b = b % 10
	c = c % 10
	d = d % 10
	

	a = str(a)
	b = str(b)
	c = str(c)
	d = str(d)
	
	encryptedNumber = c+d+a+b
	
	file = open('encryptedFile.txt', 'w')
	file.write(str(encryptedNumber))
	file.close()

	
	print('Encryption has concluded and has been stored')
	settingMain()

	return()

def settingMain(): 
	print('If you want to encrypt this number press: R. If you want to dycrypt, press D ')
	encryptER = input()
	if (encryptER == 'E'):
		numType()
	elif (encryptER == 'R'): 
		print('Loading Encryption...')
		encryption(num)
		return()
	 
	print ("If you want to decrypt this number press E or D")
	
	if (encryptER == 'D'): 
		print('Loading Decryption...')
		time.sleep(1)
		decryption()
		return()
	

def settingStart(): 
	print("Type W to Encrypt, L to read file, T to delete file")
	encryptER = input()
	if (encryptER == 'W'): 
		print ("Enter a pin with 4 digits")
		numType()
		return()
	elif (encryptER == "T"): 
		deleteFile()
		return()
	elif(encryptER == "Z"): 
		exit()
	else: 
		print('Must be W or L')
		time.sleep(0.5)
		settingStart()
		return()

def deleteFile(): 
	print('Do you want to clear the file? Y or N')
	answer = input()
	if(answer == "Y"):
		print ('Are you positive? Y or N') 
		answer = input()
		if (answer == 'Y'):
			print("Deleting...")
			file = open('encryptedFile.txt', 'r+')
			file.truncate()
			file.close()
			print("ERADICATED")
			settingStart()
			return()
		elif (answer == 'N'): 
			settingStart()
			return()
		else: 
			deleteFile()
			return()

def decryption(): 
	file = open('encryptedFile.txt', 'r')
	num = file.read()
	num = str (num)
	print (num)
	i = num[0]
	j = num[1]
	k = num[2]
	l = num[3]
	print(i)
	i = int(i)-7
	j = int(j)-7  
	k = int(k)-7 
	l = int(l)-7
	print(i)
	i = i % 10
	j = j % 10
	k = k % 10
	l = l % 10
	print(i)


	i = str(i)
	j = str(j)
	k = str(k)
	l = str(l)
	print (i)

	decryptedNumber = k+l+i+j
	print(decryptedNumber)
	file.close()
	file = open('decryptedFile.txt', 'w')
	file.write(str(decryptedNumber))
	file.close()

	
	print('Decryption has been concluded')
	

	return()


	

	
settingStart()


exit()








 



