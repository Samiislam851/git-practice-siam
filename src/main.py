from datetime import date

from utils import add, divide, multiply, subtract


def show(label, operation, a, b):
    """Run one calculator operation and report the result or the error."""
    try:
        print(f"{label}({a}, {b}) =", operation(a, b))
    except (TypeError, ZeroDivisionError) as error:
        print(f"{label}({a}, {b}) failed:", error)


def main():
    print("Name: Samiul Islam Siam")
    print("Date:", date.today())

    show("add", add, 10, 5)
    show("subtract", subtract, 10, 5)
    show("multiply", multiply, 10, 5)
    show("divide", divide, 10, 5)

    # These two demonstrate the error handling.
    show("divide", divide, 10, 0)
    show("add", add, 10, "five")


if __name__ == "__main__":
    main()
