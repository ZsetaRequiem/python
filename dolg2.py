import sys

try:
	a = sys.argv[1]
	f = open(a,"rt")
	w = open(a + "-out.txt","wt")
	line = f.readline()
	while line:
		w.write(line.upper())
		line = f.readline()
		w.write(line.lower())
		line = f.readline()
	f.close()
	w.close
except:
	print("Hiba!")
