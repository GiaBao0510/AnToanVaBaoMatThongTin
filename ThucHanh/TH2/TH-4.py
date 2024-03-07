import numpy as np

    # >>> Khởi tạo
arr = np.zeros((8,8),dtype=int) #Khởi tạo mảng 2 chiều

#Đọc bản gõ từ tệp tin
f = open('TH2/data/plaintext.txt','r')
list_content = f.readlines()
f.close()           #đóng tệp tin

#Cắt chuyển mảng 1 chiều sang thành mảng 2 chiều dựa trên dấu cách
for i in range(0,len(list_content)):
    list_content[i] = list_content[i].split(' ')

#Xóa ký tự xuống dòng nếu có
for i in range(0,len(list_content)):
    for j in range(0 ,len(list_content[0])):
        list_content[i][j] = list_content[i][j].replace('\n','')

#Lưu từng ký tự trong danh sách vào trong mảng arr
for i in range(0,len(list_content)):
    for j in range(0 ,len(list_content[0])):
        arr[i][j] = int(list_content[i][j])
#print(arr)

    #1. hàm Thực hiện hoán vị Mã hóa
def Encrypt_IP( mang):
    temp = np.zeros((8,8), dtype=int)
    chan = 0    #Lọc từng cột chẳn
    le = 1      #Lọc từng cột lẻ

    #Lọc cột lẻ trước
    for i in range(0,4):
        cot = mang[:,le]    #Lấy cột
        cot = cot[::-1]     #Đảo chiều mảng
        for j in range(len(cot)):
            temp[i,j] = cot[j]

        #Tăng giá trị
        le +=2
    
    #Lọc cột chẳn trước
    for i in range(4,8):
        cot = mang[:,chan]    #Lấy cột
        cot = cot[::-1]     #Đảo chiều mảng
        for j in range(len(cot)):
            temp[i,j] = cot[j]

        #Tăng giá trị
        chan +=2

    return temp    

    #2. Hàm thực hiện Giải mã
def Dencrypt_IP( mang): 
    temp = np.zeros((8,8), dtype=int)
    chan = 0
    le = 1

    #Gán cột lẻ trước
    for i in range(0,4):
        hang = mang[i ,:]
        hang = hang[::-1]
        for j in range( len(hang)):
            temp[j,le] = hang[j]
        le += 2
    
    #Gán cột chan trước
    for i in range(4,8):
        hang = mang[i ,:]
        hang = hang[::-1]
        for j in range( len(hang)):
            temp[j,chan] = hang[j]
        chan += 2
    
    return temp
print(Dencrypt_IP(arr))