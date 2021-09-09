"""
------------------------------------------------------
Euclidean Algorithm for LCM

(c) 2018 Julie Co, Manila, Philippines
Coursera Algorithmic Toolbox - UC San Diego & HSE
Week 2 - Algorthmic Warmup - Least Common Multiple
------------------------------------------------------
"""

# Recursive Euclidean Algorithm


def gcd(a, b):
    if(a % b == 0):
        return b
    else:
        return gcd(b, a % b)


# Derive LCM from GCD

def lcm(a, b):
    return int(a*b/gcd(a, b))


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(lcm(max(a, b), min(a, b)))
