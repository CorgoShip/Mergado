"""
## Zadání
### Úkol 1 - Rekurze:
Napište funkci ``word_chain``, která na vstupu dostane libovolně velkou množinu slov a vrátí největší počet slov, které lze zřetězit jeden po druhém tak, že první písmeno druhého slova je stejné jako poslední písmeno prvního slova. Opakování slov není povoleno.

Příklady:

```
word_chain({'goose', 'dog', 'ethanol'}) == 3  # dog – goose – ethanol
word_chain({'why', 'new', 'neural', 'moon'}) == 3  # (moon – new – why)
```
"""
import itertools
# funkce vytvori permutace dane delky a pote zkontroluje, za jsou valdini
# vrati prvni validni permutaci, na kterou narazi
# funkce zacina s permutacemi maximalni delky a pokud zadna takova neni validni,
# vytvori permutace o jedna mensi delky, pokud zadna permutace neni validni,
# pak funkce vraci prvni permutaci delky jedna (ta je vzdy validni)
def word_chain(input):
    for i in range(len(input)):
        permuts = list(itertools.permutations(list(input), r=(len(input) - i)))
       
        for perm in permuts:
            last_char = ""
            is_valid = True

            for idx, item in enumerate(perm):
                if idx == 0:
                    last_char = item[-1]
                elif item[0] == last_char:
                    last_char = item[-1]
                else:
                    is_valid = False
                
            if is_valid:
                return len(perm)

if __name__ == '__main__':
    
    input = {'why', 'new', 'neural', 'moon', 'qweas', 'iopoip'}
    # input = {'awhyq', 'sneww', 'dneurale', 'fmoonr', 'gbnmbnt', 'hcvbcvbcvby'}

    # print(word_chain(input))

    print(word_chain({'goose', 'dog', 'ethanol'}))
