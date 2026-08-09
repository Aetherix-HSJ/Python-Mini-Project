n = int(input("enter a number: "))
eSum = 0
oSum = 0
for i in range (n+1):
    if(i%2==0): eSum +=i
    else: oSum+=i
print(f"even sum in range is {eSum} and odd sum in range is {oSum}")    