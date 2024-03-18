import numpy as np
    #Chuẩn bị
BangChuCai = [
    'A','B','C','D','E',
    'F','G','H','I','J','K',
    'L','M','N','O','P',
    'Q','R','S','T','U',
    'V','W','X','Y','Z'
    ]

plaintext = "SOFARSOGOODSO"
key = "NOROSEWIT"

    #1. Tạo ma trận khóa

#Kiểm tra xem ký tự có bên trong mảng 1 chiều hay không
def KiemTraKyTuTonTai(MangKhoa, kyTu):
    for i in MangKhoa:
        if kyTu == i:
            return 1
    return 0

#Tạo ma trận khóa
def MaTranKhoa(key, BangChuCai):
    MaTranKhoa = []
    DoDaiKhoa = 0
    LayBangChuCai = 0
    dem = 0

    while dem < 25:
        #Lấy từng ký tự khóa trước gán vào ma trận
        if DoDaiKhoa < len(key):
            #Nếu ký tự không tồn tại thì thực hiện bước kiêm tra tiếp theo
            if KiemTraKyTuTonTai( MaTranKhoa,key[DoDaiKhoa]) == 0:
                if key[DoDaiKhoa] == 'I' and KiemTraKyTuTonTai( MaTranKhoa,"J") == 1:
                    DoDaiKhoa+=1
                elif key[DoDaiKhoa] == 'J' and KiemTraKyTuTonTai( MaTranKhoa,"I") == 1:
                    DoDaiKhoa+=1
                else:
                    MaTranKhoa.append(key[DoDaiKhoa])
                    DoDaiKhoa+=1
                    dem+=1
            else:
                DoDaiKhoa+=1
        else:   #Nếu duyệt xong khóa rồi thì đến bảng chữa cái
            #Nếu ký tự không tồn tại thì thực hiện bước kiêm tra tiếp theo
            if KiemTraKyTuTonTai( MaTranKhoa,BangChuCai[LayBangChuCai]) == 0:
                if BangChuCai[LayBangChuCai] == 'I' and KiemTraKyTuTonTai( MaTranKhoa,"J") == 1:
                    LayBangChuCai+=1
                elif BangChuCai[LayBangChuCai] == 'J' and KiemTraKyTuTonTai( MaTranKhoa,"I") == 1:
                    LayBangChuCai+=1
                else:
                    MaTranKhoa.append(BangChuCai[LayBangChuCai])
                    LayBangChuCai+=1
                    dem+=1
            else:
                LayBangChuCai+=1 
    return MaTranKhoa

Matrankhoa1Chieu = np.array(MaTranKhoa(key, BangChuCai))
Matrankhoa2Chieu = Matrankhoa1Chieu.reshape(5,5)        #Chuyển mảng 1 chiều thành 2 chiều

    #2.Hàm Tách plaintext, lần lượt tách 2 ký tự
def TachCap(plainText):
    ds = []
    dem = 0
    du = 0
    thua = 0

    #Lặp
    while True:
        #ĐK 1: Kiểm tra xem đã đến cuối bản rõ mà vẫn đử(Tức là không có dư 1 chữ cái nào)
        try:
            plainText[dem]
        except:
            du = 1
        #ĐK 1
        if du == 1:
            break
        else:
            #ĐK 2: Kiểm tra xem đã đến cuối bản rõ mà còn dư(Tức là còn có dư 1 chữ cái nào)
            try:
                plainText[dem+1]
            except:
                thua = 1
            #DK 2:
            if thua == 1:
                ds.append(plainText[dem])
                ds.append("Q")
                break
            else:
                if plainText[dem] != plainText[dem+1]:
                    ds.append(plainText[dem])
                    ds.append(plainText[dem+1])
                    dem+=2
                else:
                    ds.append(plainText[dem])
                    ds.append("X")
                    dem+=1
    return ds

DStachCap = TachCap(plaintext)

    #3. Mã hóa
#Hàm tìm vị trí hàng cột dựa trên ký tự trong tìm trong ma trận khóa
def TimViTri(MTK2Chieu, MTK1chieu,c):
    cot =0
    hang = 0
    for i in range(0,5):
        for j in range(0,5):
            if MTK2Chieu[i][j] == c:
                return [i, j]
            elif c == "I" and KiemTraKyTuTonTai(MTK1chieu,"J") and MTK2Chieu[i][j] == "J":
                return [i, j]
            elif c == "J" and KiemTraKyTuTonTai(MTK1chieu,"I") and MTK2Chieu[i][j] == "I":
                return [i, j]
            
#Hàm mã hóa
def MaHoa(MaTran2Chieu, MaTran1Chieu, DSTachCap):
    chan=0
    le=1
    ds = []     #Lưu các cặp đã hoán đổi
    c = ''      #Lưu đoạn mã hóa
    #Lặp
    while le < len(DSTachCap):
        #Lấy 2 ký tự để thự hiện mã hóa
        dau = DSTachCap[chan]
        duoi = DSTachCap[le]

        #Lấy vị trsi 2 ký tự trên trong ma trận khóa vừa tạo
        x1,y1 = TimViTri(MaTran2Chieu,MaTran1Chieu,dau)
        x2,y2 = TimViTri(MaTran2Chieu,MaTran1Chieu,duoi)

        #Nếu cùng hàng thì dịch chuyển mỗi ký tự hàng lên đằng trước
        if x1 == x2 and y1 != y2:
            try:    #Ký tự đầu
                ds.append(MaTran2Chieu[x1][y1 + 1])
            except:
                ds.append(MaTran2Chieu[x1][0])
            
            try:    #Ký tự đuôi
                ds.append(MaTran2Chieu[x2][y2 + 1])
            except:
                ds.append(MaTran2Chieu[x2][0])
        
        #Nếu cùng cột thì dịch chuyển mỗi ký tự cột lên đằng trước
        elif y1 == y2 and x1 != x2:
            try:    #Ký tự đầu
                ds.append(MaTran2Chieu[x1 + 1][y1])
            except:
                ds.append(MaTran2Chieu[0][y1])
            
            try:    #Ký tự đuôi
                ds.append(MaTran2Chieu[x2 + 1][y2])
            except:
                ds.append(MaTran2Chieu[0][y2])
        #Chéo thì hoán đổi cột
        else:
            ds.append(MaTran2Chieu[x1][y2])
            ds.append(MaTran2Chieu[x1][y1])

        #Dời lên lấy 2 ký tự tiếp theo
        chan+=2
        le+=2

    #Chuyển mảng thành chuỗi
    for i in ds:
        c+=i

    return c 

print( MaHoa(Matrankhoa2Chieu, Matrankhoa1Chieu, DStachCap))
