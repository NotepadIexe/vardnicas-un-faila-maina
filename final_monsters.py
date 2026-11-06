#5. nosacijums
file = open("skolen.txt", "r", encoding="utf-8")
text = file.read()
list = []
z = 0
a = text.splitlines()
i = 0
for x in a:
    b = a[i].split(", ")
    dictio = {}
    i += 1
    for y in b:
        dictio.update({"vards": b[0]})
        dictio.update({"uzvards": b[1]})
        dictio.update({"atzime": b[2]})
    list.append(dictio)

#1. nosacijums
N = int(input("Cik pievienot klat ierakstu: "))
for x in range(N):
    A = str(input("Ievadi skolena datus: "))
    file = open("skolen.txt", "a", encoding="utf-8")
    file.write(f"\n{A}")
file = open("skolen.txt", encoding="utf-8")
text = file.read()

#2.nosacijums
i = 0
for x in list:
    print(f"Vards: {list[i]['vards']}")
    print(f"Uzvards: {list[i]['uzvards']}")
    print(f"Atzime: {list[i]['atzime']}")
    i += 1

# 3.nosacijums
i = 0
for x in list:
    a: int =list[i]['atzime']
    if float(a) > 7:
        print("Atzime lielaka par 7!!!!!!")
        print(f"Vards: {list[i]['vards']}")
        print(f"Uzvards: {list[i]['uzvards']}")
        print(f"Atzime: {list[i]['atzime']}")
    i += 1

#4. nosacijums
