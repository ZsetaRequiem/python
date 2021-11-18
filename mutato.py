#!/usr/bin/env python3
import math
class pont:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def tav(self,pont):
		return math.sqrt((pont.x - self.x)**2 + (pont.y - self.y)**2)

class haromszog:
	def __init__(self,a,b,c):
		self.a = a
		self.b = b
		self.c = c
	def ker(self):
		return self.a.tav(self.b) + self.b.tav(self.c) + self.c.tav(self.a)

try:
	x1 = int(input("A.x: "))
	y1 = int(input("A.y: "))

	x2 = int(input("B.x: "))
	y2 = int(input("B.y: "))

	x3 = int(input("C.x: "))
	y3 = int(input("C.y: "))

	p1 = pont(x1,y1)
	p2 = pont(x2,y2)
	p3 = pont(x3,y3)

	h = haromszog(p1,p2,p3)
	print(h.ker())
except:
	print("HIBA")
