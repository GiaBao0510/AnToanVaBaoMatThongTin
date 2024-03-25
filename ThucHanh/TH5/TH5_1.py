# Ho va ten sinh vien: Pham Gia Bao
# Ma so sinh vien:  B2016947
# STT:  8

#0: Thêm thư viện
from tkinter import *
import tkinter as tk
from Crypto.Cipher import DES
import base64
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5
from tkinter import filedialog

#Mã hoá DES
class MAHOA_DES(tk.Toplevel):
    def __init__(self, parent):
        self.parent = parent
        Toplevel.__init__(self)
        self.title("Chương trình mã hóa đối xứng")
        self.geometry('800x400')
        
        #Row0
        self.lb1 = Label(self, text="Chương trình DEMO", font=('Arial Bold',20))
        self.lb1.grid(column=1, row=0)

        #Row1
        self.lb2 = Label(self, text="MẬT MÃ ĐỐI XỨNG DES", font=('Arial bold',20))
        self.lb2.grid(column=1, row=1)

        #row2: Bản gõ
        self.lb3 = Label(self, font=('Arial',18), text="Văn bản gốc")
        self.lb3.grid(row=2, column=0)
        self.bango = Text(self, wrap='word', width=30, height=1)
        self.bango.grid(row=2, column=1)

        #row3: Khóa
        self.lb4 = Label(self, font=('Arial',18), text="Khóa")
        self.lb4.grid(row=3, column=0)
        self.khoa = Text(self, wrap='word', width=30, height=1)
        self.khoa.grid(row=3, column=1)

        #row4: Bản mã
        self.lb5 = Label(self, font=('Arial',18), text="Văn bản được mã hóa")
        self.lb5.grid(row=4, column=0)
        self.bamma = Text(self, wrap='word', width=30, height=1)
        self.bamma.grid(row=4, column=1)

        #row5: Giải mã
        self.lb6 = Label(self, font=('Arial',18), text="Văn bản được giải mã")
        self.lb6.grid(row=5, column=0)
        self.giaima = Text(self, wrap='word', width=30, height=1)
        self.giaima.grid(row=5, column=1)

        #--------- hàm
        def pad(s):
            #Them vao cuoi so con thieu cho du boi cua 8
            return s + (8 - len(s) %8) * chr(8 - len(s) % 8)

        def unpad(s):
            return s[:-ord(s [len(s)-1:])]

        #hàm mã hóa
        def ThucHienMaHoa(self):
            txt = pad(self.bango.get('1.0',END) ).encode()
            key = pad(self.khoa.get('1.0',END)).encode()
            cipher = DES.new(key, DES.MODE_ECB)
            entxt = cipher.encrypt(txt)
            entxt = base64.b64encode(entxt)
            self.bamma.delete('1.0',END)
            self.bamma.insert(INSERT, entxt)
        
        #hàm giải mã
        def ThucHienGiaima(self):
            txt = self.bamma.get('1.0',END)
            txt = base64.b64decode(txt)
            key = pad(self.khoa.get('1.0',END)).encode()
            cipher = DES.new(key, DES.MODE_ECB)
            detxt = unpad(cipher.decrypt(txt))
            self.giaima.delete('1.0',END)
            self.giaima.insert(INSERT, detxt)

        #----------------
            #row6
        self.NutMaHoa = Button(self, text='Mã hóa', command=self.ThucHienMaHoa)
        self.NutMaHoa.grid(row=6, column=1) 
            #row7
        self.NutGiaiMa = Button(self, text='Giải mã', command=self.ThucHienGiaima)
        self.NutGiaiMa.grid(row=7, column=1) 
            #row8
        self.NutHome = Button(self, text='Quay về màn hình chính', command=self.destroy)
        self.NutHome.grid(row=8, column=1)
        

#Mã hóa Affine
class MAHOA_Affine(tk.Toplevel):
    def __init__(self, parent):
        self.parent = parent
        Toplevel.__init__(self)
        self.title("Chương trình mã hóa Affine")
        self.geometry('800x600')

        #---- Row0
        self.lb0 = Label(self, text=" ", font=("Arial Bold", 10))
        self.lb0.grid(column=0, row=0)

        #---- Row1
        self.lb1 = Label(self, text="CHƯƠNG TRINH DEMO", font=("Arial Bold", 20))
        self.lb1.grid(column=1, row=1)

        #---- Row2
        self.lb2 = Label(self, text="MẬT MÃ AFINE", font=("Arial Bold",15))
        self.lb2.grid(column=0,row=2)

        #---- Row3
        self.plainlb3 = Label(self, text="PLAIN TEXT", font=("Arial",14) )
        self.plainlb3.grid(column=0, row=3)
        self.plaintxt = Entry(self, width=20)
        self.plaintxt.grid(column=1, row=3)
        self.KEYlb4 = Label(self, text="KEY PAIR", font=("Arial",14) )
        self.KEYlb4.grid(column=2, row=3)
        self.KEYA1 = Entry(self, width=3)
        self.KEYA1.grid(column=3, row= 3)
        self.KEYB1 = Entry(self, width=5)
        self.KEYB1.grid(column=4, row= 3)
        self.ENCRYTIONbuttom = Button(self, text="Mã hóa")
        self.ENCRYTIONbuttom.grid(column=5, row= 3)

        #---- Row4
        self.cipherlb4 = Label(self, text="CIPHER TEXT", font=("Arial",14) )
        self.cipherlb4.grid(column=0, row=4)
        self.ciphertxt = Entry(self, width=20)
        self.ciphertxt.grid(column=1, row=4)
        self.DENCRYTIONbuttom = Button(self, text="Giải mã")
        self.DENCRYTIONbuttom.grid(column=3, row= 4)
        self.DENCRYTIONtxt = Entry(self, width=15)
        self.DENCRYTIONtxt.grid(column=4, row= 4)



        ''' ---- Bước 2: Cài đặt các sự kiện click ----'''

        #2.Cai dat cac ham can thiet

            #>>>> Ky tu ghi hoa
        def Char2Num(c):
            if c.isupper():
                return ord(c) - 65
            elif c.islower():
                return ord(c) - 97 + 10
            else:
                return -1

        def Num2char(c):
            #Ham chr() dung de tra ve 1 ky tu dua tren so nguyen
            if 0 <= c <= 25:
                return chr(c + 65)
            elif 25 < c < 52:
                return(c+97 - 10)
            else:
                return ""

        def encrypAF(txt,a,b,m):
            r=""
            #Vong lap nay dung de lay tung ky tu
            for c in txt:
                #Kiem tra chu cai
                if c.isalpha():
                    e = (a * Char2Num(c)+b)%m   #Ma tung ky tu sang so nguyen
                    r += Num2char(e) 
                else:
                    r += c
            return r

        #danh cho nut ma hoa
        def mahoa():
            a = int(self.KEYA1.get())
            b = int(self.KEYB1.get())
            m = 26
            entxt = encrypAF( self.plaintxt.get() ,a,b,m)

            #hien thi
            self.ciphertxt.delete(0, END)            #Lam rong
            self.ciphertxt.insert(INSERT, entxt)     #Them van ban da ma hoa

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
            for c in txt:
                if c.isalpha():
                    D =  (a1 * (Char2Num(c) - b))%m
                    vb = vb + Num2char(D)
                else:
                    vb += c
            return vb

        #Danh cho nut giai ma
        def giaima():
            a = int(self.KEYA1.get())
            b = int(self.KEYB1.get())
            m =26

            VBmahoa = str(self.ciphertxt.get())
            detxt = decryptAF(VBmahoa, a, b, m)

            #hien thi
            self.DENCRYTIONtxt.delete(0, END)
            self.DENCRYTIONtxt.insert(INSERT, detxt)

        #1. Them su kien ma hoa
        self.ENCRYTIONbuttom = Button(self, text="Mã hóa", command=mahoa)          #Da them su kien ma hoa
        self.ENCRYTIONbuttom.grid(column=5, row= 3)

        self.DENCRYTIONbuttom = Button(self, text="Giải mã", command=giaima)                        #Da them su kien giai ma
        self.DENCRYTIONbuttom.grid(column=3, row= 4)

#Mã hóa RSA
class MAHOA_RSA(tk.Toplevel):
    def __init__(self, parent):
        self.parent = parent
        Toplevel.__init__(self)
        self.title("Chương trình mã hóa RSA")
        self.geometry('800x600')
            #Row 0
        self.sp0 = Label(self, text='Chương Trình Demo', font=('Arial Bold',20))
        self.sp0.grid(row=0,column=1)

        #Row 1
        self.sp1 = Label(self, text='Mật mã bất đối xứng RSA', font=('Arial Bold',18))
        self.sp1.grid(row=1,column=1)

        #Row 2: Văn bản gốc
        self.sp2 = Label(self, text='Văn bản gốc', font=('Arial',12))
        self.sp2.grid(row=2, column=0)
        self.vanbangoc =  Text(self, wrap='word', width=50, height=1)
        self.vanbangoc.grid(row=2, column=1)

        #Row 3: Văn bản mã hóa
        self.sp3 = Label(self, text='Văn bản mã hóa', font=('Arial',12))
        self.sp3.grid(row=3, column=0)
        self.vanmahoa = Text(self, wrap='word', width=50, height=1)
        self.vanmahoa.grid(row=3, column=1)

        #Row 4: Văn bản giải mã
        self.sp4 = Label(self, text='Văn bản giải mã ', font=('Arial',12))
        self.sp4.grid(row=4, column=0)
        self.vangiaima =  Text(self, wrap='word', width=50, height=1)
        self.vangiaima.grid(row=4, column=1)

        #Row 5: Khóa cá nhân
        self.sp5 = Label(self, text='Khóa cá nhân ', font=('Arial',12))
        self.sp5.grid(row=5, column=0)
        self.khoacanhan =  Text(self, wrap='word', width=50, height=10)
        self.khoacanhan.grid(row=5, column=1)

        #Row 6: Khóa công khai
        self.sp6 = Label(self, text='Khóa cá nhân ', font=('Arial',12))
        self.sp6.grid(row=6, column=0)
        self.khoacongkhai =  Text(self, wrap='word', width=50, height=10)
        self.khoacongkhai.grid(row=6, column=1)

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
            self.khoacanhan.delete('1.0', END)
            self.khoacanhan.insert(END, key.exportKey('PEM'))
            self.khoacongkhai.delete('1.0', END)
            self.khoacongkhai.insert(END, key.publickey().exportKey('PEM'))

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
            txt = self.vanbangoc.get('1.0',END).encode('utf8')      #Lấy nội dung từ widget vanbangoc
            pub_key = get_key("public_key")     #Lấy nội dung khóa công khai được lưu ở noi nào đó trong ổ đĩa D
            cipher = PKCS1_v1_5.new(pub_key)    #Tạo ra 1 đối tượng bị mã hóa dựa trên pub_key
            entxt = cipher.encrypt(txt)         #Thực hiện mã hóa bản gõ
            entxt = base64.b64encode(entxt)     # Mã hóa chuỗi byte "entxt" sang dạng base64
            self.vanmahoa.delete("1.0",END)
            self.vanmahoa.insert(INSERT,entxt)

        def giaima_rsa():
            #Doc van ban và mã hóa chuỗi
            cipherText = self.vanmahoa.get('1.0',END)
            cipherText = base64.b64decode(cipherText)

            #Lấy nội dung tệp tin
            privateKey = get_key("private_key")

            #Thục hiện giải mã
            cipher = PKCS1_v1_5.new(privateKey)
            bangoc = cipher.decrypt(cipherText, sentinel=None)

            #Ghi nhan
            self.vangiaima.delete("1.0",END)
            self.vangiaima.insert(INSERT, bangoc)


        # ----------------------------------------

        #Row 7: tạo khóa
        self.taokhoa  =  Button(self, text='Tạo khóa', command= generate_key)
        self.taokhoa.grid(row=7, column=1)

        #Row 8: mã hóa
        self.mahoa  =  Button(self, text='Mã khóa', command= mahoa_rsa)
        self.mahoa.grid(row=8, column=1)

        #Row 9: giải mã
        self.giaima  =  Button(self, text='Giải mã', command=giaima_rsa)
        self.giaima.grid(row=9, column=1)

#-------------- Home
class MainWindow(tk.Frame):
   
    def __init__(self, parent):
        self.parent = parent
        tk.Frame.__init__(self)

        #Mã hóa des
        self.mahoaDES = Button(text='Mã hóa DES', font=('Times New Roman',11), command=self.des)
        self.mahoaDES.pack()

        #mã hóa Affine
        self.mahoaAffine = Button(text="Mã hóa Affine",font=('Times New Roman',11), command=self.affine )
        self.mahoaAffine.pack()

        #mã hóa rsa
        self.mahoaRSA = Button(text="Mã hóa RSA",font=('Times New Roman',11), command=self.rsa )
        self.mahoaRSA.pack()

        self.thoat = Button(text="Kết thúc", font=('Times New Roman',11), command=quit)
        self.thoat.pack()

    def des(self):
        MAHOA_DES(self)
    
    def affine(self):
        MAHOA_Affine(self)
    
    def rsa(self):
        MAHOA_RSA(self)

#Hàm chay chương trình
def main():
    window = tk.Tk()
    window.title("Chương trình chính")
    window.geometry('300x200')
    MainWindow(window)
    window.mainloop()
main()

