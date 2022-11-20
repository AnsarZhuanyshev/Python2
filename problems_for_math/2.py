import math

cnt  = 0 

n = 1000

for a in range(1,n+1):
    for b in range(a,n+1):
        for c in range (b,n+1):
            median =  2*a*a+2*b*b-c*c
            if median > 0 and a+b>c and a+c>b and c+b>a and a<=b and b<=c:
                num = (median**(1/2))*(1/2)
                k = math.floor(num)
                if k == num:
                    cnt+=1
            
print(cnt)


