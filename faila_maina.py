with open("skolen.txt", "a") as f:
    f.write(f"\nNow the file has more content!")

#open and read the file after the appending:
with open("skolen.txt") as f:
    print(f.read())

