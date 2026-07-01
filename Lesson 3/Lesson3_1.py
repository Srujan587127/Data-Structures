# Fibonacci using Recursion


def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    

for i in range(7):
    print(fibonacci(i))

# Factorial using Recursion 


def factorial(n):
    if n == 1:
        print("Reached base Case")
        return 1
    
    else:
        print("Calling Factorial(", n - 1, ")")
        return n * factorial(n - 1)
    

print(factorial(5))

# sum of numbers till n using recursion


def sumofnumbers(n):
    print("Calling sumofnumber(", n, ")")

    if n == 0 or n == 1:
        print("Base Case reached ")
        return n
    else:
        result = n + sumofnumbers(n - 1)
        print("Returning ", result, "for n = ", n)
        return result
    

print("Final Answer: ", sumofnumbers(5))


# Power function using Recursion


def Power(x, y):
    print("Calling Power (", x, ",", y, ")")

    if y == 1:
        print("Base case reached. ")
        return x
    else:
        half = Power(x, y // 2)

        if y % 2 == 0:
            result = half * half
            return result
        else:
            result = x * half * half
            return result
        

print("Final Answer: ", Power(3, 5))