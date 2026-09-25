

def main() :

    n = 100
    numero1 = 1 
    numero2 = 1
    for i in range(n) :
        numtemp = numero2
        numero2 = numero1 + numero2
        numero1 = numtemp
        print(numero2)


main()