x=10.5
f=((x-1)**2)*(x-2)*(x-3)                                  #(ЁЭСетИТ1)2(ЁЭСетИТ2)(ЁЭСетИТ3)
f1=2*(x-1)*(x-2)*(x-3)+((x-1)**2)*(2*x-5) #                     1.t├╝rev
f2=2*(x-2)*(x-3)+2*(x-1)*(2*x-5)+2*(x-1)*(2*x-5)+4*(x-1)**2#    2.t├╝rev
dx= -f1/f2  
iteration=0
def yuvarla(x):
    x=round(x,3)
    return x
print("iteration ",iteration," x: ",yuvarla(x)," f: ",yuvarla(f)," f1: ",yuvarla(f1), " f2: ",yuvarla(f2))
while abs(f1)>1e-10:
    iteration+=1
    x=x+dx
    f=((x-1)**2)*(x-2)*(x-3)     #(ЁЭСетИТ1)2(ЁЭСетИТ2)(ЁЭСетИТ3) #f degeri sadece g├╢stermek i├зin kullan─▒yoz i┼Яleme kat─▒lm─▒yor
    f1=2*(x-1)*(x-2)*(x-3)+((x-1)**2)*(2*x-5)
    f2=2*(x-2)*(x-3)+2*(x-1)*(2*x-5)+2*(x-1)*(2*x-5)+4*(x-1)**2 
    dx= -f1/f2 # f1 in i┼Яaretine g├╢re k├╢k├╝n sa─Я m─▒ sol mu olduguna karar verip oraya yakla┼Яmaya ├зal─▒┼Я─▒yoruz
    print("iteration ",iteration," x: ",yuvarla(x)," f: ",yuvarla(f)," f1: ",yuvarla(f1), " f2: ",yuvarla(f2))

    
    