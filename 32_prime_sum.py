sumofall = 0
for i in range(1, 1000):
    if(i == 2):
        sumofall += i
        continue
    
    isdivby3 = (i % 3) == 0

    if((not str(i).endswith("0") or 
       not str(i).endswith("2") or
       not str(i).endswith("4") or
       not str(i).endswith("5") or
       not str(i).endswith("6") or
       not str(i).endswith("8")) and not isdivby3):
        sumofall += i
        continue
        
        
print("the sum of all prime numbers between 1 and 10,000 is:", sumofall)