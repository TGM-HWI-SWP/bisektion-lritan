import math
from Aufgabe5 import solver


def solver2(func_str: str, n_val: float, tol: float = 1e-7, max_iter: int = 100) -> float:
    """
    Findet eine Nullstelle mittels Regula Falsi (Sekantenverfahren).
    
    :param func_str: Die Funktion als String.
    :param n_val: Der Wert für n.
    :param tol: Abbruchkriterium für die Genauigkeit.
    :param max_iter: Sicherheitsabbruch nach n Iterationen.
    :return: Die berechnete Nullstelle.
    """
    
    def f(x_wert:float) -> float:
        """Berechnet den Funktionswert für ein gegebenes x unter Berücksichtigung von n.
        Args:
            x_wert (float): Der aktuelle x-Wert (Stelle), der berechnet werden soll.
        Raises:
            ValueError: Wird ausgelöst, wenn die mathematische Auswertung nicht funktioniert
        Returns:
            float: Das Ergebnis der Funktion f(x).
        """
        try:
            return eval(func_str, {"x": x_wert, "n": n_val, "math": math})
        except Exception as e:
            raise ValueError(f"Fehler in der Funktionsauswertung: {e}")
    
    #Initialisierung a und b
    a:float = 0.0
    b:float = n_val + 1

    if f(a) * f(b) > 0:
            raise ValueError("Regula Falsi Fehler: f(a) und f(b) müssen unterschiedliche Vorzeichen haben.")

    c: float = a # Initialer Punkt

    for i in range(max_iter):
            # Die Regula Falsi Formel 
            # (Sekantenschnittpunkt mit der x-Achse)
            # c = b - f(b) * (b - a) / (f(b) - f(a))
            fa: float = f(a)
            fb: float = f(b)
            # Division durch Null verhindern
            if abs(fb - fa) < 1e-15:
                break

            c = b - fb * (b - a) / (fb - fa)

            #wenn der Funktionswert nah genug an Null ist: ABBRUCHHHHH
            if abs(f(c)) < tol:
                break
            # Intervall anpassen (wie Bisektion)
            if f(a) * f(c) < 0:
                b = c
            else:
                a = c

    return c

if __name__ == "__main__":
    
    while True:
            try:
                inp_n: float = float(input("Gebe n an: "))
                break 
            except ValueError:
                print("Falsche Eingabe!")
                
    m_erg: float = solver("x**2 - n", inp_n)
    # Wir berechnen y_erg kurz hier draußen für den Print
    y_erg: float = m_erg**2 - inp_n

    print("-" * 30)
    print(f'''Die Nullstelle für n = {inp_n} lautet:
        P({m_erg:.8f} | {y_erg:.2e})")
        gerundet: P({m_erg:.2f} | 0)
    ''')
    
    print("-" * 30 +"\n Testlauf mit Testwerte (mit der Bisektion aus Aufgabe5.py als Vergleich)" )
    
    
    
    #testwerteeeeeeeeeeee
    test_n_werte = [2.0, 25.0, 81.0, 144.0,]

    print(f"\n{'n':>5} | {'Bisektion':>18} | {'Regula Falsi':>18} | {'Analytisch':>12} | {'Delta (Reg)':>10}")
    print("-" * 80)

    for n in test_n_werte:
        try:
            val_bis: float = solver("x**2 - n", n)
            val_reg: float = solver2("x**2 - n", n)
            val_ana: float = math.sqrt(n)
            abweichung: float = abs(val_reg - val_ana)  
            print(f"{n:5.1f} | {val_bis:18.10f} | {val_reg:18.10f} | {val_ana:12.1f} | {abweichung:10.2e}")
        except Exception as e:
            print(f"Fehler bei n={n}: {e}")
            
