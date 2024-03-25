import numpy as np

#bảng chữ cái
aphabet = np.array([
    'A','B','C','D','E',
    'F','G','H','I','J','K',
    'L','M','N','O','P',
    'Q','R','S','T','U',
    'V','W','X','Y','Z'
])

#Khóa
key = np.array([
    [17,17,5],
    [21,18,21],
    [2,2,19]
])

#Bang rõ
plainText = "PAYMOREMONEY"

#Lấy số hàng và cột
r,c = key.shape

#Hàm tìm số thứ tự dựa trên bảng chữ cái
def TimSoThuTu(bangchucai, kytu):
    try:
        #kiêm tra số chuỗi
        if kytu.isupper() :
            for i in range(0, len(bangchucai)):
                if bangchucai[i] == kytu:
                    return i
        #ngược lại trả về -1
        else:
            return -1
    except:
        return -1

#Hàm từ số thứ tự suy ra chữa cái trong bảng chữ cái
def TimChuCai(bangchucai, STT):
    try:
        return bangchucai[STT]
    except:
        return "NULL"

#Mã hóa
def MaHoa(khoa ,bango, bangchucai):

    c = ""  #Lưu các ký tự đã bị mã hóa
    for i in range(0,len(plainText),r):
        try:
            subarrayNum = np.array([])
            dem  = 0
            #Lấy các ký tự liên tiếp dựa trên r
            while dem < r:
                #Chuyển lý tự về vị trí số của nó
                vtri = TimSoThuTu(bangchucai, bango[i+dem])
                subarrayNum = np.append(subarrayNum,vtri)
                dem+=1
            
            #Thực hiện phép nhân 2 ma trân giữa khóa và mảng con mới tạo
            Cn = (khoa@subarrayNum)%26
            
            #Chuyển các số vị trí đã mã hóa về dạng chữ
            for i in Cn:
                c+= TimChuCai(bangchucai, int(i))

        except:
            print('done')
    return c

print(MaHoa(key ,plainText, aphabet))

#Giải mã
def GiaiMa(bangChuCai, khoa, BanMa):
    #Thực hiện nghịch đảo khóa
    print(khoa)
    MaTranNghichDao = np.linalg.inv(khoa)
    print('Trước: ',MaTranNghichDao)
    MaTranNghichDao = MaTranNghichDao.astype(int)#Chuyển đổi về kiểu số nguyên
    print('Sau: ',MaTranNghichDao)
    # #Lưu trữ các ký tự được mã hóa
    # pt =""
    # for i in range(0, len(BanMa), 3):
    #     try:
    #         dem = 0
    #         while dem < r:
    #             #Lấy vị ký tự đã được mã hóa
    #             vtri = TimSoThuTu(bangChuCai, BanMa[i+dem])
    #             subarrayNum = np.append(subarrayNum, vtri)
    #             dem+=1

    #         #Thực hiện phép nhân 2 ma trận giữa ma trận nghịch đảo của khóa và mảng con vừa được thu thập trên
    #         Dn = (MaTranNghichDao@subarrayNum)%26

    #         #Chuyển các vị trí trên về dạng chữ cái
    #         for i in Dn:
    #             pt += TimChuCai(bangChuCai, int(i))
    #     except:
    #         print('done')
    # return pt

print(GiaiMa(aphabet, key , MaHoa(key ,plainText, aphabet)))                
