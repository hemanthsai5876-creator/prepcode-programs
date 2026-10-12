count=int(input("enter the number"))
output=[]
for i in range(1,count+1):
    if 1%3==0:
        if i%5==0:
            output.append("FIZZBUZZ")
        else:
            output.append("FUZZ")
    elif i%5==0:
        output.append("BUZZ")
    else:
            ouput.append(i)
print(output)