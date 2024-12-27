def celsius_to_fahrenheit(celsius):
    # fahrenheit = (9/5 * celsius) + 32
    fahrenheit = (9 * celsius / 5) + 32
    return fahrenheit
def fahrenheit_to_celsius(fahrenheit):
    # celsius = (fahrenheit - 32) * 5/9
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius
def celsius_to_kelvin(celsius):
    # kelvin = 273.15 + celsius
    kelvin = 273.15 + celsius
    return kelvin
def kelvin_to_celsius(kelvin):
    # celsius = kelvin - 273.15
    celsius = kelvin - 273.15
    return celsius

def get_temperature_input(prompt):
    """Get valid temperature input from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def continue_exit():
    while True:
        continue_or_end = input("Do you want to continue[Y|N]? ")

        if continue_or_end.capitalize() == "N":
            print("Thanks for trying my code.")
            return False
        elif continue_or_end.capitalize() == "Y":
            return True
        else:
            print("Invalid choice. Please enter 'Y' or 'N'.")

def main():
    # This is main function.
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit.")
    print("2. Fahrenheit to Celsius.")
    print("3. Celsius to Kelvin.")
    print("4. Kelvin to Celsius.")
    print("5. Exit")

    bool = True
    while bool:
        # Enter what you want to do? [1|2|3|4|5]
        choice = input("Enter Your Choice[1|2|3|4|5]: ")

        if choice == "1":
            # Celsius =======> Fahrenheit
            celsius = get_temperature_input("Enter temperature in Celsius: ")
            CTF = celsius_to_fahrenheit(celsius)
            print(f"Celsius: {celsius:.2f} ====> Fahrenheit: {CTF:.2f}")

        elif choice == "2":
            # Fahrenheit =======> Celsius
            fahrenheit = get_temperature_input("Enter temperature in Fahrenheit: ")
            FTC = fahrenheit_to_celsius(fahrenheit)
            print(f"Fahrenheit: {fahrenheit:.2f} ====> Celsius: {FTC:.2f}")

        elif choice == "3":
            # Celsius =======> Kelvin
            celsius = get_temperature_input("Enter temperature in Celsius: ")
            CTK = celsius_to_kelvin(celsius)
            print(f"Celsius: {celsius:.2f} ====> Kelvin: {CTK:.2f}")

        elif choice == "4":
            # Kelvin =======> Celsius
            kelvin = get_temperature_input("Enter temperature in Kelvin: ")
            KTC = kelvin_to_celsius(kelvin)
            print(f"Kelvin: {kelvin:.2f} ====> Celsius: {KTC:.2f}")

        elif choice == "5":
            print("Thanks for using the Temperature Converter. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5..")
            continue

        bool = continue_exit()


if __name__ == "__main__":
    main()