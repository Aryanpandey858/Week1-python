"""Temperature Converter: Celsius <-> Fahrenheit using functions."""


def c_to_f(celsius):
    return (celsius * 9 / 5) + 32


def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def main():
    print("=== Temperature Converter ===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Choose an option (1/2): ").strip()

    if choice not in ("1", "2"):
        print("Invalid choice. Please run the program again.")
        return

    try:
        value = float(input("Enter the temperature: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if choice == "1":
        print(f"{value}°C = {c_to_f(value):.2f}°F")
    else:
        print(f"{value}°F = {f_to_c(value):.2f}°C")


if __name__ == "__main__":
    main()