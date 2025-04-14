import numpy as np

def bfgs(
    f, grad_f, x0, N_max,
    epsilon1=1e-6, epsilon2=1e-6, epsilon3=1e-6,
    line_search=lambda f, xk, pk: 0.1
):
    xk = x0.copy()
    n = len(xk)
    Hk = np.eye(n)  # Başlangıçta birim matris
    k = 0

    grad_fk = grad_f(xk)

    while True:
        pk = -Hk @ grad_fk  # Arama yönü
        sk = line_search(f, xk, pk)
        xk_next = xk + sk * pk
        grad_fk_next = grad_f(xk_next)

        # Sonlandırma kriterleri
        delta_f = abs(f(xk_next) - f(xk))
        delta_x = np.linalg.norm(xk_next - xk)
        norm_grad = np.linalg.norm(grad_fk_next)

        print(f"Iter {k}: x = {xk}, f(x) = {f(xk):.6f}, ||grad|| = {norm_grad:.6f}")

        if k >= N_max:
            print("C1: Maksimum iterasyon sayısına ulaşıldı.")
            break
        if delta_f < epsilon1:
            print("C2: Fonksiyon değişimi küçük.")
            break
        if delta_x < epsilon2:
            print("C3: Adım değişimi küçük.")
            break
        if norm_grad < epsilon3:
            print("C4: Gradyan normu küçük.")
            break

        # Güncellemeler
        s = xk_next - xk
        y = grad_fk_next - grad_fk
        rho = 1.0 / (y @ s)

        # Hk güncelleme (BFGS formülü)
        I = np.eye(n)
        Hk = (I - rho * np.outer(s, y)) @ Hk @ (I - rho * np.outer(y, s)) + rho * np.outer(s, s)

        # İleri taşı
        xk = xk_next
        grad_fk = grad_fk_next
        k += 1

    return xk, f(xk)

# Örnek fonksiyon: f(x) = x^2 + 2x + 1 → minimum x = -1
def f(x): return x[0]**2 + 2*x[0] + 1
def grad_f(x): return np.array([2*x[0] + 2])

# Sabit adım boyu
def line_search(f, xk, pk):
    return 0.1

# Başlangıç noktası
x0 = np.array([0.0])

# Çalıştır
min_x, min_val = bfgs(f, grad_f, x0, N_max=100, epsilon1=1e-8, epsilon2=1e-8, epsilon3=1e-8, line_search=line_search)
print(f"\nMinimum nokta: {min_x}, f(x) = {min_val}")
