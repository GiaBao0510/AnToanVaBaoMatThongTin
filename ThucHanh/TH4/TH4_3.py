# Họ và tên sinh viên: Phạm Gia Bảo
# Mã số sinh viên:  B2016947
# STT:  8

from tkinter import *
from tkinter import filedialog
import csv
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import MD5, SHA1, SHA256, SHA512
from Crypto.Cipher import PKCS1_v1_5
import base64
import random
import re

# ^^ Giao diện ^^
window = Tk()
window.title("Welcome to Demo An Toàn Bảo Mật Thông Tin")

#row 0
sp0 = Label(window, text="Tạo tài khoản", font=('Arial Bold',20))
sp0.grid(column=1, row=0)

#row 1: username
sp1 = Label(window, text="Tên đăng nhập", font=('Arial ',15))
sp1.grid(row=1, column=0)
username = Text(window, wrap='word', width=30, height=1)
username.grid(row=1, column=1)

#row 2: password
sp2 = Label(window, text="Mật khẩu", font=('Arial ',15))
sp2.grid(row=2, column=0)
password = Text(window, wrap='word', width=30, height=1)
password.grid(row=2, column=1)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    #1. Lấy thông tin tên đăng nhập và mật khẩu lưu vào tẹp tin
def GhiVaoTepTin(pathfile,taikhoan,matkhau):
    #Cắt bỏ khoảng trống thừa
    taikhoan = re.sub(r"\s+","",taikhoan)
    matkhau = re.sub(r"\s+","",matkhau)

    with open(pathfile,"a+", encoding='utf-8') as file:
        file.write(taikhoan+","+matkhau+"\n")
 
    #2. Kiểm tra tài khoản đã tồn tại hay chưa.(Cóa trả về 1, ngược lại là 0)
def KiemTraTaiKhoanDaTonTai(pathfile ,taikhoan):
    with open(pathfile) as f:
        csv_read = csv.reader(f, delimiter=',')
        for row in csv_read:
            if row[0] == taikhoan:
                return 1
    return 0

    #3. Kiểm tra mật khâu đã tồn tại hay chưa.(Cóa trả về 1, ngược lại là 0)
def KiemTraMatKhauDaTonTai(pathfile ,matkhau):
    with open(pathfile) as f:
        csv_read = csv.reader(f, delimiter=',')
        for row in csv_read:
            if row[1] == matkhau:
                return 1
    return 0

    #4. lấy tải khoản và mật khẩu(Đã bị băm) rồi ghi vào cuối file
def luuTaiKhoan():
    csdl = './CSDL.csv'
    #lấy tài khoản
    taikhoan = username.get('1.0',END)
    taikhoan = taikhoan.strip()
    #Lấy mật khẩu
    matkhau = password.get('1.0',END).encode()

    #Kiem tra tai khoan da ton tai
    if KiemTraTaiKhoanDaTonTai(csdl, taikhoan.strip()) == 1:
        print("Tai khoan da ton tai")

        #nếu tài khoan đã tồn tại thì tìm dòng chưa tài khoản để lưu mật khẩu
        with open(csdl) as f:
            csv_read2 = csv.reader(f, delimiter=',')
            LayMatKhauBibam = ''
            #Tìm kiếm tai khoan
            for row in csv_read2:
                if taikhoan == row[0]:
                    LayMatKhauBibam = str(row[1])
        
        #Từ mật khẩu trên. Băm nó rồi lưu vào danh sách
        listHashPW = []

        md5 = MD5.new(matkhau)
        md5 = md5.hexdigest().upper().strip()
        sha1 = SHA1.new(matkhau)
        sha1 = sha1.hexdigest().upper().strip()
        sha256 = SHA256.new(matkhau)
        sha256 = sha256.hexdigest().upper().strip()
        sha512 = SHA512.new(matkhau)
        sha512 = sha512.hexdigest().upper().strip()
            #Lưu
        listHashPW.append(md5)
        listHashPW.append(sha1)
        listHashPW.append(sha256)
        listHashPW.append(sha512)
        
        #Lấy mật khẩu thật so sánh trong danh sách mật khẩu đã băm đển kiểm tra
        thanhcong = 0
        for i in listHashPW:
            if i == LayMatKhauBibam:
                thanhcong = 1
                break

        if thanhcong == 1:
            print("Đăng nhập thành công")
        else: 
            print("Đăng nhập thất bại")
                    
    else:
        print("Đăng nhập thất bại")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#row 3: Nút tạo tài khoản
taotaikhoan = Button(window, text="Đăng nhập", command=luuTaiKhoan)
taotaikhoan.grid(row=3, column=1)

#----------
window.geometry('450x150')
window.mainloop()