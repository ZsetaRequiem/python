#! /usr/bin/env python3

def myupper(str):
	szo = ""
	for i in str:
		if 'a' <= i <= 'z':
			szo +=chr(ord(i) - 32)
		else:
			szo+= i
	return szo

szovag = input("")

print(myupper(szovag))
