N = int(input("Enter the value of N:"))

print(str(N / 3), not str(N / 3).startswith("0."))

for n in range(N):
    n += 1
    divide3 = str(n / 3)
    divide5 = str(n / 5)

    isfizz = False
    isbuzz = False

    if(not divide3.startswith("0.") and divide3.endswith(".0")):
        isfizz = True
    if(not divide5.startswith("0.") and divide5.endswith(".0")):
        isbuzz = True

    if(isfizz and isbuzz):
        print("FizzBuzz")
    elif(isfizz):
        print("Fizz")
    elif(isbuzz):
        print("Buzz")
    else:
        print(n)

    