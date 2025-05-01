import re

def factorial_recursive(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be a non-negative number")
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

def fibonacci_recursive(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be a non-negative number")
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def sum_list_recursive(lst: list) -> int:
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    if not all(isinstance(x, (int, float)) for x in lst):
        raise TypeError("All elements of the list must be numbers")
    if not lst:
        return 0
    else:
        return lst[0] + sum_list_recursive(lst[1:])

def is_palindrome_recursive(text: str) -> bool:
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    text = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    if len(text) <= 1:
        return True
    elif text[0] != text[-1]:
        return False
    else:
        return is_palindrome_recursive(text[1:-1])

if __name__ == '__main__':
    # Testing factorial_recursive
    print("Testing factorial_recursive:")
    try:
        print(f"Factorial of 5: {factorial_recursive(5)}")
        print(f"Factorial of 0: {factorial_recursive(0)}")
        factorial_recursive(-1)
    except Exception as e:
        print(f"An error occurred: {e}")

    # Testing fibonacci_recursive
    print("\nTesting fibonacci_recursive:")
    try:
        print(f"5th Fibonacci number: {fibonacci_recursive(5)}")
        print(f"0th Fibonacci number: {fibonacci_recursive(0)}")
        fibonacci_recursive(-1)
    except Exception as e:
        print(f"An error occurred: {e}")

    # Testing sum_list_recursive
    print("\nTesting sum_list_recursive:")
    try:
        print(f"Sum of [1, 2, 3, 4, 5]: {sum_list_recursive([1, 2, 3, 4, 5])}")
        print(f"Sum of []: {sum_list_recursive([])}")
        sum_list_recursive([1, 2, "a"])
    except Exception as e:
        print(f"An error occurred: {e}")

    # Testing is_palindrome_recursive
    print("\nTesting is_palindrome_recursive:")
    try:
        print(f"\"racecar\" is a palindrome: {is_palindrome_recursive('racecar')}")
        print(f"\"A man, a plan, a canal: Panama\" is a palindrome: {is_palindrome_recursive('A man, a plan, a canal: Panama')}")
        print(f"\"hello\" is a palindrome: {is_palindrome_recursive('hello')}")
        is_palindrome_recursive(123)
    except Exception as e:
        print(f"An error occurred: {e}")
