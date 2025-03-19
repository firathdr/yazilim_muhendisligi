import math
import numpy as np

def f(x):
    f=(x[0]-1.5)**2 + (x[1]-2.5)**2
    return f

def gradf(x):
    gradf=[2*(x[0]-1.5),2*(x[1]-2.5)]
    
    return gradf
def hessianf(x):
    H=np.array([[2,0],[0,2]])
    return H

x=[4,3]
i=0
print("i: ",i,"f(x):", f(x))
loop=True

while loop:
    i+=1
    x=x-.01*np.array(gradf(x))
    normGradf=np.linalg.norm(gradf(x))
    print("i:",i,"f(x):",f(x),"gradf(x):",normGradf)
    if normGradf<1e-8:
        loop=False
print("x=",x)

    
H=hessianf(x)
ozdeger,ozvektor=np.linalg.eig(H)

if min(ozdeger)>0:
    print("x noktası minimum")
elif max(ozdeger)<0:
    print("x noktası maksimum")
else:
    print("x noktası semer")