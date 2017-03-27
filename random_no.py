Python program - It will generate random numbers between 1 to 3 and display resultant text(number in words) accordingly.

run in File Editor (Pyhton - 3.6.0, File > New File > File Editor)


import random
def getA(ans):
	if ans == 1:
		return 'one'
	elif ans == 2:
		return 'two'
	elif ans == 3:
		return 'three'	

r= random.randint(1,3)
f= getA(r)
print (f)

