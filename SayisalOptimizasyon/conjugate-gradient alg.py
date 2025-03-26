import numpy as np
import math
import matplotlib.pyplot as plt

def f(x):
    f=3+(x[0]-1.5*x[1])**2+(x[1]-2)**2
    return f
def gradf(x):
    gradf=np.array([2*(x[0]-1.5*x[1]),-3*(x[0]-1.5*x[1])+2*(x[1]-2)])
    return gradf

def gsmain(f,xk,pk):
    xalt=0
    xust=1
    dx=0.000001
    alpha=(1+math.sqrt(5))/2
    tau=1-1/alpha
    epsilon=dx/(xust-xalt)
    N=round(-2.078*math.log(epsilon))
    k=0
    x1 = xalt + tau * (xust - xalt); 
    f1 = f(x1*pk+xk);
    x2 = xust - tau * (xust - xalt); 
    f2 = f(x2*pk+xk);
    
    for k in range(0, N):
        if f1 > f2:
            xalt = 1*x1; 
            x1 =1* x2; 
            f1 = 1*f2;
            x2 = xust - tau * (xust - xalt);  
            f2 = f(x2*pk+xk);
        else:
            xust = 1*x2; 
            x2 =1* x1; 
            f2 = 1*f1;
            x1 = xalt + tau * (xust - xalt); 
            f1 = f(x1*pk+xk);
    return x

#------adım1----
x=np.array([-5.4,1.7])
x1=[x[0]]
x2=[x[1]]
nMax=10000
eps1=1e-10
eps2=1e-10
eps3=1e-10
k=0
#---------------
updatedx=np.array([1e10,1e10])
C1=nMax<k
C2=abs(f(updatedx)-f(x))<eps1
C3=np.linalg.norm(updatedx-x)<eps2
C4=np.linalg.norm(gradf(updatedx))<eps3
previousGrad=1
previousP=1
#------adım2----
while not(C1 or C2 or C3 or C4):
    k+=1
    if k==1:
        pk=-gradf(x)
    else:
        beta=np.dot(gradf(x),gradf(x))/np.dot(previousGrad,previousGrad)
        pk=-gradf(x)+beta*previousP
    previousGrad=1*gradf(x)
    previousP=1*pk
    sk=gsmain(f, x, pk)
    x=x+sk*pk
    print("iterasyon:",k,"  x1:",round(x[0],5),"  x2:",round(x[1],5),"  f:",round(f(x),5),"  gradf:",gradf(x))
    C1=nMax<k
    C2=abs(f(updatedx)-f(x))<eps1
    C3=np.linalg.norm(updatedx-x)<eps2
    C4=np.linalg.norm(gradf(updatedx))<eps3
    updatedx=1*x
    x1.append(x[0])
    x2.append(x[1])
#---------------
plt.plot(x1,x2)
plt.scatter(x1,x2)
plt.show()
