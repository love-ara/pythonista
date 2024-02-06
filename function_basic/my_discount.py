
def discounter(price, discount):
	discount = discount/100
	price = price
	discounted_price = price - (price * discount)
	return discounted_price

#print(discounter(150, 15))	