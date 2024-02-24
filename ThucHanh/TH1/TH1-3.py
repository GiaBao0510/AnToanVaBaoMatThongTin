# Ho va ten sinh vien: Pham Gia Bao
# Ma so sinh vien:  B2016947
# STT:  8

from tkinter import *

''' ---- Bước 1: Tạo giao diện ----'''
#Khoi tao man hinh chinh
window = Tk()
window.title("Welcome to Demo An Toan va Bao Mat An Toan Thong Tin")    #Tieu de

#Them cac control
#---- Row0
lb0 = Label(window, text=" ", font=("Arial Bold", 10))
lb0.grid(column=0, row=0)

#---- Row1
lb1 = Label(window, text="CHƯƠNG TRINH DEMO", font=("Arial Bold", 20))
lb1.grid(column=1, row=1)

#---- Row2
lb2 = Label(window, text="MẬT MÃ AFINE", font=("Arial Bold",15))
lb2.grid(column=0,row=2)

#---- Row3
plainlb3 = Label(window, text="PLAIN TEXT", font=("Arial",14) )
plainlb3.grid(column=0, row=3)
plaintxt = Entry(window, width=20)
plaintxt.grid(column=1, row=3)
KEYlb4 = Label(window, text="KEY PAIR", font=("Arial",14) )
KEYlb4.grid(column=2, row=3)
KEYA1 = Entry(window, width=3)
KEYA1.grid(column=3, row= 3)
KEYB1 = Entry(window, width=5)
KEYB1.grid(column=4, row= 3)
ENCRYTIONbuttom = Button(window, text="Mã hóa")
ENCRYTIONbuttom.grid(column=5, row= 3)

#---- Row4
cipherlb4 = Label(window, text="CIPHER TEXT", font=("Arial",14) )
cipherlb4.grid(column=0, row=4)
ciphertxt = Entry(window, width=20)
ciphertxt.grid(column=1, row=4)
DENCRYTIONbuttom = Button(window, text="Giải mã")
DENCRYTIONbuttom.grid(column=3, row= 4)
DENCRYTIONtxt = Entry(window, width=15)
DENCRYTIONtxt.grid(column=4, row= 4)



''' ---- Bước 2: Cài đặt các sự kiện click ----'''

#2.Cai dat cac ham can thiet

    #>>>> Ky tu ghi hoa
def Char2Num(c):
    if c.isnumeric():
        return ord(c) - 48
    elif c.isupper():
        return ord(c) - 65 + 10
    elif c.islower():
        return ord(c) - 97 + 36
    else:
        return -1

def Num2char(c):
    #Ham chr() dung de tra ve 1 ky tu dua tren so nguyen
    if  0 <= c < 10:
        return chr(c + 48)
    elif 10 <= c < 36:
        return chr(c + 65 - 10)
    elif 25 < c < 52:
        return chr(c + 97 - 36)
    else:
        return ""

def encrypAF(txt,a,b,m):
    r=""
    #Vong lap nay dung de lay tung ky tu
    print("  ----- Mã Hóa  ------")
    print("a = {0}, b = {1}, m = {2}".format(a,b,m))
    for c in txt:
        print("- ký tự: ",c)
        #Kiem tra chu cai
        if c != " ":
            e = (a * Char2Num(c)+b)%m   #Ma tung ky tu sang so nguyen
            print("\t > E: ",e)
            r += Num2char(e) 
            print("\t > R: ",r)
        else:
            r += "+"
    return r

#danh cho nut ma hoa
def mahoa():
    a = int(KEYA1.get())
    b = int(KEYB1.get())
    m = 26
    entxt = encrypAF( plaintxt.get() ,a,b,m)

    #hien thi
    ciphertxt.delete(0, END)            #Lam rong
    ciphertxt.insert(INSERT, entxt)     #Them van ban da ma hoa

def xgcd(a,m):
    temp = m
    x0,x1,y0,y1 = 1,0,0,1
    while m!=0:
        q,a,m = a // m, m, a%m  #q = a//m, a=m, m=a%m
        x0,x1 = x1, x0 - q *x1  # x0 = x1, x1 = x0 - q *x1
        y0, y1 = y1, y0-q*y1    #y0 = y1, y1 = y0 - q *y1
    if x0 < 0: temp+x0
    return x0

def decryptAF(txt,a,b,m):
    vb = ""
    a1=xgcd(a,m)
    print("  ----- Giải mã ------")
    print("a = {0}, b = {1}, m = {2}, ƯỚc chung({3},{4}) = {5}".format(a,b,m,a,b, a1))
    for c in txt:
        print("- ký tự: ",c)
        if c != "+":
            D =  (a1 * (Char2Num(c) - b))%m
            print("\t > D: ",D)
            vb = vb + Num2char(D)
            print("\t > vb: ",vb)
        else:
            vb += " "
    return vb

#Danh cho nut giai ma
def giaima():
    a = int(KEYA1.get())
    b = int(KEYB1.get())
    m =26

    VBmahoa = str(ciphertxt.get())
    detxt = decryptAF(VBmahoa, a, b, m)

    #hien thi
    DENCRYTIONtxt.delete(0, END)
    DENCRYTIONtxt.insert(INSERT, detxt)

#1. Them su kien ma hoa
ENCRYTIONbuttom = Button(window, text="Mã hóa", command=mahoa)          #Da them su kien ma hoa
ENCRYTIONbuttom.grid(column=5, row= 3)

DENCRYTIONbuttom = Button(window, text="Giải mã", command=giaima)                        #Da them su kien giai ma
DENCRYTIONbuttom.grid(column=3, row= 4)

#Hien thi cua so
window.geometry('800x300')
window.mainloop()