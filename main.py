from math import sqrt

#### Fonction secondaire


def isprime(p):

    # votre code ici
    if p <= 1 :
        return False
    elif p == 2 :
        return True
    elif p % 2 == 0 :
        return False

    for i in range(3, int(sqrt(p))+1, 2) :
        if p%i == 0 :
            return False
    return True

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
