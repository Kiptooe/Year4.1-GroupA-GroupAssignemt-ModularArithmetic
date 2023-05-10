def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_gcd(b, a % b)
        return gcd, y, x - (a // b) * y

p = 26513
q = 32321

gcd, u, v = extended_gcd(p, q)

print(f"gcd: {gcd}, u: {u}, v: {v}")
