import math

HATA = 0.002

def F(x):
    return math.sin(x) + math.cos(x) - x

def main():
    a = float(input("a değerini giriniz: "))
    b = float(input("b değerini giriniz: "))
    
    if F(a) * F(b) >= 0:
        print(f"{a:.4f} ve {b:.4f} arasında kök yoktur...")
        return
    
    x0 = (a + b) / 2
    i = 0
    
    while True:
        i += 1
        print(f"{i}. adımda yaklaşık kök= {x0:.4f}\t yeni aralık= [{a:.4f}, {b:.4f}]")
        x1 = x0
        
        if F(x0) * F(a) < 0:
            b = x0
        else:
            a = x0
        
        x0 = (a + b) / 2
        
        if abs(x0 - x1) <= HATA:
            break
    
    print(f"{i+1}. adımda döngüden çıkıldı. {i+1}. adımdaki yaklaşık kök= {x0:.4f}")
    print(f"{HATA:.3f} hata ile yaklaşık kök = {x0:.4f}")
    print(f"f({x0:.4f}) = {F(x0):.3f}")

if __name__ == "__main__":
    main()
