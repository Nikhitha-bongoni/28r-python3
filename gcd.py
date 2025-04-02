def find_gcd(a, b):
    while b:
        a, b = b, a % b  
    return a

a = 12
b = 18
print("GCD:", find_gcd(a, b))
