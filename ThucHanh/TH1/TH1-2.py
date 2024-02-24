# Ho va ten sinh vien: Pham Gia Bao
# Ma so sinh vien:  B2016947
# STT:  8

def Char2Num(c):
    #Hamf ord() tra ve so nguyen cho ma Unicode theo ky tu
    return ord(c) - 65

def Num2char(c):
    #Ham chr() dung de tra ve 1 ky tu dua tren so nguyen
    return chr(c + 65)

'''
    - Ham nay dung de ma hoa chuoi dau vao voi cac tham so nhu sau:
        + txt: Van ban dau vao
        + a
        + b
        + m: mod
'''
def encrypAF(txt,a,b,m):
    r=""
    #Vong lap nay dung de lay tung ky tu
    for c in txt:
        e = (a * Char2Num(c)+b)%m   #Ma tung ky tu sang so nguyen
        #print(" - so dau:{0} so e: {1} + Chu: {2} ".format(Char2Num(c),e,Num2char(e)))
        r = r+Num2char(e)           #Ghi nhan lai ket qua ma hoa cua tung ky tu
    return r


#-----------------------------------
#Chuong trinh euclid extended de tim uoc so chung lon nhat
def xgcd(a,m):
    temp = m
    x0,x1,y0,y1 = 1,0,0,1
    while m!=0:
        q,a,m = a // m, m, a%m  #q = a//m, a=m, m=a%m
        x0,x1 = x1, x0 - q *x1  # x0 = x1, x1 = x0 - q *x1
        y0, y1 = y1, y0-q*y1    #y0 = y1, y1 = y0 - q *y1
    if x0 < 0: temp+x0
    return x0

'''
    - Ham nay dung de giai hoa chuoi dau vao voi cac tham so nhu sau:
        + txt: Van ban dau vao
        + a
        + b
        + m: mod
'''
def decryptAF(txt,a,b,m):
    vb = ""
    a1=xgcd(a,m)
    for c in txt:
        #Giai ma tung ky tu dau vao
        D =  (a1 * (Char2Num(c) - b))%m
        vb = vb + Num2char(D)
    return vb

#Hien thi
plaintext = "HELLOWORLD"
a,b = 7,3       #Cặp khóa
print("Input: ",plaintext)
print("Encrytion: ",encrypAF(plaintext,a,b,26))
print("Dencrytion: ",decryptAF(encrypAF(plaintext,a,b,26) ,a,b,26) )