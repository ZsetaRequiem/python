#!/usr/bin/env python3
my_list=[1,2,4,4,1,4,2,6,2,9]
egyedi=[]
for number in my_list:
	if number not in egyedi:
		egyedi.append(number)
print("A lista egyedi elemekkel")
print(egyedi)
