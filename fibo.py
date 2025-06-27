def fibonacci_recursive(n):
    """
    Calculates the nth Fibonacci number using recursion.

    Args:
        n: The index of the Fibonacci number to calculate (non-negative integer).

    Returns:
        The nth Fibonacci number.
    """
    if n <= 1:  # Base cases for F(0) and F(1)
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example usage:
# print(fibonacci_recursive(0))  # Output: 0
# print(fibonacci_recursive(1))  # Output: 1
# print(fibonacci_recursive(2))  # Output: 1
# print(fibonacci_recursive(7))  # Output: 13
