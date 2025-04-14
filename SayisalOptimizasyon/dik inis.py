import numpy as np

def gradient_descent(
    f, grad_f, x0, N_max, epsilon1=1e-6, epsilon2=1e-6, epsilon3=1e-6,
    line_search=lambda f, xk, pk: 0.01

):
    """
    f         : Amaç fonksiyonu
    grad_f    : Gradyan fonksiyonu
    x0        : Başlangıç noktası (numpy array)
    N_max     : Maksimum iterasyon sayısı
    epsilon1  : |f(x_k+1) - f(x_k)| < epsilon1
    epsilon2  : ||x_k+1 - x_k|| < epsilon2
    epsilon3  : ||grad_f(x_k+1)|| < epsilon3
    line_search: Adım boyu seçimi için fonksiyon (isteğe bağlı)
    """
    xk = x0.copy()
    k = 0

    while True:
        grad_fk = grad_f(xk)
        pk = -grad_fk

        sk = line_search(f, xk, pk)  # Adım boyunu bul
        xk_next = xk + sk * pk

        # Sonlandırma kriterleri
        delta_f = abs(f(xk_next) - f(xk))
        delta_x = np.linalg.norm(xk_next - xk)
        norm_grad = np.linalg.norm(grad_f(xk_next))

        print(f"Iter {k}: x = {xk}, f(x) = {f(xk)}, ||grad|| = {norm_grad}")

        if k >= N_max:
            print("C1: Maksimum iterasyon sayısına ulaşıldı.")
            break
        if delta_f < epsilon1:
            print("C2: Fonksiyon değişimi küçük, algoritma durdu.")
            break
        if delta_x < epsilon2:
            print("C3: Adım değişimi küçük, algoritma durdu.")
            break
        if norm_grad < epsilon3:
            print("C4: Gradyan normu küçük, algoritma durdu.")
            break

        xk = xk_next
        k += 1

    return xk, f(xk)

# Örnek: f(x) = x^2 + 2x + 1 → minimum x = -1
def f(x): return (x[0]**2 + 2*x[0] + 1)
def grad_f(x): return np.array([2*x[0] + 2])

# Line search sabit adım: 0.1
def constant_line_search(f, xk, pk):
    return 0.1

# Kullanım:
x0 = np.array([0.0])
solution, fval = gradient_descent(f, grad_f, x0, N_max=100, epsilon1=1e-8, epsilon2=1e-8, epsilon3=1e-8, line_search=constant_line_search)

print(f"\nMinimum nokta: {solution}, f(x) = {fval}")
