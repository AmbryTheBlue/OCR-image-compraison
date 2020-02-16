#Python 3.7
#Autor: Jakub Ambroz, Gymnazium Jirovcova 8
#Soucast maturitni práce: Umela inteligence a OCR
#Datum: 19.2.20
#verze: 1.0
#github: https://github.com/AmbryTheBlue/OCR-image-compraison
#popis: Program pouzije prikazy OpenCV podle souboru prikazy_path, popis formatu tohoto souboru je v dokumentaci

import os
import errno
import cv2

path = "E:/MP/datasets/pero"
prikazy_path = path + "/prikazy-pro-opencv.txt"

with open(prikazy_path, 'r') as prikazy:
    radka_prikazu = 0
    status = ""
    seznam_vytvorenych_slozek = ""
    for line in prikazy:
        pole = line.split(" ")
        zdroj_path = path + "/" + pole[0]
        db_path = path + "/" + pole[1]
        par_path = path + "/" + pole[2]
        cil_slozka_path = path + "/" + pole[0]

        #test zda jsou v poradku parametry
        chyba_v_par = 0
        pole_par = []
        try:
            with open(par_path) as parametry:
                for line in parametry:
                    pole_par = line.split(" ")
        #print(pole_par)
        except:
            chyba_v_par = 1
            print("Nefunkcni paramtery")


        #test zda-li je zadani korektni
        chyba_v_prikazech = 0
        for i in range(3,len(pole)):
            try:
                ukon = int(pole[i])
                pole[i] = int(pole[i])
                if(ukon<10):#upscale
                    print("resize")
                    if(ukon==1):
                        print("INTER_AREA")
                        cil_slozka_path = cil_slozka_path + "01({})-".format(pole_par[0])
                    elif(ukon==2):
                        print("INTER_CUBIC")
                        cil_slozka_path = cil_slozka_path + "02({})-".format(pole_par[0])
                    elif(ukon==3):
                        print("INTER_LINEAR")
                        cil_slozka_path = cil_slozka_path + "02({})-".format(pole_par[0])
                    else:
                        print("chyba(neznamy prikaz) v prikazy_pro_opnecv.txt")
                        chyba_v_prikazech = chyba_v_prikazech +1
                elif(ukon<20):
                    if(ukon==11):
                        print("to_gray")
                        cil_slozka_path = cil_slozka_path + "11-"
                    else:
                        print("chyba(neznamy prikaz) v prikazy_pro_opnecv.txt")
                        chyba_v_prikazech = chyba_v_prikazech + 1
                elif(ukon<30):
                    if(ukon==21):
                        print("noise_removal")
                        cil_slozka_path = cil_slozka_path + "21({},{},{})-".format(pole_par[1],pole_par[2],pole_par[3])
                    else:
                        print("chyba(neznamy prikaz) v prikazy_pro_opnecv.txt")
                        chyba_v_prikazech = chyba_v_prikazech + 1
                elif(ukon<40):
                    print("blur")
                    if(ukon==31):
                        print("avg")
                        cil_slozka_path = cil_slozka_path + "31({},{})-".format(pole_par[4], pole_par[4])
                    elif(ukon==32):
                        print("bilateral")
                        cil_slozka_path = cil_slozka_path + "32({},{},{})-".format(pole_par[5], pole_par[6], pole_par[7])
                    elif(ukon==33):
                        print("gauss")
                        cil_slozka_path = cil_slozka_path + "33({},{},{})-".format(pole_par[8], pole_par[8], pole_par[9])
                    elif(ukon==34):
                        print("median")
                        cil_slozka_path = cil_slozka_path + "34({})-".format(pole_par[10])
                    else:
                        print("chyba(neznamy prikaz) v prikazy_pro_opnecv.txt")
                        chyba_v_prikazech = chyba_v_prikazech + 1
                elif(ukon<50):
                    print("threshold")
                    if(ukon==41):
                        print("adaptive_mean")
                        cil_slozka_path = cil_slozka_path + "41({},{})-".format(pole_par[11], pole_par[12])
                    elif(ukon==42):
                        print("adaptive_gauss")
                        cil_slozka_path = cil_slozka_path + "42({},{})-".format(pole_par[13], pole_par[14])
                    elif(ukon==43):
                        print("otsu")
                        cil_slozka_path = cil_slozka_path + "43-"
                    else:
                        print("chyba(neznamy prikaz) v prikazy_pro_opnecv.txt")
                        chyba_v_prikazech = chyba_v_prikazech + 1
            except:
                print("chyba(prikaz neni cislo) v prikazy_pro_opnecv.txt")
                chyba_v_prikazech = chyba_v_prikazech + 1



        #otestovani zda-li existuje zdrojova slozka
        if os.path.exists(zdroj_path):
            print("Zdrojova slozka existuje")
            existuje_slozka = True
        else:
            print("Zdrojova slozka nenalezena")
            existuje_slozka = False


        #je-li vse v poradku spusti se program pro tento radek prikazu
        if (0 < chyba_v_prikazech or 0 < chyba_v_par or existuje_slozka==False):
            print("Vysktla se chyba/y ({}) v prikazy-pro-opencv.txt nebo v paramterech ({})  nebo slozka, ze ktere cerpame obrazky - existence({})".format(chyba_v_prikazech,chyba_v_par,existuje_slozka))
            print("Preskakuji tuto radku a pokracuji na dalsi ")
            status = status + "\n\nPrikazova radka c.{} nebyla nactena uspesne. \n Vysktla se chyba/y ({}) v prikazy-pro-opencv.txt nebo v paramterech ({}) nebo slozka, ze ktere cerpame obrazky - existence({}) .\n Radka bude preskocena".format(radka_prikazu, chyba_v_prikazech, chyba_v_par, existuje_slozka)
        else:
            print("Vse v poradku oteviram databazi")
            status = status + "\n\nPrikazova radka c.{} uspesne nactena.".format(radka_prikazu)

            print("{} \nVytvoreni cilove slozky, nebo overeni jeji existence".format(cil_slozka_path))
            ###Vytvor slozku jestli neexistuje
            if not os.path.exists(cil_slozka_path):
                try:
                    os.makedirs(cil_slozka_path, 0o700)
                except OSError as e:
                    if e.errno != errno.EEXIST:
                        raise
            status = status + "\nSlozka {} uspesne vytvorena.".format(cil_slozka_path)

            seznam_vytvorenych_slozek = seznam_vytvorenych_slozek + "\n" + cil_slozka_path.split("/")[4] + " " + pole[1]

            #Otevreni databaze
            if os.path.exists(db_path):
                status = status + "\n Databaze otevrena, probiha uprava"
                with open(db_path, 'r') as db:
                    print(status)
                    db_radky = 0
                    for line in db:
                        db_radky = db_radky + 1
                        img_name = line.strip().split(" ")[0]
                        this_img_path = zdroj_path + "/" + img_name
                        obrazek = cv2.imread(this_img_path)
                        print(this_img_path)
                        for i in range(3, len(pole)):
                            ukon = int(pole[i])
                            if (ukon < 10):
                                #print("resize")
                                if (ukon == 1):
                                    #print("INTER_AREA")
                                    obrazek = cv2.resize(obrazek, None, fx=float(pole_par[0]), fy=float(pole_par[0]), interpolation=cv2.INTER_AREA)
                                elif (ukon == 2):
                                    #print("INTER_CUBIC")
                                    obrazek = cv2.resize(obrazek, None, fx=float(pole_par[0]), fy=float(pole_par[0]), interpolation=cv2.INTER_CUBIC)
                                elif (ukon == 3):
                                    #print("INTER_LINEAR")
                                    obrazek = cv2.resize(obrazek, None, fx=float(pole_par[0]), fy=float(pole_par[0]), interpolation=cv2.INTER_LINEAR)
                            elif (ukon < 20):
                                if (ukon == 11):
                                    #print("to_gray")
                                    obrazek = cv2.cvtColor(obrazek, cv2.COLOR_BGR2GRAY)
                            elif (ukon < 30):
                                if (ukon == 21):
                                    #print("noise_removal")
                                    obrazek = cv2.fastNlMeansDenoising(obrazek, float(pole_par[1]), int(pole_par[2]), int(pole_par[3]))
                            elif (ukon < 40):
                                #print("blur")
                                if (ukon == 31):
                                    #print("avg")
                                    obrazek = cv2.blur(obrazek, (int(pole_par[4]), int(pole_par[4])))
                                elif (ukon == 32):
                                    #print("bilateral")
                                    obrazek = cv2.bilateralFilter(obrazek, int(pole_par[5]), float(pole_par[6]),float(pole_par[7]))
                                elif (ukon == 33):
                                    #print("gauss")
                                    obrazek = cv2.GaussianBlur(obrazek, (int(pole_par[8]), int(pole_par[8])), float(pole_par[9]))
                                elif (ukon == 34):
                                    #print("median")
                                        obrazek = cv2.medianBlur(obrazek, int(pole_par[10]))
                            elif (ukon < 50):
                                #print("threshold")
                                if (ukon == 41):
                                    #print("adaptive_mean")
                                    try:
                                        obrazek = cv2.cvtColor(obrazek, cv2.COLOR_BGR2GRAY)
                                    except:
                                        print("Already grayscale")
                                    obrazek = cv2.adaptiveThreshold(obrazek, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, int(pole_par[11]), float(pole_par[12]))
                                elif (ukon == 42):
                                    #print("adaptive_gauss")
                                    try:
                                        obrazek = cv2.cvtColor(obrazek, cv2.COLOR_BGR2GRAY)
                                    except:
                                        print("Already grayscale")
                                    obrazek = cv2.adaptiveThreshold(obrazek, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, int(pole_par[13]), float(pole_par[14]))
                                elif (ukon == 43):
                                    #print("otsu")
                                    try:
                                        obrazek = cv2.cvtColor(obrazek, cv2.COLOR_BGR2GRAY)
                                    except:
                                        print("Already grayscale")
                                    ret, obrazek = cv2.threshold(obrazek, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
                        this_img_path_new = cil_slozka_path + "/" + img_name
                        cv2.imwrite(this_img_path_new, obrazek)
                        print("db_radka ({}), zapis do souboru({})".format(db_radky,this_img_path_new))
                        if(db_radky%100==0):
                            print(status)
                status = status + "\n Databaze byla uspesne vytvorena v nove slozce"

            else:
                print("Databaze nenalezena. Preskakuji")
                status = status + "\n Databaze nenalezena. Preskoceno"

        radka_prikazu = radka_prikazu + 1

print("Ono to vyslo!!!")
print(status)
print(seznam_vytvorenych_slozek)