import matplotlib as mpl
import math

n = float(input("Gebe n an: "))

def solver(func_str: str, n_val: float, tol: float = 1e-7) -> float:
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
    b = 0.2 * n_val

    if f(a) * f(b) >= 0: # falls 0.2 *n nicht für b reicht
        print("Fehler: Das gewählte Intervall [a, b] schließt die Nullstelle nicht ein!")
        b = n_val + 1

    while abs(f(m)) > tol:
        m = (a + b) / 2
            #Vorzeichen
        if f(a) * f(m) < 0:
            b = m # Nullstelle liegt links
            x = True
        else:
            a = m  # Nullstelle liegt rechts
            x = False
        #print(f"Die Nullstelle für n={n_val} lautet: P({c:.4f} | 0)")
        if x == True:
            print(f"Die Nullstelle lautet {m}|{a}")
        else:
            print(f"Die Nullstelle lautet {b}|{m}")
    return m


        
if __name__ == "__main__":
    
    solver()