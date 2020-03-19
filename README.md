# OCR-image-compraison
>Czech description only (English might be added later to the end of this file)
## Co to je:
Jedná se o součást [maturitní práce][3]. Jedná se o skupinu programů, která může být použita k:
1. Generování různých úprav obrázků pomocí [OpenCV][2], soubor [mastercv.py](../blob/master/mastercv.py)
2. Rozpoznání textu z obrázků ([OCR][5]) pomocí [Tesseractu][4] přes pytesseract, soubor [tesseract.py](../blob/master/tesseract.py)
3. Porovnání dvou textů (jeden s řešením a druhý s textem rozeznaným [Tesseractem][4]) k získání zaokrouhlené obdoby [Word error rate][6], která určuje úspěšnost rozpoznání slov. Soubor [accuracy.py](../blob/master/accuracy.py)
4. Seřazení úspěšností vypočítané [accruacy.py](../blob/master/accuracy.py), soubor [sortovac.py](../blob/master/sortovac.py)
Popis formátu souborů s paramtery určujícími, co tyto programy provedou jsou v [dokumentace.pdf](../blob/master/dokumentace.pdf)
## Maturitní práce
Obsahuje popis postupů, které jsou použity v praktické části. Vysvětluje proč jsou použity a zhodnocuje jejich nedostatky.
Pro úplnost je nahrána (soubor [SP-ambroz.pdf](../blob/master/SP-amborz.pdf)) celá i teoretickou částí, která se programů přímo nedotýká. Zároveň obsahuje i zdrojové soubory(ve složce [MP-ambroz](tree/master/MP-ambroz)) v TeXu (použit XeLaTex a Bib(la)tex). Styl používá (s jen drobnými úpravami) [Jonášova stylu pro Seminární práce][1], který obsahuje i drobný tutoriál na využití TeX a tohoto stylu.


[1]:https://github.com/JoHavel/Maturitni-Seminarni-Prace
[2]:https://opencv.org/
[3]:https://github.com/AmbryTheBlue/OCR-image-compraison#maturitní-práce
[4]:https://github.com/tesseract-ocr/tesseract
[5]:https://cs.wikipedia.org/wiki/Optick%C3%A9_rozpozn%C3%A1v%C3%A1n%C3%AD_znak%C5%AF
[6]:https://en.wikipedia.org/wiki/Word_error_rate
