from algemene_functies import mijn_functie_2

#8.12 opgave 5
smaak = "aardbei"
prijs = 4
korting = 0.1

def totaal_korting():
    global prijs
    berekening_1 = prijs * korting
    prijs_korting = prijs - berekening_1
    return prijs_korting
text_1 = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs:.2f} Euro voor {totaal_korting():.2f} Euro "

print(text_1)

#8.12 opgave 6 + 7

#verdiensten
ma = 220
di = 430
wo = 125
do = 160
vr = 205
za = 90
zo = 345

def inkomsten_totaal(ma, di, wo, do, vr, za, zo):
    omzet = ma + di + wo + do + vr + za + zo
    return omzet

def btw(inkomsten):
    return inkomsten * 0.09



totaal_inkomsten = inkomsten_totaal(ma, di, wo, do, vr, za, zo)
btw_bedrag = btw(totaal_inkomsten)

text_2 = f"Het totaal van alle inkomsten van deze week is {totaal_inkomsten:.2f} Euro, waarover {btw_bedrag:.2f} Euro btw betaald dient te worden."

print(text_2)


#8.12 opgave 8

def laag_hoog(ma, di, wo, do, vr, za, zo):
    mijn_lijst = [ma, di, wo, do, vr, za, zo]
    hoogste = max(mijn_lijst)
    laagste = min(mijn_lijst)
    return laagste, hoogste

laagste, hoogste = laag_hoog(ma, di, wo, do, vr, za, zo)

print(f"Laagste: {laagste}, Hoogste: {hoogste}")

#8.12 opgave 9 + 10

def gemiddelde(ma, di, wo, do, vr, za, zo):
    import statistics
    Mijn_lijst = [ma, di, wo, do, vr, za, zo]
    return statistics.mean(Mijn_lijst)

print(f"De gemiddelde inkomsten deze week zijn", gemiddelde(ma, di, wo, do, vr, za, zo), "Euro")

#8.12 opgave 11

def meervoudig():
    invoer_lijst = [10, 5, 3, 2, 1, 2, 9]
    hoogste = max(invoer_lijst)
    laagste = min(invoer_lijst)
    return laagste, hoogste
laagste, hoogste = meervoudig()

print(f"laagste: {laagste}, hoogste: {hoogste}")

#8.12 opgave 12

def combinatie(invoer_lijst_2):
    invoer_lijst_2 = meervoudig()
    hoogste = max(invoer_lijst_2)
    laagste = min(invoer_lijst_2)
    return laagste, hoogste

laagste, hoogste = combinatie([])

print(f"Laagste: {laagste}, Hoogste: {hoogste}")