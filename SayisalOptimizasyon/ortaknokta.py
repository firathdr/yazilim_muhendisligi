#import numpy as np
#import math
def f1(x):
    f1=2*(x-1)*(x-2)*(x-3)+(x-1)**2*(2*x-5)
    return f1
xa=-2
xb=+5

if f1(xa)*f1(xb)<0:
    print("seçilen noktalar doğru")
    
    while abs(xa-xb)>1e-10:
        ortaknokta=(xa+xb)/2
        if f1(ortaknokta)*f1(xa)>0:
            xa=ortaknokta
        else:
            xb=ortaknokta
        print(xa,xb,ortaknokta,abs(xa-xb))
else:
    print("doğru noktaları seç")
    

    