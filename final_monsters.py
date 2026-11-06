#5. nosacijums 
file = open("skolen.txt", "r", encoding="utf-8")
text = file.read()
list1 = []
z = 0
a = text.splitlines()
for x in a:
    z += 1
i = 0
for x in a:
    b = a[i].split(", ")
    dictio = {}
    i += 1
    for y in b:
        dictio.update({"vards": b[0]})
        dictio.update({"uzvards": b[1]})
        dictio.update({"atzime": b[2]})
    list1.append(dictio)

#1. nosacijums Site var pievienot failam ierakstus
N = int(input("Cik pievienot klat ierakstu: "))
for x in range(N):
    A = str(input("Ievadi skolena datus: "))
    file = open("skolen.txt", "a", encoding="utf-8")
    file.write(f"\n{A}")
file = open("skolen.txt", encoding="utf-8")
text = file.read()

#2.nosacijums
i = 0
for x in list1:
    print(f"Vards: {list1[i]['vards']}")
    print(f"Uzvards: {list1[i]['uzvards']}")
    print(f"Atzime: {list1[i]['atzime']}")
    i += 1

# 3.nosacijums
i = 0
for x in list1:
    a: float= list1[i]['atzime']
    if float(a) > 7:
        print("Atzime lielaka par 7!!!!!!")
        print(f"Vards: {list1[i]['vards']}")
        print(f"Uzvards: {list1[i]['uzvards']}")
        print(f"Atzime: {list1[i]['atzime']}")
    i += 1

#4. nosacijums
sum = 0
i = 0
for x in list1:
    a: float= list1[i]['atzime']
    sum += float(a)
    i += 1
i = 0
vid = sum/z
print(vid)
for x in list1:
    a: float= list1[i]['atzime']
    if float(a)<z:
        print("Mazaks par videjo!!!")
        print(f"Vards: {list1[i]['vards']}")
        print(f"Uzvards: {list1[i]['uzvards']}")
        print(f"Atzime: {list1[i]['atzime']}")
    i += 1
