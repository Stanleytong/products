products = []

while True:
	name = input('請輸入產品名稱： ')
	if name == 'q':
		break
	price = input('請輸入產品價錢： ')
	products.append([name, price])
print(products)

print (products[1][0])

for p in products:
	print(p[0], '的價格是', p[1])