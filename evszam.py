year = int(input("Kerem adjon meg egy evszamot"))
if year < 1852:
	print("Nem Gergo")
elif not year % 4 and (year % 100 or not year % 400):
	print ("szoko")
else:
	print ("nem szokik")
