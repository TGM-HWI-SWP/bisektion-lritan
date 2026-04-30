from Aufgabe5 import solver
from Aufgabe6 import solver2
from Aufgabe7 import plotter
import math


def berechne_seillaenge():
    func_str = "math.cosh(50/x) - 1 - 10/x"

    #solverrrrrr
    a = solver(func_str, a=100, b=200, tol=1e-10)
    print(f"Gefundener Krümmungsradius a = {a:.6f} m")

    # Seillänge
    l = 2 * a * math.sinh(50 / a)
    print(f"Seillänge l = {l:.6f} m")

    return a, l

if __name__ == "__main__":
    a, l = berechne_seillaenge()
    
