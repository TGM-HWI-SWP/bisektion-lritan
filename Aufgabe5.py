import matplotlib as mpl

n = input("Gebe n an: ")

def solver(func_str: str, a: float, b: float, tol: float = 1e-6) -> float:
    """
    Findet eine Nullstelle mittels Bisektion.
    :param func_str: Die Funktion als String, z.B. "x**2 - 25"
    :param a: Untere Intervallgrenze
    :param b: Obere Intervallgrenze
    :param tol: Abbruchkriterium (Genauigkeit) =1e-6 numerische Nullstelle um so nah wie möglich ans das Ergebniss zu kommen
    """
    
    #Initialisierung a und b
    a = 0
    b = 0.2 * n

    # f(x) = x^2 - n
    fa = a**2 - n
    fb = b**2 - n
    
    pass


if __name__ == "__main__":
    
    solver()