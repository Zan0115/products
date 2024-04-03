products = []
while True:
    name = input("請輸入商品名稱 : ")
    if name == 'q':
        break
    price = input("請輸入商品價格 : ")
    products.append([name, price]) # 將list append進list內
print(products)

for p in products:
    print(p[0], "的價格是 :", p[1])

with open('product.csv', 'w') as f: # 開啟(沒有的話就建立)product.csv檔案，並設為寫入模式
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n') # csv檔可用excel開啟，用逗號來放在excel的不同行，用\n來放在不同列