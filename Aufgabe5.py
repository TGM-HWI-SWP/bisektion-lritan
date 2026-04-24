import matplotlib as mpl
import math

while True:
    try:
        inp_n: float = float(input("Gebe n an: "))
        break 
    except ValueError:
        print("Falsche Eingabe: Bitte gebe eine Zahl ein!")

def solver(func_str: str, n_val: float, tol: float = 1e-7) -> float:
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
            return eval(func_str, {"x": x_wert, "n": n_val, "math": math})
        except Exception as e:
            raise ValueError(f"Fehler in der Funktionsauswertung: {e}")
    
    #Initialisierung a und b
    a:float = 0.0
    b:float = 0.2 * n_val

    if f(a) * f(b) >= 0: # falls 0.2 *n nicht für b reicht
        #print("Das gewählte Intervall [a, b] schließt die Nullstelle nicht ein!")
        b = n_val + 1
    
    
    m = (a + b) / 2 # startwert für die Bisektion 
    while abs(f(m)) > tol:
        m = (a + b) / 2
            
            #Vorzeichenprüfung /für Intervallhalbierung
        if f(a) * f(m) < 0:
            b = m # Nullstelle liegt links
        else:
            a = m  # Nullstelle liegt rechts
    
    # Finalen y-Wert für die Anzeige berechnen
    y_erg: float = f(m) 
        
    print(f"Die Nullstelle für n= {n_val} lautet:\n P({m}|{y_erg})")     
    # :.2f rundet auf 2 Stellen, :.2e zeigt die kleine Zahl schöner an
    print(f"\ngerundet??:\n P({m:.2f} | {0})\n")   


    return m


        
if __name__ == "__main__":
    
    solver("x**2 - n", inp_n)
    
    test_werte = [25,81,144]
    for n in test_werte:
            print(f"\n--- Testlauf für n = {n} ---")

            numerisch: float = solver("x**2 - n", n)

            # Analytische Lösung berechnen (Vergleichswert)
            analytisch: float = math.sqrt(n)
            # Abweichung berechnen
            abweichung: float = abs(numerisch - analytisch)

            print(f"Numerisch:  {numerisch:.8f}")
            print(f"Analytisch: {analytisch:.8f}")
            print(f"Differenz:  {abweichung:.2e}\n--------------------------")    
    
