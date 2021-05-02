#找檔案在不在
import os


#讀取檔案
def read_file(filename):
    products = [] 
    with open(filename, 'r', encoding='utf-8') as f: #讀取檔案
        for line in f:
            if '商品,價格' in line: #更簡潔的寫
               continue
            name, price = line.strip().split(',')
            products.append([name, price])
    print(products)
    return products    

#輸入購買的商品
def user_input(products):
    while True:
        name = input('請輸入購買過的商品：')
        if name == 'q':
            break
        price = input('請輸入價格：')
        products.append([name, price])

    print(products)
    return products

#印出小清單內的內容
def print_products(products):
    for p in products:
        print(p[0], '的價格是', p[1]) 

#寫入檔案
def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f: 
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n')
        return filename

def main():
    filename = 'products.csv'
    if os.path.isfile(filename):
        print('找到檔案了')
        products = read_file(filename)
    else:
        print('沒有找到檔案')
    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

main()