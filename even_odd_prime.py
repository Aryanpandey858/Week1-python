"""Even/Odd & Prime Number Checker."""
import math


def is_even(n):
    return n % 2 == 0


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def main():
    print("=== Even/Odd & Prime Number Checker ===")
    while True:
        try:
            n = int(input("\nEnter an integer (0 to quit): "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if n == 0:
            print("Goodbye!")
            break

        print(f"{n} is {'Even' if is_even(n) else 'Odd'}.")
        print(f"{n} is {'a Prime number' if is_prime(n) else 'NOT a Prime number'}.")


if __name__ == "__main__":
    main()