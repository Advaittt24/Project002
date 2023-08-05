# Add
a=0
start = int(input('Enter starting range = '))
end = int(input('Enter ending renge = '))
for num in range(start,end+1):
    a=num+a
    print(a,end=' ')


#multiplication table

Num = int(input("Enter a number "))
for x in range(1,10+1):
    result = Num * x
    print(Num," * ",x," = ",result)


#counting alphabets 
mum=0
name=str(input('Enter a word '))
for a in name:
    mum = mum+1
    print("Your total number of wrods is ",mum )


#counting number
b=0
sum = str(input("Enter Numbers "))
for l in sum :
    b= b +1 
print('total no. are = ',b)


#reverse number
no = int(input("Enter Numbers = "))
print(str(no)[::-1])