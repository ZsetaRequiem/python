#!/usr/bin/env python3

def myint (param):
	n = 0
	for i in param:
		k = ord(i)
		if k>=48 and k<=57:
			n = n*10 + (k-48)
		else:
			break
	return n

szoveg = input("Adjon meg egy szoveget: ")

try:
	assert  len(szoveg)>=1 and len(szoveg)<=12
except:
	print("Hibas szamot adtal meg!")
	exit()
print(myint(szoveg))
