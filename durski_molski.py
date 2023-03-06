nazivi_tonova = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'H']
polozaji_tonova = list(range(12))

pocetni_ton = input('Unesite početni ton (npr. C, C#, D, ...): ')
while pocetni_ton not in nazivi_tonova:
    pocetni_ton = input('Unesite početni ton (npr. C, C#, D, ...): ')

pozicija = nazivi_tonova.index(pocetni_ton)  

durski = [nazivi_tonova[(pozicija + i) % len(nazivi_tonova)] for i in [0, 4, 7]]
molski = [nazivi_tonova[(pozicija + i) % len(nazivi_tonova)] for i in [0, 3, 7]]

akordi = {'Durski': durski, 'Molski': molski}

for naziv_akorda, polozaji in akordi.items():
    print(naziv_akorda + ':', ', '.join(polozaji))
