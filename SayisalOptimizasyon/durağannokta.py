import sympy as sp

# Sembolleri tanımla
x1, x2 = sp.symbols('x1 x2')

# Fonksiyonu tanımla
f = x1**2 -2*x1 -3*x2*x1+12*x2

# Gradienti (nabla f) hesapla
grad_f = [sp.diff(f, var) for var in (x1, x2)]
print("GRADYANT ====   ",grad_f)

# Durağan noktaları bulmak için gradyanı sıfıra eşitle
stationary_points = sp.solve(grad_f, (x1, x2))
print("Durağan Noktalar:", stationary_points)

# Hessian matrisini hesapla
H = sp.hessian(f, (x1, x2))

# Durağan noktada Hessian'ı değerlendir
H_at_stationary = H.subs({x1: stationary_points[x1], x2: stationary_points[x2]})
print("Hessian Matrisinde Durağan Noktadaki Değer:\n", H_at_stationary)

# Özdeğerleri hesapla
eigenvals = H_at_stationary.eigenvals()
print("Özdeğerler:", eigenvals)

# Noktanın tipini belirle
if all(val > 0 for val in eigenvals):
    print("Bu nokta yerel minimumdur.")
elif all(val < 0 for val in eigenvals):
    print("Bu nokta yerel maksimumdur.")
else:
    print("Bu nokta bir eyer noktasıdır.")


