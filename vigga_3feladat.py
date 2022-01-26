#NG
print("1. feladat: ")
print("------------------------------")
cars = []

with open("jarmu.txt") as ff:
    for sor in ff:
        ora, perc, mp, rendszam = sor.split()
        cars.append((int(ora), int(perc), int(mp), rendszam))

print(cars, "\n")
print("2. feladat: ")
print("------------------------------")
print("A  rendőrök legalább", cars[-1][0] + 1 - cars[0][0], "órát dolgoztak.""\n")

print("3. feladat: ")
print("------------------------------")
print("Műszaki ellenőrzésen átesett járművek:")
vizsgaltido = None
for ora, perc, mp, rendszam in cars:
    if ora != vizsgaltido:
        print(ora, "óra", rendszam)
        vizsgaltido = ora

print("")

print("4. feladat: ")
print("------------------------------")
def idodiff(kezdo, vegso):
    ko, kp, kmp = kezdo
    vo, vp, vmp = vegso
    return vo*3600 + vp*60 + vmp - ko*3600 - kp*60 - kmp

with open("vizsgalat.txt", "w", encoding="utf-8") as ff:
    ff.write("{0:02d} {1:02d} {2:02d} {3}\n".format(*cars[0]))
    vizsgaltido= cars[0]

with open("vizsgalat.txt", "a") as ff:
    for i in range(len(cars)):
        if idodiff(vizsgaltido[:3], cars[i][:3]) >= 5*60:
            ff.write("{0:02d} {1:02d} {2:02d} {3}\n".format(*cars[i]))
            vizsgaltido = cars[1]

print("Lásd a vizsgalat.txt-ben")
