bingot = []
numerot = []
with open("input4.txt") as tiedosto:
    alku = True
    bingo = []
    for rivi in tiedosto:
        if alku:
            rivi = rivi.strip()
            rivi = rivi.split(",")
            for numero in rivi:
                numerot.append(int(numero))
            alku = False
            continue
        if rivi == "\n" and len(bingo) != 0:
            bingot.append(bingo)
            bingo = []
        elif rivi != "\n":
            bingorivi = []
            rivi = rivi.strip()
            rivi = rivi.split(" ")
            rivi = [numero for numero in rivi if numero]
            for numero in rivi:
                bingorivi.append(int(numero))
            bingo.append(bingorivi)


def ruudukko_oikein(bingoruudukko: list, pelatut: list):
    for rivi in bingoruudukko:
        if vaaka_oikein(rivi, pelatut):
            return True
    for a in range(5):
        if sarake_oikein(bingoruudukko, pelatut, a):
            return True
    

def sarake_oikein(bingoruudukko:list, pelatut: list, sarakenro: int):
    pystyrivi = []
    for rivi in bingoruudukko:
        pystyrivi.append(rivi[sarakenro])
    for luku in pystyrivi:
        if luku not in pelatut:
            return False
    return True

def vaaka_oikein(vaakarivi: list, pelatut: list):
    for luku in vaakarivi:
        if luku not in pelatut:
            return False
    return True


def onko_bingo(bingoruudukot: list, bingonumerot: list):
    pelatut_numerot = []
    for numero in bingonumerot:
        pelatut_numerot.append(numero)
        for bingoruudukko in bingoruudukot:
            if ruudukko_oikein(bingoruudukko, pelatut_numerot):
                print("BINGO")
                print(summa(bingoruudukko, pelatut_numerot, numero))
                return
                

def summa(bingoruudukko: list, pelatut: list, numero: int):
    summa = 0
    for rivi in bingoruudukko:
        for luku in rivi:
            if luku not in pelatut:
                summa += luku
    summa = summa * numero
    return summa
 
onko_bingo(bingot, numerot)


