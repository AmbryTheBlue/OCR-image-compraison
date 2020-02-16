#Python 3.7
#Autor: Jakub Ambroz, Gymnazium Jirovcova 8
#Soucast maturitni práce: Umela inteligence a OCR
#Datum: 19.2.20
#verze: 1.0
#github: https://github.com/AmbryTheBlue/OCR-image-compraison
#popis: Vola Tesseract k rozeznani textu z obrazku ve slozce imgpath z databaze obrazku dbpath. Vysledky ulozi do textoveho souboru. Vyzaduje nainstalovany Tesseract na pocitaci.

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
path = "E:/MP/datasets/pero"
list_path = path + "/soubory-pro-tesseract.txt"

chyba_zapis =0
chyba_tesseract =0
with open(list_path, 'r') as f_master:
    j = 0
    for radka in f_master:
        pole = radka.split(" ")
        imgpath = path + "/" + pole[0].strip()
        dbpath = path + "/" + pole[1].strip()
        with open(dbpath,'r') as f_read:
            i = 0
            for line in f_read:
                i = i +1
                pole_imgname = line.strip().split(" ")
                imgname = pole_imgname[0]
                this_imgpath = imgpath + "/" + imgname
                filepath = this_imgpath + ".tess"
                print("(" + str(j) + ") " + str(i) + " : " + filepath)
                try:
                    konverze = pytesseract.image_to_string(Image.open(this_imgpath),lang="eng")
                    #print(konverze.strip())
                    with open(filepath, 'w') as f_write:
                        try:
                            f_write.write(konverze)
                            print(konverze)
                        except:
                            f_write.write("Encoding_failed")
                            print("Encoding_failed:")
                            print(konverze)
                            chyba_zapis = chyba_zapis+1
                except:
                    print(str(i) + " : " + "Chyba v tesseractu(asi soubor neexistuje)")
                    chyba_tesseract = chyba_tesseract + 1
            j = j + i
            print("Chyb v zapise:" + str(chyba_zapis))
            print("chyb v tesseractu: " +str(chyba_tesseract))
