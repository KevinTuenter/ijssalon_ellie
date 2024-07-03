def decoreer(tekst=""):
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()

def fooi_pp(bedrag, personen):
    try:
        bedrag_pp = bedrag / personen
    except:
        bedrag_pp = "??"
    return f"Het bedrag per persoon is {bedrag_pp} Euro"

def onderstreep(tekst=""):
    uit = []
    uit.append(tekst)
    uit.append(len(tekst) * "=")
    return uit


def som(inkomsten):
    de_som = []
    de_som.append(inkomsten)
    de_som.append(sum(inkomsten.values()))
    return sum(inkomsten.values())
    


    
    

