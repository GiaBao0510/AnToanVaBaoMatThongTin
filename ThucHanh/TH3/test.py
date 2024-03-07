#Uoc so chung lơn nhat
def gcd(a,b):
    if a > b:
        print('a: ',a,' ,b: ',b)
        r = a%b
        print( 'r:',r)
        
        if r == 1:
            return 1
        elif r > 0:
            return gcd(b,r)
        elif r == 0:
            return 0
    else:
        return 0

def Euclide_moRong(a,b):
    x0,x1,y0,y1 = 0,1,1,0
    
    while True:
        print('----------------')
        r = a%b
        print('r = ',r)
        if r == 0:
            break 
        q = a//b
        print('q = ',q)
        x = x1 - q*x0
        print('x = ',x)
        y = y1 - q*y0
        print('y = ',y)
        
        a,b = b,r
        x0 , x1 ,y0 ,y1 = x, x0, y, y0
    print('Ket qua')
    return y

print(Euclide_moRong(7,5))
