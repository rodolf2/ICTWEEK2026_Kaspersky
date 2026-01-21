l = input("Enter the temperatures for 7 days (separated by spaces):").strip().split(" ")
print(l)

total = 0
for num in l:
    total += int(num)

average = total / len(l)
average = "%.2f" % average

print("Average Temperature:", average + "°")

days_hotter = 0

for num in l:
    inum = float(num)
    if(inum > float(average)):
        days_hotter += 1

print("Number of days hotter than average:", days_hotter)
