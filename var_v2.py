file = open("skolen.txt", "r", encoding="utf-8")
text = file.read()
list = []
z = 0
a = text.splitlines()
i = 0
for x in a:
    b = a[i].split(",")
    dictio = {}
    i += 1
    for y in b:
        dictio.update({"vards": b[0]})
        dictio.update({"uzvards": b[1]})
        dictio.update({"atzime": b[2]})
    list.append(dictio)
print(list)