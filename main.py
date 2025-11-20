"""Module contenant une fonction qui teste si un entier est premier."""
from math import sqrt

#### Fonction secondaire


def isprime(p):
    """Retourne True si p est un nombre premier."""
    # votre code ici
    if p <= 1 :
        return False
    if p == 2 :
        return True
    if p % 2 == 0 :
        return False

    for i in range(3, int(sqrt(p))+1, 2) :
        if p%i == 0 :
            return False
    return True

#### Fonction principale


def main():
    """Affiche les nombres premiers inférieurs à 100."""
    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
