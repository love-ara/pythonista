price = int(input("Enter the price of your car :"))

if price < 1000000:
	tax = (10/100)* price 
	print('your tax rate is ', tax)

if price == 1000000 and price < 3000000:
	tax = (15/100)* price 
	print('your tax rate is ', tax)

if price == 3000000 and price < 5000000:
	tax = (20/100)* price
	print('your tax rate is ', tax)

if price >= 5000000:
	tax = (25/100)* price
	print('your tax rate is ', tax)
