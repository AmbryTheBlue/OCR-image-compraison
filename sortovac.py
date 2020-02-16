#Python 3.7
#Autor: Jakub Ambroz, Gymnazium Jirovcova 8
#Soucast maturitni práce: Umela inteligence a OCR
#Datum: 19.2.20
#verze: 1.0
#github: https://github.com/AmbryTheBlue/OCR-image-compraison
#popis: Uspporada kombinace prikazu podle uspesnosti rozpoznani Tesseractem z vystupniho souboru accuracy.py

path = "E:/MP/datasets/pero"
f_path = path + "/" + "procenta.txt"
cil_path = path + "/" + "sorted-to-percent.txt"

with open(f_path) as zdroj:
    velke_pole = []
    for line in zdroj:
        pole = line.strip().split("\t")
        velke_pole.append(pole)
novy_list = sorted(velke_pole, key=lambda x:x[1])
print(novy_list)
with open(cil_path, 'w') as cil:
    for radek in novy_list:
        cil.write("{}\t{}\t{}\t{}\t{}\n".format(radek[0],100*float(radek[1]),100*float(radek[2]),radek[3],radek[4]))