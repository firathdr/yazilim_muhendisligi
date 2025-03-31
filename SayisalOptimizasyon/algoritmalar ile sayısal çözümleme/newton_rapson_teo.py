import math

HATA = 0.00001

def F(x):
    return math.exp(x) - 3 * x

def FT(x):
    return math.exp(x) - 3

def main():
    x0 = 0.0
    i = 0
    print(f"Yönteme başladığımız nokta= {x0:.6f}")
    
    while True:
        x = x0
        x0 = x - F(x) / FT(x)
        i += 1
        print(f"{i}. adımda yaklaşık değer= {x0:.6f}")
        
        if abs(x0 - x) <= HATA:
            break
    
    print(f"yaklaşık kök = {x0:.6f}")
    print(f"f({x0:.6f}) = {F(x0):.6f}")

if __name__ == "__main__":
    main()
