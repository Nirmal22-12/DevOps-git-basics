# Python Calculator

A lightweight, interactive command-line calculator written in Python. This script provides basic and extended arithmetic functions both as an interactive CLI application and as an importable Python module.

## Features

- **Basic Arithmetic**: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`)
- **Advanced Operations**: Power (`^`), Modulus (`%`)
- **Robust Error Handling**:
  - Safe handling of division and modulus by zero with informative errors.
  - Input validation to gracefully handle non-numeric inputs.
- **Clean Formatting**: Displays integer results cleanly without trailing decimals (e.g., `15` instead of `15.0`).

## Prerequisites

- Python 3.6 or higher

## Getting Started

### 1. Interactive CLI Mode

Run the calculator directly from your terminal:

```bash
python calculator.py
```

#### Example Usage

```text
====================================
        Python Calculator           
====================================

Select operation:
1. Add (+)
2. Subtract (-)
3. Multiply (*)
4. Divide (/)
5. Power (^)
6. Modulus (%)
7. Exit
Enter choice (1-7): 1
Enter first number: 10
Enter second number: 5

Result: 10 + 5 = 15
```

### 2. Module Import Usage

You can also import `calculator.py` into your Python scripts:

```python
import calculator

print(calculator.add(10, 5))         # Output: 15
print(calculator.subtract(10, 4))    # Output: 6
print(calculator.multiply(3, 4))     # Output: 12
print(calculator.divide(20, 5))      # Output: 4.0
print(calculator.power(2, 3))        # Output: 8
print(calculator.modulus(10, 3))     # Output: 1
```

## Available Functions

| Function | Signature | Description |
| :--- | :--- | :--- |
| `add` | `add(a, b)` | Returns `a + b` |
| `subtract` | `subtract(a, b)` | Returns `a - b` |
| `multiply` | `multiply(a, b)` | Returns `a * b` |
| `divide` | `divide(a, b)` | Returns `a / b` (Raises `ValueError` if `b == 0`) |
| `power` | `power(a, b)` | Returns `a ** b` |
| `modulus` | `modulus(a, b)` | Returns `a % b` (Raises `ValueError` if `b == 0`) |