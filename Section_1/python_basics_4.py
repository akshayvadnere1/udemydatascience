# Boolean

print(1 == 3)
print(True or False)
print(1 == 3)

if 1 == 3:
    print("How did that happen")
elif 1 > 3:
    print("Yikes")
else:
    print("All is good in the world")

# Looping

for i in range(10):
    print(i)

for i in range(10):
    if i == 1:
        continue
    if i > 5:
        break
    print(i)

x = 0
while x < 10:
    print(x)
    x += 1

# Activity

integers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\nActivity\n")
for i in integers:
    if i % 2 == 0:
        print(i)