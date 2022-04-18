# Author: Viernes, Michael
# Date: 04-08-2022
# Objective: Create a fibonacci sequence by trying different approaches (recursion, memoization, loop)

# 1st Approach: Recursion
def fibonacci_recursion(n):
    """
    params: n - the range of sequence
    returns: a list of fibonacci sequence
    """
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    else:
        return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

# 2nd Approach Memoization
def fibonacci_memoization(n):
    """
        params: n - the range of sequence
        returns: a list of fibonacci sequence
    """
    
    pass
    
        
# Main Program
if __name__ == "__main__":
    while True:
        try:
            print("FIBONACCI SEQUENCE".rjust(15, "*"))
            num = int(input("Type the position of fibonacci: "))
            # display list and sum of fibonacci
            fib = [(fibonacci_recursion(i)) for i in range(num)]
            print("The sum of {} fibonacci sequence is {}".format(num, sum(fib)))
            print(f"While the list of {num} fibonacci sequence are :\n{fib}")
        except ValueError as ve:
            print("Please type a number.")
            pass
