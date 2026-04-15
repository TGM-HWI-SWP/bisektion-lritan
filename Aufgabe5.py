import matplotlib as mpl
import math

n = float(input("Gebe n an: "))

def solver(func_str: str, n_val: float, a: float, b: float, tol: float = 1e-7) -> float:
    """Findet eine Nullstelle mittels Bisektion.
    
    :param func_str: Die Funktion als String, z.B. "x**2 - n"
    :param n_val: Der Wert für n, der in der Formel genutzt wird
    :param a: Untere Intervallgrenze
    :param b: Obere Intervallgrenze
    :param tol: Toleranz (Abbruchkriterium) - Genauigkeit =1e-6 numerische Nullstelle um so nah wie möglich ans das Ergebniss zu kommen 
    """
    
    def f(x_wert):
        return eval(func_str, {"x": x_wert, "n": n_val, "math": math})
    
    #Initialisierung a und b
    a = 0
    b = 0.2 * n

    # f(x) = x^2 - n
    fa = f(a)
    fb = f(b)
    
    if fa * fb >= 0: # falls 0.2 *n nicht für b reicht
        print("Fehler: Das gewählte Intervall [a, b] schließt die Nullstelle nicht ein!")
        b = n + 1

    while (b-a) > tol: # Während a oder b 
        m= (a+b)/2
        fm=m**2 - n
        
        if fa*fm < 0:
            b = m  
            continue
        else:
            a = m
            continue

    print(f"Die Nullstelle ist {a}|{b} ") 
    
if __name__ == "__main__":
    
    solver()