#!/usr/bin/env python3
szov = input("Adj meg egy szoveget: ")
try:
	elt = int(input("Adj meg egy szamot: "))
	assert elt>=1 and elt<=25
except:
	print("Hibas szamot adtal meg")
	exit()

for i in szov:
	kod = ord(i)
	if kod >= 65 and kod <= 90:
		kod +=elt 
		if code > 122:
			code -=26
		print(chr(code), end = "")
	elif code >= 65 and code <= 90:
		code += x
		if code > 90:
			code -= 26
		print(chr(code), end = "")
	else: 
		print(i, end = "")
print("")

