"""
------------------------------------------------------------------------
Last Digit - Sum of n Fibonacci Numbers

(c) 2018 Julie Co, Manila, Philippines
Coursera Algorithmic Toolbox - UC San Diego & HSE
Week 2 - Algorthmic Warmup - Last Digit of the Sum of Fibonacci Numbers
------------------------------------------------------------------------
"""

# Iterative Fibonacci Number Summation -- Last Digit


def sum_fib(n):

    prev = 0
    curr = 1

    # Initialize Fibonacci memo. Fibonacci last digit is expected to repeat a pattern after n indices
    pattern = []

    # Memoize the (Fib_n, Fib_(n+1)). Once the first pair (0,1) appears after some n terms, the cycle is complete.
    pattern.append((0, 1))

    ##print("{}: {}".format(0, pattern[-1]))

    for i in range(n):

        temp = curr
        curr = (curr + prev) % 10
        prev = temp % 10

        if (prev, curr) in pattern:     # Stop memoization after a Fibonacci pair repeats in the memo

            # Index of the last digit of the nth Fibonacci term.
            index = n % len(pattern)

            # Number of cycle repetition for n terms
            multiplier = int(n/len(pattern))

            # Sum of last digits of n Fib terms
            sums = (multiplier * sum([x for (x, y) in pattern]) +
                    sum([x for (x, y) in pattern[0:index+1]])) % 10

            return sums

        else:

            # Append Fibonacci pair while cycle is not complete
            pattern.append((prev, curr))

        ##print("{}: {}".format(i+1, pattern[-1]))

    # In pair (a,b) for index n, a is always the las digit of the nth Fibonacci term. b is for the (n+1)th term.
    return sum([x for (x, y) in pattern]) % 10


if __name__ == '__main__':
    n = int(input())
    print(sum_fib(n))
