def get_prime_place(target):
    prime_count = 0

    for i in range(1, 10000):
        if(i == 2):
            prime_count += 1
            if(prime_count == target):
                return i
            continue
        
        isdivby3 = (i % 3) == 0

        if((not str(i).endswith("0") or 
        not str(i).endswith("2") or
        not str(i).endswith("4") or
        not str(i).endswith("5") or
        not str(i).endswith("6") or
        not str(i).endswith("8")) and not isdivby3):
            prime_count += 1
            if(prime_count == target):
                return i
            continue

print("the 500th prime number", get_prime_place(500))
print("the 750th prime number", get_prime_place(750))
print("the 150th prime number", get_prime_place(150))