# Ho va ten sinh vien: Pham Gia Bao
# Ma so sinh vien:  B2016947
# STT:  8


def Char2Num(c):
    #Hamf ord() tra ve so nguyen cho ma Unicode theo ky tu
    return ord(c) - 65

def Num2char(c):
    #Ham chr() dung de tra ve 1 ky tu dua tren so nguyen
    return chr(c + 65)

print(Num2char(65))

'''
    - Ham nay dung de ma hoa chuoi dau vao voi cac tham so nhu sau:
        + txt: Van ban dau vao
        + a
        + b
        + m: mod
'''
def encrypAF(txt,a,b,m):
    r=""
    #Vong lap nay dung de lay tung ky tu
    for c in txt:
        e = (a * Char2Num(c)+b)%m   #Ma tung ky tu sang so nguyen
        #print(" - so dau:{0} so e: {1} + Chu: {2} ".format(Char2Num(c),e,Num2char(e)))
        r = r+Num2char(e)           #Ghi nhan lai ket qua ma hoa cua tung ky tu
    return r
print(encrypAF("HELLO",3,5,26))
