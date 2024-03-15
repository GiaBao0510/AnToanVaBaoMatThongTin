# Họ và tên sinh viên: Phạm Gia Bảo
# Mã số sinh viên:  B2016947
# STT:  8

from tkinter import *
from tkinter import filedialog

window = Tk()
window.title("Welcome tp Demo An Toan Bao Mat Thong Tin")

#Row 0
sp0 = Label(window, text='')
sp0.grid(row=0,column=0)

#Row 1 
sp1 = Label(window, text='Chương trình Băm', font=('Arial Bold',20))
sp1.grid(row=1, column=1)

#Row 2
sp2 = Label(window, text='Văn bản', font=('Arial',20))
sp2.grid(row=2, column=0)
bango = Text(window, wrap='word', width=50, height=1)
bango.grid(row=2, column=1)

#Row 3 
radioGroup = LabelFrame(window, text='Hàm Băm')
radioGroup.grid(row=3, column=1)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import MD5, SHA1, SHA256, SHA512
from Crypto.Cipher import PKCS1_v1_5
import base64

chedobam = IntVar()
chedobam.set(-1)

def hashing():
    content = bango.get('1.0',END).encode()
    func = chedobam.get()

    if func == 0:
        result = MD5.new(content)
    elif func == 1:
        result = SHA1.new(content)
    elif func == 2:
        result = SHA256.new(content)
    elif func == 3:
        result == SHA512.new(content)
    
    #Cập nhật kết quả sau khi nó được xác định
    rs = result.hexdigest().upper()

    giatribam.delete("1.0",END)
    giatribam.insert(INSERT,rs)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#Row 4: Hash MD5
MD5_func = Radiobutton(radioGroup, text='Hash MD5', font=('Times New Roman', 11), variable=chedobam, value=0, command=hashing )
MD5_func.grid(row=4, column=0)

#Row 5: hàm băm sha1
SHA1_func = Radiobutton(radioGroup, text='Hash SHA1', font=('Times New Roman',11), variable=chedobam, value=1, command=hashing)
SHA1_func.grid(row=5, column=0)

#Row 6: hàm băm sha256
SHA256_func = Radiobutton(radioGroup, text='Hash SHA256', font=('Times New Roman',11), variable=chedobam, value=2, command=hashing)
SHA256_func.grid(row=6, column=0)

#Row 7: hàm băm sha512
SHA512_func = Radiobutton(radioGroup, text='Hash SHA512', font=('Times New Roman',11), variable=chedobam, value=3, command=hashing)
SHA512_func.grid(row=7, column=0)

#Row 8: Giá trị băm
sp3 = Label(window, text='Giá trị băm', font=('Arial', 15))
sp3.grid(column=0, row=8)
giatribam = Text(window, wrap='word', width=50, height=1)
giatribam.grid(column=1, row=8)

#-----------
window.geometry('550x300')
window.mainloop()