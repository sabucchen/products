
products = []
while True:
	name = input('請輸入購買過的商品：')
	if name == 'q':
		break
	price = input('請輸入價格：')
	#苦幹型寫法
	# p = []
	# p.append(name)
	# p.append(price)
	# products.append(p)

	#進階型寫法
	# p = [name, price]
	# products.append(p)

	#超級強寫法
	products.append([name, price])

print(products)

for p in products:
	#印出小清單內的內容
	#print(p)

	#再進階一點應用
	print(p[0], '的價格是', p[1])

with open('products.txt', 'w') as f:
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')

with open('products.csv', 'w') as f: 
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')


