# 打開文件檔，將文件檔內資料轉成list
products = []
with open('product.csv', 'r', encoding = 'utf-8') as f:
    for line in f:
        if '商品,價格' in line: # 跳過第一列資料
            continue # 跳到迴圈下一round
        name, price = line.strip().split(',') # 用split(',')來用逗點做分割，分割完的結果是list；用strip來除掉換行符號
        products.append([name, price])
print(products)

# 輸入商品名稱、價格，並存到文件檔
while True:
    name = input("請輸入商品名稱 : ")
    if name == 'q':
        break
    price = input("請輸入商品價格 : ")
    products.append([name, price]) # 將list append進list內
print(products)

# 印出所有購買紀錄
for p in products:
    print(p[0], "的價格是 :", p[1])

# 寫入檔案
with open('product.csv', 'w', encoding = 'utf-8') as f: # 開啟(沒有的話就建立)product.csv檔案，並設為寫入模式
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n') # csv檔可用excel開啟，用逗號來放在excel的不同行，用\n來放在不同列