
# ---------------UZDUOTIS------------------------------------
# Sukurkite sarasa is ivairaus tipo elementu privalo buti bent pora bool, bent pora int float, stringu...
# Pasinaudodami list comprehension ir is instance suskaičiuokite atskirai intu ir boolu kieki (int ir bool kiekis kartu)
# Ir apskaičiuokite stringu kieki
# Apskaičiuokite sąraše esančių skaičių (int, float, bool) sumą (Ne kiekį)
mano_sarasas = [True, False, 10, 25, 3.14, 2.71, "labas", "pasauli", 7.5, 0, True]
int_bool_kiekis = sum([1 for x in mano_sarasas if isinstance(x, (int, bool))])  
# Ši eilutė suskaičiuoja kiek dėžutėje yra int ir bool elementų.
# for x in mano_sarasas reiškia: "Eik per kiekvieną daiktą sąraše"
# if isinstance(x, (int, bool)) reiškia: "Jei šis daiktas yra int arba bool tipo..."
# [1 for ...] reiškia: "Už kiekvieną atitinkantį, parašyk vienetą (1)"
# # sum(...) reiškia: "Sudėk visus tuos vienetus"
string_kiekis = sum([1 for x in mano_sarasas if isinstance(x, str)])
#  Ši eilutė suskaičiuoja kiek yra tekstų (str tipo).
skaiciu_suma = sum([x for x in mano_sarasas if isinstance(x, (int, float, bool))])
# Čia suskaičiuojama visų skaičių suma. Net True ir False:
# True = 1
# False = 0
# Pvz., jei turėtume 10, 3.14, True, tai gautume 10 + 3.14 + 1 = 14.14.


print("Int ir Bool kiekis:", int_bool_kiekis)
print("String kiekis:", string_kiekis)
print("Skaičių suma:", skaiciu_suma)

# REZULTATAS TERMINALE:
# Int ir Bool kiekis: 6
# String kiekis: 2
# Skaičių suma: 50.35