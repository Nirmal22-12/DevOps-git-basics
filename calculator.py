"""Basic Calculator Module."""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return the quotient of a and b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def power(a, b):
    """Return a raised to the power of b."""
    return a**b


def modulus(a, b):
    """Return the remainder of a divided by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot perform modulus by zero.")
    return a % b


def get_number(prompt):
    """Prompt the user for a valid numeric input."""
    while True:
        try:
            val = float(input(prompt))
            return int(val) if val.is_integer() else val
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def main():
    """Interactive command-line interface for the calculator."""
    print("====================================")
    print("        Python Calculator           ")
    print("====================================")

    while True:
        print("\nSelect operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Power (^)")
        print("6. Modulus (%)")
        print("7. Exit")

        choice = input("Enter choice (1-7): ").strip()

        if choice == "7":
            print("Thank you for using Python Calculator. Goodbye!")
            break

        if choice not in ("1", "2", "3", "4", "5", "6"):
            print("Invalid choice! Please select between 1 and 7.")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        try:
            if choice == "1":
                result = add(num1, num2)
                op = "+"
            elif choice == "2":
                result = subtract(num1, num2)
                op = "-"
            elif choice == "3":
                result = multiply(num1, num2)
                op = "*"
            elif choice == "4":
                result = divide(num1, num2)
                op = "/"
            elif choice == "5":
                result = power(num1, num2)
                op = "^"
            elif choice == "6":
                result = modulus(num1, num2)
                op = "%"

            if isinstance(result, float) and result.is_integer():
                result = int(result)

            print(f"\nResult: {num1} {op} {num2} = {result}")

        except ValueError as e:
            print(f"\nError: {e}")


if __name__ == "__main__":
    main()
