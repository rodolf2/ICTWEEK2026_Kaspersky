num = int(input("Enter the number of rows:"))
for i in range(num):
    string = ""
    for j in range(i+ 1):
        string += str(i + 1) + " "
    
    print(string)
