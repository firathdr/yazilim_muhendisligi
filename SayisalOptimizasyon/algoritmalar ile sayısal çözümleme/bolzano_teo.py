import math

def F(x):
    return (1.0 / 3) * (x ** 3) - (5.0 / 2) * (x ** 2) + 6 * x + 10

def main():
    a = float(input("a değerini giriniz: "))
    b = float(input("b değerini giriniz: "))
    h = 0.5
    s = 0
    
    i = a
    while i <= b:
        if F(i) == 0:
            print(f"{i:.5f} değeri fonksiyonun gerçek köküdür.")
            s += 1
        elif F(i) * F(i + h) < 0:
            print(f"Bolzano teoreminden {i:.5f} ile {i + h:.5f} arasında en az bir kök vardır...")
            s += 1
        i += h
    
    if s != 0:
        print(f"{a:.5f} ile {b:.5f} arasında en az {s} tane kök vardır...")
    else:
        print(f"{a:.5f} ile {b:.5f} arasında kök yoktur...")

if __name__ == "__main__":
    main()
