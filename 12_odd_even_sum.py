l = input("Enter a list of numbers separated by spaces:").strip().split(" ")
print("List:", l)
print("-------------------")

oddsum = 0
evensum = 0

for n in l:
    n = int(n)
    mod = n % 2

    if(mod == 0):
        oddsum += n
    elif(mod == 1):
        evensum += n

print("Sum of even numbers:", evensum)
print("Sum of odd numbers:", oddsum)