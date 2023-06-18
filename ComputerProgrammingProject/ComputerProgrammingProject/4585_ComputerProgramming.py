#Welcome to my computer programming project
#SkillsUSA CA
#Region 4 Competition 2023
#Computer Programming
#Contestant ID: 4585

import time
import csv

#tells you what the error is when you put over 4 digits
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
#this is the encryption itself with sum+7 modulo 10
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
	
	file = open('encryptedFile.txt', 'w') #this is the .txt file that will hold the encrypted number of 4 digits. Check for encrypted number
	file.write(str(encryptedNumber))
	file.close()

	
	print('Encryption has concluded and has been stored')
	settingMain()

	return()
   
	
	


#this is the setting for the encryption and decryption. After you encrypt using 'W', this will give the user the option to decrypt or encrypt that encrypted number 
def settingMain(): 
	print('If you want to encrypt this number press: R. If you want to dycrypt, press D. If you want to delete file, press T ')
	encryptER = input()
	if (encryptER == 'E'):
		numType()
	elif (encryptER == 'R'): 
		print('Loading Encryption...')
		encryption(num)
		return() 
	elif (encryptER == 'T'): 
		print ('Deleting File...')
		deleteFile()
		return()
	elif (encryptER == 'D'): 
		print('Loading Decryption...')
		time.sleep(1)
		decryption()
		return()
	
#this will be the frist thing that pops up, it will give you the option to encrypt
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
		print('Must be W or L or T')
		time.sleep(0.5)
		settingStart()
#the commands here are to delete/remove the file
def deleteFile(): 
	print('Do you want to clear the file? Y or N')
	encryptER = input()
	if(encryptER == "Y"):
		print ('Are you positive?') 
		if (encryptER == 'Y'):
			print("Deleting...")
			file = open('profileEncrypt.txt', 'r+')
			file.truncate()
			file.close()
			print("ERADICATED")
			settingStart()
			return()
	if (encryptER == 'N'):
		settingStart()
		return()
#this is the dycryption itself and all the math and logic to decrypt the encrypted number
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
	file = open('decryptedFile.txt', 'w') #this is the .txt file that is will be stored in. Check for decyrpted number
	file.write(str(decryptedNumber))
	file.close()

	
	print('Decryption has been concluded')
	

	return()


	
settingStart()


exit()








 #first encryption
 #first dycryption



