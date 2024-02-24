def Char2Num(c):
    #Hamf ord() tra ve so nguyen cho ma Unicode theo ky tu
    return ord(c) - 65

def Num2char(c):
    #Ham chr() dung de tra ve 1 ky tu dua tren so nguyen
    return chr(c + 65)

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

#Giải bài toán
DoanMaHoa = "LOLYLTQOLTHDZTDC"
TuKhoa = "LAMUOI"
m = 26
kq = 0
VBtimThay = ""
#Khoa a
for a in range(1,27):
    #Khoa b
    for b in range(1,27):
        #print(decryptAF(DoanMaHoa,a,b,m))
        if TuKhoa in decryptAF(DoanMaHoa,a,b,m):
            #print("Da tim thay: ", decryptAF(DoanMaHoa,a,b,m))
            VBtimThay = decryptAF(DoanMaHoa,a,b,m)
            kq = 1

            break
if kq == 0:
    print("Không tìm thấy")
else: 
    print("Đã tìm thấy: ",VBtimThay)
        

