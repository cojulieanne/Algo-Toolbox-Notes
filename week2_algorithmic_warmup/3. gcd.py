"""
------------------------------------------------------
Euclidean Algorithm

(c) 2018 Julie Co, Manila, Philippines
Coursera Algorithmic Toolbox - UC San Diego & HSE
Week 2 - Algorthmic Warmup - Greatest Common Divisor
------------------------------------------------------
"""

# Recursive Euclidean Algorithm


def gcd(a, b):
    if(a % b == 0):
        return b
    else:
        return gcd(b, a % b)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(max(a, b), min(a, b)))
