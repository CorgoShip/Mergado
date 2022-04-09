"""
### Úkol 4 - Validace textového souboru
- Připravte script pro validaci [tohoto](https://pastebin.com/tNmieVFn) CSV souboru ve formátu:
    - Jméno knihy; Jméno autora; ISBN; cena
- Validujte, že všechny hodnoty jsou zadané, že ISBN je ve správném formátu a že cena je kladné číslo
    - cena je zadána jako desetinné číslo oddělené tečkou nebo čárkou, doplněné o měnu (Kč nebo €)
- Pokud narazíte na nevalidní řádek, vypište číslo řádku a jaký nastal problém

#### Příklad výstupu
```
Invalid ISBN on line: 21
Missing title on line: 67
Invalid price on line: 90
Missing author on line: 149
Error! 3 column(s) on line 185!
Invalid price on line: 224
"""

import csv
import re

def check_title(title: str):
    return title.strip()

def check_author(author: str):
    return author.strip()

def check_isbn(isbn: str):
    # soubor obsahuje pouze ISBN10
    
    if len(isbn) != 10:
        return False
     
    weight = 10
    sum = 0

    for i in range(9):
        try:
            digit = int(isbn[i])
        except:            
            return False

        sum += digit * weight        
        weight -=1       
   
    try:
        last_digit = int(isbn[9])
        sum += last_digit
    except:
        if (isbn[9] == "X"):
            sum += 10           
        else:
            return False
    
    return (sum % 11 == 0)

def check_price(price: str):
    result =  re.match(r"^\d+[.,]\d+[ ]?((Kč)|€)$", price.strip())
    return bool(result) 


if __name__ == '__main__':
    with open("tNmieVFn.csv", newline='') as csvfile:
        csvReader = csv.reader(csvfile, delimiter=';')
        for idx, row in enumerate(csvReader, start=1):
            if len(row) < 4:
                # Pokud radek neobsahuje 4 polozky, tak neni validni                
                print(F"Error! {len(row)} column(s) on line {idx}!")
            else:
                if (not check_title(row[0])):
                    print(F"Missing title on line: {idx}")                            
                elif (not check_author(row[1])):
                    print(F"Missing author on line: {idx}")                
                elif (not check_isbn(row[2])):
                    print(F"Invalid ISBN on line: {idx}")
                elif (not check_price(row[3])):
                    print(F"Invalid price on line: {idx}")
                    
