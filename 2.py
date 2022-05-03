def maximum(num1,num2,num3):
    if(num1>num2 and num1>num3):
        return num1
    
    elif(num2>num3 and num2>num1):
        return num2
    
    else:
        return num3

m = maximum(10,30,20)
print("The value of the maximum is"+str(m))