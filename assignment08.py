# Add
a=0
for num in range(1,11):
    a=num+a
    print(a,end=' ')


#multiplication table

Num = int(input("Enter the number you want to generate a multiplication table for, then hit the `enter` key: "))
Range = range(1,11)
for x in Range:
    result = Num * x
    print(Num," * ",x," = ",result)
