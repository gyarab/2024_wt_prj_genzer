import httpx

print('ahoj')
url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt?date=13.02.2025"
r = httpx.get(url)

lines = r.text.split("\n")

row = ""
for line in lines:
    if "|EUR|" in line:
        row = line

row_arr = row.split("|")

kurz_str = row_arr[-1]
kurz_str = kurz_str.replace(",", ".")

kurz = float(kurz_str)
print(kurz)

while True:
    smer = input("Zadej smer prevodu (1 = EUR na CZK, 2 = CZK na EUR): ")
    if smer in ["1", "2"]:
        break
    else:
        print("Chyba")

while True:
    vstup = input("Zadej castku: ")
    try:
        castka = float(vstup)
        if castka < 0:
            print("Chyba")
            continue
        break
    except ValueError:
        print("Chyba")

if smer == "1":
    vysledek = castka * kurz
    print(f"Vysledek je {vysledek:.2f} CZK")
else:
    vysledek = castka / kurz
    print(f"Vysledek je {vysledek:.2f} EUR")

