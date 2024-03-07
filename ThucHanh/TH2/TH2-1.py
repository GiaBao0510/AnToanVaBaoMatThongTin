from tkinter import *
#Khoi tạo màn hình
window = Tk()
window.title("Welcome to Demi An Toàn Bảo Mật Thông Tin")

#Row 0 - column 0
sp0 = Label(window, text=" ", font=('Arial Bold', 10))
sp0.grid(column=0,row=0)

#Row 1
sp1 = Label(window, text="CHƯƠNG TRÌNH DEMO", font=('Arial Bold', 20))
sp1.grid(column=1,row=1)

#Row 2
sp2 = Label(window, text="MẬT MÃ ĐỐI XỨNG DES", font=('Arial Bold', 17))
sp2.grid(column=1, row=2)

#Row 3: Bản gõ 
sp3t1 = Label(window, text='Văn bản gốc', font=('Arial',12), width=20)
sp3t1.grid(column=0, row=3)
sp3e1 = Entry(window, width=90, background='yellow')
sp3e1.grid(column=1, row=3)

#Row 4: Khóa
sp4t1 = Label(window, text='Khóa', font=('Arial',12), width=20)
sp4t1.grid(column=0, row=4)
sp4e1 = Entry(window, width=90, background='yellow')
sp4e1.grid(column=1, row=4)

#Row 5: Văn bản được mã hóa
sp5t1 = Label(window, text='Văn bản được mã hóa', font=('Arial',12), width=20)
sp5t1.grid(column=0, row=5)
sp5e1 = Entry(window, width=90, background='yellow')
sp5e1.grid(column=1, row=5)

#Row 6: Văn Bản được giải mã 
sp6t1 = Label(window, text='Văn Bản được giải mã', font=('Arial',12), width=20)
sp6t1.grid(column=0, row=6)
sp6e1 = Entry(window, width=90, background='yellow')
sp6e1.grid(column=1, row=6)

import base64                   #Thư viện này cung cấp các hàm để mã hóa và giải mã dữ liệu theo chuẩn Base64.
from Cryptodome.Cipher import DES   #Thư viện này cung cấp các hàm để mã hóa và giải mã dữ liệu theo thuật toán DES.


def pad(s):
    #Thêm vào cuối số còn thiếu cho đủ bội của 8
    kyTuConLai = chr(8 - len(s) % 8)            #Ky tự được chọn sau khi tính toán
    SoLuongKyTuConLai = (8 - len(s) % 8)        #So lượng ký tự còn lại
    return s + SoLuongKyTuConLai * kyTuConLai

def unpad(s):
    KyTuCuoiChuoi = chr( s[len(s)-1])         #Lấy ký tự cuối chuỗi
    SoMaAscci = ord( KyTuCuoiChuoi )    #Chuyển đổi ký tự cuối chuỗi sang thành số trong bảng mã Ascci
    loc = s[:-SoMaAscci]                #Loại bỏ số lượng các ký tự cuối
    return loc

def MaHoa_DES():
    #Lấy dữ liệu đầu vào
    txt = pad( sp3e1.get()).encode('utf8')  #Phương thức encode() dùng để mã hóa chuỗi bằng cách sử dụng mã chỉ định. Mặc định là utf8
    key = pad( sp4e1.get()).encode('utf8')

    '''
        Hàm DES.new(): Dùng để tạo 1 đối tượng mã hóa theo thuật toán DES. và hàm này nhận 2 tham số.
         + Key: khóa được sử dụng để mã hóa và giả mã dữ liệu. Khóa phải là 1 chuỗi byte có độ dài 8 byte.
         + mode: chế độ hoạt động của thuật toán:
            >  DES.MODE_ECB: Chế độ mã hóa khối điện tử (Electronic Codebook). 
            Mỗi khối dữ liệu được mã hóa độc lập với các khối khác.
            > DES.MODE_CBC: Chế độ mã hóa liên kết khối (Cipher Block Chaining). 
            Mỗi khối dữ liệu được mã hóa dựa trên kết quả mã hóa của khối trước đó.
    '''
    cipher = DES.new(key, DES.MODE_ECB)     #Vậy biến này dùng để mã hóa bản gõ dựa trên khóa
    entxt = cipher.encrypt(txt)             #Phương thức encrypt() dùng để mã hóa đối tượng văn bản
    entxt = base64.b64encode( entxt)        #Hàm này chuyển đổi văn bản sang dạng Base64. Việc chuyển đổi sang dạng Base64 giúp cho văn bản mã hóa dễ đọc và truyền tải hơn.
    
    #Hiển thị đoạn mã hóa
    sp5e1.delete(0, END)
    sp5e1.insert(INSERT, entxt)

def GiaiMa_DES():
    #Lấy dữ liệu đầu vào
    EnTxt = sp5e1.get() 
    EnTxt = base64.b64decode(EnTxt)         #Hàm b64decode() dùng để mã hóa chuỗi EnTxt từ dạng Base64 sang dạng bytes
    key = pad( sp4e1.get() ).encode('utf8')
    
    #Giải mã
    cipher = DES.new(key, DES.MODE_ECB)
    deTXT =  cipher.decrypt(EnTxt)  #Thực hiện giải mã
    deTXT = unpad( deTXT)

    #Ghi nhận lại giải mã
    sp6e1.delete(0, END)
    sp6e1.insert(INSERT, deTXT)


# >>> Hiển thị Luôn luôn ở cuối <<<
    #Nút bấm
ENCRYTIONbuttom = Button(window, text='Mẫ hóa', command= MaHoa_DES)
ENCRYTIONbuttom.grid(column=0, row=7)
DENCRYTIONbuttom = Button(window, text='Giải mã', command= GiaiMa_DES)
DENCRYTIONbuttom.grid(column=1, row=7)
    #Hiển thị
window.geometry('800x300')
window.mainloop()
