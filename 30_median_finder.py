# Enter an odd number of integers separated by spaces: 20 29 303 919 30
# Sorted list: [20, 29, 30, 303, 919]
# The number in the middle (index 2) is: 30
l = input("Enter an odd number of integers separated by spaces:").strip().split(" ")

l.sort()
print("Sorted list:", l)
mid = (len(l) - 1) / 2
print("The number in the middle (index "+str(int(mid))+") is:", l[int(mid)])

