"""
### Úkol 2 - Prvočísla a palindromy
- Připravte program, který vypíše první prvočíslo, které je větší než uživatelem zadaná hodnota a které je zároveň palindromem.

#### Příklady vstupů a očekávané výstupy
| Vstup    | Výstup          |
| -------- | --------------- |
| 100      | 101             |
| 100000   | 1003001         |
| xy       | Invalid input!  |
"""
from math import sqrt
import sys

def is_palindrom(num):
    # Cislo prevedu na string a ten nasledne otocim
    num_str = str(num)
    reverse_str = num_str[::-1]

    try:
        # Otocene cislo pretypuju zpatky na int
        reverse = int(reverse_str)
    except: # Toto by nemelo snad nikdy nastat, protoze pretypovavam int->str->int
        sys.exit("Doslo k interni chybe pri pretypovani str->int")

    # Pokud se puvodni cislo i jeho revers rovna, jde o palindrom
    return reverse == num


def is_prime(num):
    # Cislo n muze mit unikatni delitele pouze do hodnoty sqrt(n), proto nema smysl hledat dale
    # Priklad pro n = 35: 5 * 7 = 35, staci zkontrolovat 5
    # 7 > sqrt(35), proto pokud je 7 delitel, tak druhy delitel uz musel byt zkontrolovan
    # Zacinam od cisla 2, protoze 1 deli kazde cislo beze zbytku
    for i in range(2, int(sqrt(num)) + 1): 
        if (num % i == 0):
            return False
    return True


if __name__ == '__main__':
    # Zpracovani argumentu (aby byl zadan prave jeden argument)
    if (len(sys.argv) < 2):
        print("Nebyl zadan argument")
        sys.exit("$ python ./script2.py value: int")
    elif (len(sys.argv) > 2):
        print("Zadano mnoho argumentu")
        sys.exit("$ python ./script2.py value: int")

    # Kontrola, zda byl zadan int
    try:
        input = int(sys.argv[1])
    except:        
        sys.exit("Invalid input!")

    # V nekonecnem cyklu kontroluju, zda aktualni cislo je palindrom a prvnocislo, pokud ano, vypisu ho
    # a program ukoncim, jinak inkrementuju a opakuju znova
    # jako prvni kontroluju palindrom, protoze tato kontrola je rychlejsi
    # prvocislo kontroluju jenom v pripade, ze jde o palindrim
    while (True):
        input += 1        
        if is_palindrom(input):
            if is_prime(input):
                print(input)
                exit()
        
