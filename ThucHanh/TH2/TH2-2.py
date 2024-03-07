from tkinter import *
from tkinter import filedialog

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

#Row 3: Hiển thị văn bản
hienThiVanBan = Text(window, wrap='word', width=80, height=20)
hienThiVanBan.grid(column=1 , row=3)

# ------------------------------------------------------
    #Hàm mở văn bản txt
def OpenFile():
    #Phương thức askopenfiles(): Dùng để mở hộp thoại và chọn tệp tin đã được chỉ định
    pathFile = filedialog.askopenfiles(
        title="Chọn tệp tin văn bản",
        filetypes=[("Tệp tin văn bản","*.txt")]
    )
    #Đọc tệp tin
    f = open( pathFile[0].name ,'r')

    if pathFile:    #Kiểm tra có phải tệp tin đã đọc hay không, nếu không thì hiển thị thông báo lỗi
        #Ghi van ban dã đọc
        hienThiVanBan.delete("1.0", END)
        hienThiVanBan.insert(INSERT, f.read())
    else: 
        hienThiVanBan.delete("1.0", END)
        hienThiVanBan.insert(INSERT, "Error")

    f.close()

#-------------------------------------------------------

#Row 4: nút mở văn bản
nutTepTin = Button(window, text='Mở tệp tin', command= OpenFile)
nutTepTin.grid(column=1, row=4)

#space
space1 = Label(window, text=" ", font=('Arial Bold', 10))
space1.grid(column=0,row=5)

#Row 6: Khóa,
ghiKhoa = Label(window, text='Khóa', font=('Arial',12), width=20)
ghiKhoa.grid(column=0 ,row=6)
khoa = Entry(window, width= 50,background='yellow')
khoa.grid(column=1, row=6)

#space
space1 = Label(window, text=" ", font=('Arial Bold', 10))
space1.grid(column=0,row=7)


# Xử lý
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
    txt = pad( hienThiVanBan.get("1.0", END)).encode('utf8')  #Phương thức encode() dùng để mã hóa chuỗi bằng cách sử dụng mã chỉ định. Mặc định là utf8
    key = pad( khoa.get()).encode('utf8')

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
    hienThiVanBan.delete("1.0", END)
    hienThiVanBan.insert(INSERT, entxt)

def GiaiMa_DES():
    #Lấy dữ liệu đầu vào
    EnTxt = hienThiVanBan.get("1.0", END) 
    EnTxt = base64.b64decode(EnTxt)         #Hàm b64decode() dùng để mã hóa chuỗi EnTxt từ dạng Base64 sang dạng bytes
    key = pad( khoa.get() ).encode('utf8')
    
    #Giải mã
    cipher = DES.new(key, DES.MODE_ECB)
    deTXT =  cipher.decrypt(EnTxt)  #Thực hiện giải mã
    deTXT = unpad( deTXT)

    #Ghi nhận lại giải mã
    hienThiVanBan.delete("1.0", END)
    hienThiVanBan.insert(INSERT, deTXT)

    # >>>> HIển thị

#Phần thêm nút
    #Row 8:  nút mã hóa và nút giải mã
NutMaHoa = Button(window, text='Mẫ hóa', command=MaHoa_DES)
NutMaHoa.grid(column=0, row=8)

NutGiaiMa = Button(window, text='Giải mã', command=GiaiMa_DES)
NutGiaiMa.grid(column=1, row=8)

#Phần hiển thị ra màn hình
window.mainloop()