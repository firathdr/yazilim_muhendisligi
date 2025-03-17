import math

#bir fonksiyonun belirli bir aralıktaki kökünü bulmak için kullanılan bir yarı yarıya bölme yöntemidir.

xa=1 #birinci nokta
xb=200  # ikinci nokta
dx=.0001   # hata payı 
iterasyon=1 #adım sayısı

def f1(x):
    #return 2 * (x - 1) * (x - 2) * (x - 3) + ((x - 1) ** 2) * (2 * x - 5)
    return x**3 - x - 2  #fonksiyonumuz

while f1(xa)*f1(xb)<0:
    iterasyon+=1
    xk=xa+(xb-xa)/2.0
    if (abs(f1(xk))==0 or abs(xb-xa)<dx):
        print(xa,xb,xk)
        break
    else:
        if f1(xk)*f1(xa)>0:
            xa=xk
        else:
            xb=xk
    print(f"{iterasyon}. Adım Güncel aralık: [{xa}, {xb}], xk: {xk}")



          
