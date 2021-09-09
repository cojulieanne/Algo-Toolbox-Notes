"""
----------------------------------------------------------------------------------
Sum of Squares of Fibonacci Numbers 

(c) 2018 Julie Co, Manila, Philippines
Coursera Algorithmic Toolbox - UC San Diego & HSE
Week 2 - Algorthmic Warmup - Last Digit of the Sum of Squares of Fibonacci Numbers
----------------------------------------------------------------------------------
"""

# Iterative Fibonacci Numbers Sum of Squares


def sum_fib(n):

    prev = 0
    curr = 1

    # Initialize Fibonacci memo. Fibonacci last digit is expected to repeat a pattern after n indices
    pattern = []

    # Memoize the (Fib_n, Fib_(n+1), Fib_n**2, Fib_(n+1)**2).
    # Once the first pair (0,1,0,1) appears after some n terms, the cycle is complete.
    pattern.append((0, 1, 0, 1))

    #print("{}: {}, {}".format(0, pattern[-1], pattern[-1][0]**2))

    for i in range(n):

        temp = curr
        curr = (curr + prev) % 10
        prev = temp % 10

        # Stop memoization after a Fibonacci pair repeats in the memo
        if (prev, curr, prev**2, curr**2) in pattern:

            # Index of the last digit of the nth Fibonacci term.
            index = n % len(pattern)

            multiplier = int(n/len(pattern))  # Number of cycles

            # Sum of squares of last digit of n Fibonacci terms
            sums = (multiplier * sum([a for (x, y, a, b) in pattern]) +
                    sum([a for (x, y, a, b) in pattern[0:index+1]])) % 10

            return sums

        else:
            # Append Fibonacci pair (x,y, x**2, y**2) while cycle is not complete
            pattern.append((prev, curr, prev**2, curr**2))

        #print("{}: {}, {}".format(i+1, pattern[-1], pattern[-1][0]**2))

    # In pair (x,y,a,b) for index n, x is always the last digit of the nth Fibonacci term. b is for the (n+1)th term
    # a is the square of the last digit of nth term
    return sum([a for (x, y, a, b) in pattern]) % 10


if __name__ == '__main__':
    n = int(input())
    print(sum_fib(n))
