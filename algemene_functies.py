a = 2
b = 4
c = 10
d = 12

def mijn_functie_1(a):
    return a * a


print("Teruggeefwaarde")
print(mijn_functie_1(a))
print(mijn_functie_1(b))
print(mijn_functie_1(c))
print(mijn_functie_1(d))


b = 15
def mijn_functie_2():
    global b
    b = b + 10
print("binnen: ", b)

print("buiten: ", b)
mijn_functie_2()
print("buiten: ",b)
