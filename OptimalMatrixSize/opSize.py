import math

print("Enter number of variables in matrix: ")
n = int(input())

a = int(math.sqrt(n))+1
while(a >= 1):
    if(n%a==0):
        b = n//a
		if b>a:
			a,b = b,a
        print("Optimal Matrix Dimensions are: ",a," X ",b)
        break
    else:
        a -= 1
