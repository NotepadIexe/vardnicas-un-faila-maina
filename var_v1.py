#5.nosacijums
file = open("skolen.txt", "r", encoding="utf-8")
text = file.read()

#1. nosacijums
N = int(input("IEvadi cik gribi ierakstu vardnica: "))
dic = {}
for x in range(N):
    dic[x] = str(input("Ievadi vardu uzvardu un atzimi: "))
#2. nosacijums
for x in dic:
    a = dic[x].split()
    print(f"Vards: {a[0]}, uzvards {a[1]}, atzime {a[2]}")
# 3.nosacijums
for x in dic:
    a = dic[x].split()
    if int(a[2]) > 7:
        print("Atzime lielaka par 7")
        print(f"Vards: {a[0]}, uzvards {a[1]}, atzime {a[2]}")
#4. nocaijums
sum = 0
for x in dic:
    a = dic[x].split()
    sum += int(a[2])
vid = sum/(N+1)
for x in dic:
    a = dic[x].split()
    if int(a[2]) < vid:
        print(f"Vards: {a[0]}, uzvards {a[1]}, atzime {a[2]}")