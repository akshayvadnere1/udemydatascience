x = [1, 2, 3, 4, 5, 6]
print(len(x))
print(x[:3])
print(x[-2:])
x.extend([7, 8])
print(x)
x.append(9)
print(x)

y = [10, 11, 12]
listoflists = [x, y]
print(listoflists)

print(y[1])

z = [3, 2, 1]
z.sort(reverse=True)
print(z)

tup1 = (1, 2, 3)
tup2 = (4, 5, 6)

listoftup = [tup1, tup2]
print(listoftup)

age, income = "32,500".split(",")
print(age, income)

captains = {}
captains["Enterprise"] = "Kirk"
captains["Enterprise D"] = "Picard"
captains["Deep Space Nine"] = "Sisko"
captains["Voyager"] = "Janeway"

print(captains["Voyager"])
print(captains.get("Enterprise"))
#print(captains.get["Akshay"])
print(captains.get("Akshay"))

for ship in captains:
    print(ship + ": " + captains[ship])