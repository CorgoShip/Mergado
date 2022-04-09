"""
### Úkol 3 - Hokej
- Z webu https://isport.blesk.cz/vysledky/hokej/liga?action=season&season=3089 vyscrapujte výsledky všechny zápasů
- Vyfiltrujte zápasy, které vyhrál Váš oblíbený tým
- Vypište datum a jméno poraženého týmu

#### Příklad výstupu
```
13. 3. jsme porazili Vítkovice
14. 3. jsme porazili Vítkovice
17. 3. jsme porazili Vítkovice
18. 3. jsme porazili Vítkovice
31. 3. jsme porazili Plzeň
1. 4. jsme porazili Plzeň
4. 4. jsme porazili Plzeň
7. 4. jsme porazili Plzeň
15. 4. jsme porazili Třinec
18. 4. jsme porazili Třinec
19. 4. jsme porazili Třinec
22. 4. jsme porazili Třinec
```
"""

import re
import urllib.request


# Princip fungovani parseru:
# Pro kazdou polozku (datum, vitez a porazeny) si najdu tag,
# ktery je tesne pred hledanou hodnotou a pomoci regexu ji vytahnu
def parse_section(section, our_team):    
    zapasy = section.split('<div class="datetime-container">')

    for idx, item in enumerate(zapasy):
        if idx == 0:
            continue

        date = re.search(r"\d+\.\s\d.", zapasy[idx])
        date = date.group(0)
     
        loser = zapasy[idx].split('<div class="team-name team-looser">')
        loser = re.search(r"[a-zA-Z0-9À-ž]+", loser[1])
        loser = loser.group(0)

        winner = zapasy[idx].split('<div class="team-name">')
        winner = re.search(r"[a-zA-Z0-9À-ž]+", winner[1])
        winner = winner.group(0)

        if (winner == our_team):
            print(F"{date} jsme porazili {loser}")


if __name__ == '__main__':
    with urllib.request.urlopen('https://isport.blesk.cz/vysledky/hokej/liga?action=season&season=3089') as response:

        OUR_TEAM = "Brno" # Tady se na nastavit, z pohledu ktereho tymu vypis delame
          
        decoded_response = response.read().decode()

        # Toto odstrani velkou cast html, ve ktere nejsou relevantni data (napriklad by byl problem, kdyby
        # i tato cast obsahovala tagy podle kterych parsuju data)
        shorter_response = decoded_response.split('</div><div class="box-container no-padding hockey">')

        parse_section(shorter_response[0], OUR_TEAM)

