#Sum upto N numbers

#input= n , output = 1+2+3+4+5 = 15

def sum1(n):
    return (n)*(n+1)//2

def sum2(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    return sum

n = int(input("Enter your number"))

print("Result from sum1 {}".format(sum1(n)))
print("Result from sum2 {}".format(sum2(n)))
