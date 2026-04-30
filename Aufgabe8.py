import math
from Aufgabe5 import solver

def sqm_test():
    # Das Polynom 
    func_poly = "2*x + x**2 + 3*x**3 - x**4"
    # Gewünschte Genauigkeiten ε
    genauigkeiten = [1e-2, 1e-8]
    
    print(f"{'Ziel-ε':>10} | {'Ergebnis x':>15} | {'Schritte':>10} | {'Status'}")
    print("-" * 60)

    for eps in genauigkeiten:
        try:
            res = solver(func_poly, a =3,b=4, tol=eps) 

            schritte = math.ceil(math.log2(4 / eps))

            #Nullstelle?
            y_check = eval(func_poly, {"x": res, "math": math})
            if abs(y_check):
                status = "OK"
            else:
                eps = "Abweichung"
            
            print(f"{eps:10.0e} | {res:15.10f} | {schritte:10} | {status}")
            
        except Exception as e:
            print(f"Fehler bei ε={eps}: {e}")

if __name__ == "__main__":
    print("=== Softwarequalitätsmanagement Phase ===")
    print("Testfall: Polynom P4(x) im Bereich [3, 4]")
    sqm_test()
    print("-" * 60)
    print("Interpretation: Die Bisektion benötigt für jede weitere")
    print("Dezimalstelle ca. 3.32 Iterationen (log2(10)).")
    
    print("\nTestfall 1: Mehrere Nullstellen (x^3 - 6x)")
    func_multi = "x**3 - 6*x"
    try:
        res = solver(func_multi, a=-100,b=6, tol=1e-6)
        print(f"Gefundene Nullstelle: x = {res:.6f}")
    except Exception as e:
        print(f"Fehler: {e}")

