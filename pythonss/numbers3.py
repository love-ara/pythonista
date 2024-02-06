number = 0
square = 0
cube = 0

print('number\tsquare\tcube')

for number in range(0, 6):
	square = number * number
	cube = number * number * number
	print('{0:6d}\t{1:6d}\t{2:3d}'.format(number, square,cube))