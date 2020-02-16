#Python 3.7
#Autor: Jakub Ambroz, Gymnazium Jirovcova 8
#Soucast maturitni práce: Umela inteligence a OCR
#Datum: 19.2.20
#verze: 1.0
#github: https://github.com/AmbryTheBlue/OCR-image-compraison
#popis: Spocita uspesnost rozpoznani slov Tesseractem pro ruzné kombinace prikazu. A ulozi do textoveho souboru.

path = "E:/MP/datasets/pero"
list_path = path + "/soubory-pro-evaluaci.txt"
cil_path = path + "/procenta.txt"

celkem_unknown_error = 0
cely_text = ""
with open(list_path) as seznam_slozek:
    for line in seznam_slozek:
        img_path = path + "/" + line.split(" ", 1)[0].strip()
        #print(img_path)
        db_path = path + "/" + line.split(" ", 1)[1].strip()
        with open(db_path) as seznam_obrazku:
            cislo_radky = 0
            celkem_pocet_cilovych_slov = 0
            celkem_pocet_zbylych_cilovych_slov = 0
            unknown_error = 0
            celkem_error_rate = 0.0
            for radka in seznam_obrazku:
                cislo_radky = cislo_radky + 1
                cilova_slova = radka.split(" ",1)[1].strip().split(" ")
                potess_path = img_path + "/" + radka.strip().split(" ",1)[0] + ".tess"
                prelozeny_text_oneline = ""
                funkcni_radka = True
                try:
                    with open(potess_path) as prelezeny_text:
                        for miniradka in prelezeny_text:
                            prelozeny_text_oneline = prelozeny_text_oneline + miniradka.strip() + " "
                except:
                    #print("Unknown error. Soubor asi neexistuje, ale nevim proc. Asi nejaka chyba zapisu pri vytvareni souboru.")
                    unknown_error = unknown_error + 1
                    funkcni_radka = False
                if(funkcni_radka):
                    prelozena_slova = prelozeny_text_oneline.strip().split(" ")
                    pocet_cilovych_slov = len(cilova_slova)
                    if(prelozena_slova[0] != "Encoding_failed"):
                        celkem_pocet_cilovych_slov = celkem_pocet_cilovych_slov + pocet_cilovych_slov
                        for test_slovo in prelozena_slova:
                            for spravne_slovo in cilova_slova:
                                if(test_slovo==spravne_slovo):
                                    cilova_slova.remove(spravne_slovo)
                                    break
                            if(len(cilova_slova)==0):
                                break
                        zbyly_pocet_cilovych_slov = len(cilova_slova)
                        celkem_pocet_zbylych_cilovych_slov = celkem_pocet_zbylych_cilovych_slov + zbyly_pocet_cilovych_slov
                        error_rate = zbyly_pocet_cilovych_slov/pocet_cilovych_slov
                        celkem_error_rate = celkem_error_rate + error_rate
                    else:
                        cislo_radky = cislo_radky - 1
                else:
                    cislo_radky = cislo_radky - 1
            #print("pocet nevysvetlitelnych chyb: " + str(unknown_error))
            celkem_unknown_error = celkem_unknown_error + unknown_error
            print(img_path)
            prumer_slovovy_error_rate = celkem_pocet_zbylych_cilovych_slov/celkem_pocet_cilovych_slov
            print("Prumerny error rate({}/{}): ".format(str(celkem_pocet_zbylych_cilovych_slov) ,celkem_pocet_cilovych_slov) + str(prumer_slovovy_error_rate))
            prumer_radkovy_error_rate = celkem_error_rate / cislo_radky
            print("Prumerny error rate na radce(pocet {}): ".format(cislo_radky) + str(prumer_radkovy_error_rate))
            print()
            cely_text = cely_text + line.split(" ", 1)[0].strip() + "\t" + str(prumer_slovovy_error_rate) + "\t" + str(prumer_radkovy_error_rate) + "\t{}/{}\t{}".format(celkem_pocet_zbylych_cilovych_slov, celkem_pocet_cilovych_slov, cislo_radky) + "\n"
    with open(cil_path, 'w') as soubor:
        soubor.write(cely_text)
    print("Vse dobehlo hladce.")
    print("Az na {} neznamych erroru".format(celkem_unknown_error))



