def decimal_to_binary(decimal):
    return bin(decimal).replace("0b", "")

def binary_to_decimal(binary):
    return int(binary, 2)

def main():
    print("Welcome to the Binary Conversion Calculator!")

    while True:
        print("\nMenu:")
        print("1. Convert Binary to Decimal")
        print("2. Convert Decimal to Binary")
        print("3. Quit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            binary_input = input("Enter a binary number: ")
            if all(bit in "01" for bit in binary_input):
                decimal_result = binary_to_decimal(binary_input)
                print(f"The decimal equivalent of {binary_input} is {decimal_result}.")
            else:
                print("Invalid binary input. Please enter a valid binary number.")
        elif choice == "2":
            try:
                decimal_input = int(input("Enter a decimal number: "))
                if decimal_input >= 0:
                    binary_result = decimal_to_binary(decimal_input)
                    print(f"The binary equivalent of {decimal_input} is {binary_result}.")
                else:
                    print("Invalid decimal input. Please enter a non-negative integer.")
            except ValueError:
                print("Invalid decimal input. Please enter a valid integer.")
        elif choice == "3":
            print("Thank you for using the Binary Conversion Calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
