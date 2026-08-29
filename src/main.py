from datetime import date

from utils import add, subtract


def main():
    print("Name: Samiul Islam Siam")
    print("Date:", date.today())

    print("add(10, 5) =", add(10, 5))
    print("subtract(10, 5) =", subtract(10, 5))


if __name__ == "__main__":
    main()
