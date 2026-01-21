num = float(input("Enter the numeric score(0-100): "))
print("Numeric Score:", num)
converted = 0
if(num >= 98):
    converted = 1.0
elif(num >= 95):
    converted = 1.25
elif(num >= 92):
    converted = 1.50
elif(num >= 89):
    converted = 1.75


print("Converted Grade:", converted)