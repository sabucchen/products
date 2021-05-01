#讀取檔案
products = []

with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		#土方法把s取到的東西丟到name,price
		# s = line.strip().split(',')
		# name = s[0]
		# price = s[1]

		#更簡潔的寫
		name, price = line.strip().split(',')
		products.append([name, price])
print(products)



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

# with open('products.txt', 'w') as f:
# 	for p in products:
# 		f.write(p[0] + ',' + p[1] + '\n')

with open('products.csv', 'w', encoding='utf-8') as f: 
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')


