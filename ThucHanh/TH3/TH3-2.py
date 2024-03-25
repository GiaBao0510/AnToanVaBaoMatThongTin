# Họ và tên sinh viên:  Phạm Gia Baoe
# Mã số sinh viên:  B2016947
# STT: 8

    # >>> thêm thư viện <<<<<
import random

    # >>>> Các hàm xử lý <<<<
#Uoc so chung lơn nhat
def gcd(a,b):
    if a > b:
        r = a%b
        if r == 1:
            return 1
        elif r > 0:
            return gcd(b,r)
        elif r == 0:
            return 0
    else:
        return 0

def Euclide_moRong(a,b):
    tempQ = a
    #Khoi tạo biến
    x0,x1,y0,y1 = 0,1,1,0
    
    while True:
        r = a%b
        if r == 0:
            break 
        q = a//b
        x = x1 - q*x0
        y = y1 - q*y0
        
        a,b = b,r
        x0 , x1 ,y0 ,y1 = x, x0, y, y0
    return tempQ+y

#3. Kiểm tra số nguyên tố
def kiemtrasonguyento(num):
    for i in range(2,num):
        j = num -1
        if num % i == 0:
            return 0
        if num % j == 0:
            return 0
        if j > i:
            j -=1
    return 1

#4. Hàm trả vể 2 số nguyên tố ngẫu nhiên
def HaiSoNguyenToNgauNhien(ds):
    #Biến hỗ trợ
    mucDau = 10
    mucDuoi = 20
    temp = []

    #Chọn p
    p = ds[ random.randint(mucDau, mucDuoi) ]
    temp.append(p)
    
    #Nếu số chọn khác nhau thì hủy vòng lặp
    while True:
        q = ds[ random.randint(mucDau, mucDuoi) ]
        if p != q:
            temp.append(q)
            break
    return temp

listSoNguyenTo = [] #Danh sách số nguyên tố

#Lưu các sô nguyên tố và danh sách
file = open('DanhSachSoNguyenTo.txt','r')
DauVao = file.readline()        #Chuỗi đầu vào
DauVao = DauVao.split()         #Phân tách chuỗi thành danh sách dựa trên khoảng cách
DauVao = list(map(int, DauVao)) #Thay đổi tất cả các phần tử trong danh sách sang kiểu số nguyên

#Sinh khóa
def SinhKhoa():
    #1. Chọn P,Q hai số nguyên tố ngẫu nhiên
    q,p = HaiSoNguyenToNgauNhien(DauVao)
    #2. Tính n
    n =q * p
    #3. Tính phi
    phi = (q-1)*(p-1)
    #4.Tạo danh sách các số ngẫu nhiên từ 1 đến phi và sau đó chọn e ngẫu nhiên xuất hiện trong danh sách
    danhsach1 = []
    for i in range(1,phi +1):
        if gcd(phi, i) == 1:
            danhsach1.append(i)
    e = danhsach1[ random.randint(0, len(danhsach1) -1) ]
    #5. Tính D
    d = Euclide_moRong(phi, e)

    return e,d,n

# Sinh khóa Cá nhân
def PrivateKey(E, P, N):
    C = (P**E)%N 
    return C

# Sinh khóa công khai
def PublicKey(D, C ,N):
    P = (C**D )% N
    return P

#>>>Mã hóa
def MaHoa(text , E, N):
    VanBanMaHoa = str()
    for i in text:
        soThapPhan = ord(i)                                 #Chuyen cac ky tu ve dang thap phân
        soThapLucPhan = hex( PublicKey(E, soThapPhan, N))   #Chuyển các lý tự từ hệ thập phân sang thập lục phân
        VanBanMaHoa += soThapLucPhan
    return VanBanMaHoa

#>>>Giải mã
def GiaiMa(cipherText , D, N):
    tach = cipherText.split('0x')        #tách để tạo ra danh sách dựa trên "0x"
    tach = tach[1:]                      #Loại bỏ phần tử đầu. Vì nó là khoảng trống
    tach = [ int(x,16) for x in tach]    #Chuyển tất cả các phần tử bên trong danh sách từ hệ thập lục phân sang hệ thập phân

    #Chuyển các phần tử bên trong về dạng số nguyên
    ghinhan = ''
    for i in range(len(tach)):
        ghinhan +=  str( chr(PrivateKey(D, tach[i], N)))
        
    return ghinhan

#------ Chạy ---------
plaitText = "SECRET OK"        #Bản gõ
print('Bản gõ: ',plaitText)
E,D,N = SinhKhoa()               #sinh khóa
print("E: ",E," - D: ",D," - N: ",N)

mh =  MaHoa(plaitText , E, N)
print(" - Van Ban Ma Hoa: ",mh)
print(' - Giải mã: ',GiaiMa(mh , D, N))