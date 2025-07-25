num=int(input("Enter any number"))
square=0
i=num
rem=0
while i>0:
    rem=i%10
    square = square + rem ** 3
    i = i//10
if square == num:
    print(f"{num} is an armstrong number")
else:
    print(f"{num} is not an armstrong number")

    
    

