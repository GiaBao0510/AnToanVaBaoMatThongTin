# Họ và tên sinh viên:  Phạm Gia Baoe
# Mã số sinh viên:  B2016947
# STT: 8

from tkinter import *
from tkinter import filedialog

window = Tk()
window.title("Welcome to Demo An Toan bao mat thong tin")

#Row 0
sp0 = Label(window, text='Chương Trình Demo', font=('Arial Bold',20))
sp0.grid(row=0,column=1)

#Row 1
sp1 = Label(window, text='Mật mã bất đối xứng RSA', font=('Arial Bold',18))
sp1.grid(row=1,column=1)

#Row 2: Văn bản gốc
sp2 = Label(window, text='Văn bản gốc', font=('Arial',12))
sp2.grid(row=2, column=0)
vanbangoc =  Text(window, wrap='word', width=50, height=1)
vanbangoc.grid(row=2, column=1)

#Row 3: Văn bản mã hóa
sp3 = Label(window, text='Văn bản mã hóa', font=('Arial',12))
sp3.grid(row=3, column=0)
vanmahoa = Text(window, wrap='word', width=50, height=1)
vanmahoa.grid(row=3, column=1)

#Row 4: Văn bản giải mã
sp4 = Label(window, text='Văn bản giải mã ', font=('Arial',12))
sp4.grid(row=4, column=0)
vangiaima =  Text(window, wrap='word', width=50, height=1)
vangiaima.grid(row=4, column=1)

#Row 5: Khóa cá nhân
sp5 = Label(window, text='Khóa cá nhân ', font=('Arial',12))
sp5.grid(row=5, column=0)
khoacanhan =  Text(window, wrap='word', width=50, height=10)
khoacanhan.grid(row=5, column=1)

#Row 6: Khóa công khai
sp6 = Label(window, text='Khóa cá nhân ', font=('Arial',12))
sp6.grid(row=6, column=0)
khoacongkhai =  Text(window, wrap='word', width=50, height=10)
khoacongkhai.grid(row=6, column=1)

# ------------ hàm hỗ trợ ----------------
    #Thu vien ho tro
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5
import base64

    #Tạo khóa
def generate_key():
    key = RSA.generate(1024)        #Tạo khóa có độ dài 1024 bit
    pri = save_file(                #Luu file khoa ca nhan
        key.exportKey('PEM'),                           #tham số 1: Xuất khóa sang định dạng PEM
        'wb',                                           #tham số 2: Chế đọ mở file(wb: nhị phân)
        'Lưu khóa cá nhân',                             #tham số 3: Tiêu đề hộp thoai lưu file
        (("All files","*.*"), ("PEM files","*.pem")),   #tham số 4: Loại file .pem 
        ".pem"                                          #tham số 5: Mở rộng file(.pem)
    )
    pub = save_file(
        key.publickey().exportKey('PEM'),
        'wb',
        'Lưu khóa công khai',
        (("All Files", "*.*"), ("PEM files","*.pem")),
        ".pem"
    )
    khoacanhan.delete('1.0', END)
    khoacanhan.insert(END, key.exportKey('PEM'))
    khoacongkhai.delete('1.0', END)
    khoacongkhai.insert(END, key.publickey().exportKey('PEM'))

    #Thủ tục lưu file
def save_file(content, _mode, _tile, _filetypes, _defaultextension):
    #ham asksaveasfile() dùng để mở hộp thoại lưu tệp và trả về 1 đối tượng file
    f = filedialog.asksaveasfile(           
        mode= _mode,                        #Tham số mode: chỉ định chế độ mở tệp
        initialdir= "D:/",                  #Thạm số initialdir: chỉ định thư mục ban đâu được hiên thị trong hộp thoại mở tệp 
        title= _tile,                       # tham số title: tiêu đề của hộp thoại
        defaultextension= _defaultextension # tham số defaultextension: chỉ định phần mở rộng cho tên tệp
    )
    if f is None: return
    f.write(content)
    f.close()

    #Lấy khóa
def get_key(key_style):
    filename = filedialog.askopenfilename(
        initialdir= "D:/",
        title= "Open" +key_style,
        filetypes= (("PEM files","*.pem"), ("All files", "*.*"))
    )

    if filename is None: 
        return
    with open(filename, 'rb') as file:
        key = file.read()
    return RSA.importKey(key)   #Hàm importKey() dùng để lấy 1 chuỗi bytes đầu vào và trả vè 1 đối tượng RSA

def mahoa_rsa():
    txt = vanbangoc.get('1.0',END).encode('utf8')      #Lấy nội dung từ widget vanbangoc
    pub_key = get_key("public_key")     #Lấy nội dung khóa công khai được lưu ở noi nào đó trong ổ đĩa D
    cipher = PKCS1_v1_5.new(pub_key)    #Tạo ra 1 đối tượng bị mã hóa dựa trên pub_key
    entxt = cipher.encrypt(txt)         #Thực hiện mã hóa bản gõ
    entxt = base64.b64encode(entxt)     # Mã hóa chuỗi byte "entxt" sang dạng base64
    vanmahoa.delete("1.0",END)
    vanmahoa.insert(INSERT,entxt)

def giaima_rsa():
    #Doc van ban và mã hóa chuỗi
    cipherText = vanmahoa.get('1.0',END)
    cipherText = base64.b64decode(cipherText)

    #Lấy nội dung tệp tin
    privateKey = get_key("private_key")

    #Thục hiện giải mã
    cipher = PKCS1_v1_5.new(privateKey)
    bangoc = cipher.decrypt(cipherText, sentinel=None)

    #Ghi nhan
    vangiaima.delete("1.0",END)
    vangiaima.insert(INSERT, bangoc)


# ----------------------------------------

#Row 7: tạo khóa
taokhoa  =  Button(window, text='Tạo khóa', command= generate_key)
taokhoa.grid(row=7, column=1)

#Row 8: mã hóa
mahoa  =  Button(window, text='Mã khóa', command= mahoa_rsa)
mahoa.grid(row=8, column=1)

#Row 9: giải mã
giaima  =  Button(window, text='Giải mã', command=giaima_rsa)
giaima.grid(row=9, column=1)

#Chạy 
window.geometry("650x600")
window.mainloop()