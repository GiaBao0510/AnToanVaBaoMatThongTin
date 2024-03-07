import csv

listCountry = []    #Danh sách các nước
lenlist = []

with open("TH2/data/country.csv", "r") as fileCSV:
    reader = csv.reader(fileCSV, delimiter=',')
    for i in reader:
        #Chỉ lưu tên các nước có độ dài là 8
        if len(i[1].replace(" ","")) <= 7: 
            listCountry.append( i[1].replace(" ",""))   #lưu các tên nước vào danh sách
            lenlist.append( len(i[1].replace(" ","")))
        
#1. Mật mã cần bẻ
cipher = ["lIZg7tB/NvuG4MXsCDFUsRjvQrjw/UuUGzZw+QMMDF4nGjQCGzY0Uw==","LsmDvf9t1pLPn+NZ99+cVx+V1ROl2/9KNqk9PLTe5uRii/aNc/X3tw==", "5cdbWs00vXghkBLECplG8ClNQ2Da5R/9KZ0bAKRs+bPvhwOwIt7Sh2ZZFtxHBAK9"]

plainText = "The treasure is under the coconut tree"    #Bản rõ

# 2. Quy trình bẻ khóa
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

def GiaiMa_DES(k, Estring):
    #Lấy dữ liệu đầu vào
    EnTxt = base64.b64decode(Estring)         #Hàm b64decode() dùng để mã hóa chuỗi EnTxt từ dạng Base64 sang dạng bytes
    key = pad( k ).encode('utf8')
    
    #Giải mã
    cipher = DES.new(key, DES.MODE_ECB)
    deTXT =  cipher.decrypt(EnTxt)  #Thực hiện giải mã
    deTXT = unpad( deTXT)
    return deTXT

#1. Thực hiện kiếm khóa của văn bản mã hóa thứ 1
findKey = '' 
for k in listCountry:
    if GiaiMa_DES(k, cipher[0]) == plainText.encode('utf8'):
        findKey = k
        print('- Key: ',k)
        break

#2. Thực hiện tìm kiếm khóa 
for e in cipher:
    giaiMa = GiaiMa_DES(findKey, e).decode('utf8')
    print(giaiMa)