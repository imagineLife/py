pets = ['cat','lion','tiger', 'dog','giraffe']
for itm in pets:
	print('I have a {0}'.format(itm))

for i in range(5):
	print(i)

for itm in range(10,15):
	print(itm)

for itm in range(10,20,2):
	print(itm)

for itm in range(10,0,-3):
	print(itm)

for p in pets:
	if p == 'dog':
		print('no dogs allowed! stopping loop')
		break
	else:
		print(p)