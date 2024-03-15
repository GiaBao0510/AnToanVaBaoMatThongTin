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

    #1.Hàm tạo tẹp tin
def TaoTepTin(pathFileCSV):
    try:
        open(pathFileCSV, "r")
        print('>>> Tệp tin đã tồn tại')
    except:
        #Nếu tệp tin không tồn tại thì tạo
        open(pathFileCSV, "x")
        print(">>> Đã tạo tệp tin")

TaoTepTin("CSDL.csv")

    #2. Lấy thông tin tên đăng nhập và mật khẩu lưu vào tẹp tin
def GhiVaoTepTin(pathfile,taikhoan,matkhau):
    #Cắt bỏ khoảng trống thừa
    taikhoan = re.sub(r"\s+","",taikhoan)
    matkhau = re.sub(r"\s+","",matkhau)
    
    with open(pathfile,"a+", encoding='utf-8') as file:
        file.write(taikhoan+","+matkhau+"\n")
 
    #3. Kiểm tra tài khoản đã tồn tại hay chưa.(Cóa trả về 1, ngược lại là 0)
def KiemTraTaiKhoanDaTonTai(pathfile ,taikhoan):
    with open(pathfile) as f:
        csv_read = csv.reader(f, delimiter=',')
        for row in csv_read:
            if row[0] == taikhoan:
                return 1
    return 0

    #4. lấy tải khoản và mật khẩu(Đã bị băm) rồi ghi vào cuối file
def luuTaiKhoan():
    csdl = './CSDL.csv'
    #lấy tài khoản
    taikhoan = username.get('1.0',END)
    taikhoan = taikhoan.strip()
    #Kiem tra tai khoan da ton tai
    if KiemTraTaiKhoanDaTonTai(csdl, taikhoan.strip()) == 1:
        print("Tai khoan da ton tai")
    else:
        #lấy mật khẩu
        pw = password.get('1.0',END).encode()

        #Random ham bam
        chedobam = random.randint(0,3)

        if chedobam == 0:
            result = MD5.new(pw)
        elif chedobam == 1:
            result = SHA1.new(pw)
        elif chedobam == 2:
            result = SHA256.new(pw)
        elif chedobam == 3:
            result == SHA512.new(pw)

        rs = result.hexdigest().upper()
        rs = str(rs).strip()
        #Luu vao tẹp tin
        print("Da them du lieu thanh cong")
        GhiVaoTepTin(csdl,taikhoan,rs)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#row 3: Nút tạo tài khoản
taotaikhoan = Button(window, text="Tạo tài khoản", command=luuTaiKhoan)
taotaikhoan.grid(row=3, column=1)

#----------
window.geometry('450x150')
window.mainloop()