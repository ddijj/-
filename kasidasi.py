import linecache

from tentoapp import *

x=1

def click():
    if e1.text in list_Product:
        list_a[list_Product.index(e1.text)] = list_a[list_Product.index(e1.text)]+1
        list_b[list_Product.index(e1.text)] = list_b[list_Product.index(e1.text)]+1
    else:
        list_Product.append(e1.text)
        list_a.append(1)
        list_b.append(1)
    print(list_Product)
    print(list_a)
    print(list_b)


def click2():
    if e1.text in list_Product:
        if list_a[list_Product.index(e1.text)]>0 :
            if list_a[list_Product.index(e1.text)]==list_b[list_Product.index(e1.text)]:
                list_b[list_Product.index(e1.text)] = list_b[list_Product.index(e1.text)]-1
            list_a[list_Product.index(e1.text)] = list_a[list_Product.index(e1.text)]-1
            print(list_a[list_Product.index(e1.text)])
            print(list_b[list_Product.index(e1.text)])

        else:
            print("在庫がありません")
    else:
        print("elar001")
    print(list_Product)
    print(list_a)
    print(list_b)

def click3():
    if e1.text in list_Product:
        if list_b[list_Product.index(e1.text)]>0:
            list_b[list_Product.index(e1.text)] = list_b[list_Product.index(e1.text)]-1
        else:
            print("在庫がありません")
    else:
        print("elar001")
    print(list_Product)
    print(list_a)
    print(list_b)

def click4():
    if e1.text in list_Product:
        if list_a[list_Product.index(e1.text)]>list_b[list_Product.index(e1.text)]:
            list_b[list_Product.index(e1.text)] = list_b[list_Product.index(e1.text)]+1
        else:
            print('elar002')
    else:
        print("elar001")
    print(list_Product)
    print(list_a)
    print(list_b)

def click5():
    with open('hello.txt', 'w') as f:
        for d in list_Product:
            f.write("%s\n" % d)
    with open('hello2.txt', 'w') as f:
        for d in list_a:
            f.write("%s\n" % d)
    with open('hello3.txt', 'w') as f:
        for d in list_b:
            f.write("%s\n" % d)

def click6():
    global list_Product,list_a,list_b
    with open('hello.txt','r') as f1:
        list_Product = [s.strip() for s in f1.readlines()]
    with open('hello2.txt','r') as f2:
        list_a = [s.strip() for s in f2.readlines()]
        list_a = [int(n) for n in list_a]

    with open('hello3.txt','r') as f3:
        list_b = [s.strip() for s in f3.readlines()]
        list_b = [int(n) for n in list_a]

    print(list_Product)
    print(list_a)
    print(list_b)




list_Product = ['book1','book2']
list_a=[3,2]
list_b=[3,2]

app = App()

e1 = Entry(app)
e1.pack()

b1 = Button(app)
b1.text = "在庫+"
b1.onclick = click
b1.pack()

b2 = Button(app)
b2.text = "在庫-"
b2.onclick = click2
b2.pack()

b3 = Button(app)
b3.text = "貸し出し"
b3.onclick = click3
b3.pack()

b4 = Button(app)
b4.text = "返却"
b4.onclick = click4
b4.pack()

b5 = Button(app)
b5.text = "保存"
b5.onclick = click5
b5.pack()

b6 = Button(app)
b6.text = "読み込み"
b6.onclick = click6
b6.pack()

app.start()

input()
