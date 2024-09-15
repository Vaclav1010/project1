print("Ahoj studenti Pytohn Akademie")

mesta = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
ceny = (150, 200, 120, 120, 100, 180)
cara = "=" * 35
nabidka = """
1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180
"""


print("VITEJTE U NASI APLIKACE DESTINATO!")
cara = "=" * 35
print(cara)
print(f"{nabidka}\n{cara}")
destinace = input("CISLO DESTINACE: ")
jmeno = input("JMENO: ")
prijmeni = input("PRIJMENI: ")
mail = input("MAIL: ")
print(cara)
spravna_destinace = mesta[int(destinace) - 1]
cena = ceny[int(destinace) - 1]
print(f"""DEKUJI, {jmeno}, ZA OBJEDNAVKU,
CIL. DESTINACE:, {spravna_destinace}, CENA JIZDNEHO: {cena} Kč.
NA TVUJ MAIL, {mail}, JSME TI POSLALI LISTEK.""")


