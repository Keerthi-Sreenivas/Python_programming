# Product of numbers a*b  = lcm*gcd
# Time Complexity = O(log(min(a,b)))

def gcd(a,b):
    if a == 0:
        return b
    return gcd(b%a,a)

def lcm(a,b):
    prod = a*b
    hcf = gcd(a,b)
    return prod//hcf

a,b = map(int,input("Enter your numbers: ").split()) #enter with space ex: 3 12
print("GCD of the numbers: {}, LCM of the numbers: {}".format(gcd(a,b),lcm(a,b)))

    
