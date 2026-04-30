import matplotlib as mpl
import math


def solver(func_str: str, a: float, b: float, tol: float = 1e-7) -> float:
    """Findet eine Nullstelle mittels Bisektion.
    
    :param func_str: Die Funktion als String, z.B. "x**2 - n"
    :param n_val: Der Wert für n, der in der Formel genutzt wird
    :param a: Untere Intervallgrenze
    :param b: Obere Intervallgrenze
    :param tol: Toleranz (Abbruchkriterium) - Genauigkeit =1e-6 numerische Nullstelle um so nah wie möglich ans das Ergebniss zu kommen 
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
            return eval(func_str, {"x": x_wert, "math": math})
        except Exception as e:
            raise ValueError(f"Fehler in der Funktionsauswertung: {e}")
    

    if f(a) * f(b) >= 0: 
        #print("Das gewählte Intervall [a, b] schließt die Nullstelle nicht ein!")
        raise ValueError("Fehler: f(a) und f(b) müssen unterschiedliche Vorzeichen haben!")


    
    while True:
        m = (a + b) / 2
        fm = f(m)

        if abs(fm) < tol:
            return m

        if f(a) * fm < 0:
            b = m
        else:
            a = m  # Nullstelle liegt rechts


        
if __name__ == "__main__":
    while True:
        try:
            inp_n: float = float(input("Gebe n an: "))
            break 
        except ValueError:
            print("Falsche Eingabe: Bitte gebe eine Zahl ein!")

    m_erg: float = solver(f"x**2 - {inp_n}", a=0, b=inp_n, tol=1e-7)

    # y-Wert berechnen
    y_erg: float = m_erg**2 - inp_n

    print("-" * 30)
    print(f'''Die Nullstelle für n = {inp_n} lautet:
        P({m_erg:.8f} | {y_erg:.2e})
        gerundet: P({m_erg:.2f} | 0)''')
    print("-" * 30)

    # Testwerte
    test_werte = [25, 81, 144]

    print(f"Testlauf mit Testwerte\n{'n':>5} | {'Bisektion':>18} | {'Analytisch':>12} | {'Delta':>10}")
    print("-" * 80)

    for n in test_werte:
        numerisch: float = solver(f"x**2 - {inp_n}", a=0, b=inp_n, tol=1e-7)
        analytisch: float = math.sqrt(n)
        abweichung: float = abs(numerisch - analytisch)

        print(f"{n:5.1f} | {numerisch:18.10f} | {analytisch:12.1f} | {abweichung:10.2e}")
