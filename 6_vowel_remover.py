string = input("Enter a string: ")

out = ""
for s in string:
    if(s == "a" or s == "e" or s == "i" or s == "o" or s == "u"):
        continue
    out += s

print("Result:", out)