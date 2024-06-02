# Highest common factor
# greatest common devisor

def HCF(num1,num2):
    if num1 > num2:
        smaller = num2
    else:
        smaller = num1
    
    for i in range(1, smaller+1):
        if (num1 % i == 0) and (num2 % i == 0):
            hcf = i
    return hcf
            
print(f"hcf of number is: ", HCF(num1= 12,num2=30))
