def decimal_to_binary(decimal):
    binary_result = ""
    while decimal > 0:
        remainder = decimal % 2
        binary_result = str(remainder) + binary_result
        decimal = decimal // 2
    return binary_result if binary_result else "0"


def binary_to_decimal(binary):
    decimal_result = 0
    binary = binary[::-1]
    for i in range(len(binary)):
        if binary[i] == '1':
            decimal_result += 2 ** i
    return decimal_result


def decimal_to_hexadecimal(decimal):
    hexadecimal_digits = "0123456789ABCDEF"
    hexadecimal_result = ""
    while decimal > 0:
        remainder = decimal % 16
        hexadecimal_result = hexadecimal_digits[remainder] + hexadecimal_result
        decimal = decimal // 16
    return hexadecimal_result if hexadecimal_result else "0"


def hexadecimal_to_decimal(hexadecimal):
    hexadecimal_digits = "0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F"
    decimal_result = 0
    hexadecimal = hexadecimal.upper()
    for i in range(len(hexadecimal)):
        digit = hexadecimal_digits.index(hexadecimal[i])
        decimal_result = decimal_result * 16 + digit
    return decimal_result


def hexadecimal_to_binary(hexadecimal):
    binary_result = ""
    hexadecimal_digits = "0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F"
    for char in hexadecimal:
        binary_result += format(hexadecimal_digits.index(char), '04b')
    return binary_result


def binary_to_hexadecimal(binary):
    hexadecimal_result = hex(int(binary, 2))[2:]
    return hexadecimal_result.upper()


def octal_to_decimal(octal):
    decimal_result = 0
    octal = octal[::-1]
    for i in range(len(octal)):
        decimal_result += int(octal[i]) * 8 ** i
    return decimal_result


def decimal_to_octal(decimal):
    octal_result = ""
    while decimal > 0:
        remainder = decimal % 8
        octal_result = str(remainder) + octal_result
        decimal = decimal // 8
    return octal_result if octal_result else "0"


def main():
    print("Welcome to the Conversion Calculator!")

    while True:
        print("\nMenu:")
        print("1. Convert Binary to Decimal")
        print("2. Convert Decimal to Binary")
        print("3. Convert Hexadecimal to Decimal")
        print("4. Convert Decimal to Hexadecimal")
        print("5. Convert Hexadecimal to Binary")
        print("6. Convert Binary to Hexadecimal")
        print("7. Convert Octal to Decimal")
        print("8. Convert Decimal to Octal")
        print("9. Quit")

        choice = input("Enter your choice (1-9): ")

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
            hexadecimal_input = input("Enter a hexadecimal number: ")
            if all(char.upper() in "0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F" for char in hexadecimal_input):
                decimal_result = hexadecimal_to_decimal(hexadecimal_input)
                print(f"The decimal equivalent of {hexadecimal_input} is {decimal_result}.")
            else:
                print("Invalid hexadecimal input. Please enter a valid hexadecimal number.")
        elif choice == "4":
            try:
                decimal_input = int(input("Enter a decimal number: "))
                if decimal_input >= 0:
                    hexadecimal_result = decimal_to_hexadecimal(decimal_input)
                    print(f"The hexadecimal equivalent of {decimal_input} is {hexadecimal_result}.")
                else:
                    print("Invalid decimal input. Please enter a non-negative integer.")
            except ValueError:
                print("Invalid decimal input. Please enter a valid integer.")
        elif choice == "5":
            hexadecimal_input = input("Enter a hexadecimal number: ")
            if all(char.upper() in "0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F" for char in hexadecimal_input):
                binary_result = hexadecimal_to_binary(hexadecimal_input)
                print(f"The binary equivalent of {hexadecimal_input} is {binary_result}.")
            else:
                print("Invalid hexadecimal input. Please enter a valid hexadecimal number.")
        elif choice == "6":
            binary_input = input("Enter a binary number: ")
            if all(bit in "01" for bit in binary_input):
                hexadecimal_result = binary_to_hexadecimal(binary_input)
                print(f"The hexadecimal equivalent of {binary_input} is {hexadecimal_result}.")
            else:
                print("Invalid binary input. Please enter a valid binary number.")
        elif choice == "7":
            octal_input = input("Enter an octal number: ")
            if all(oct_digit in "0,1,2,3,4,5,6,7" for oct_digit in octal_input):
                decimal_result = octal_to_decimal(octal_input)
                print(f"The decimal equivalent of {octal_input} is {decimal_result}.")
            else:
                print("Invalid octal input. Please enter a valid octal number.")
        elif choice == "8":
            try:
                decimal_input = int(input("Enter a decimal number: "))
                if decimal_input >= 0:
                    octal_result = decimal_to_octal(decimal_input)
                    print(f"The octal equivalent of {decimal_input} is {octal_result}.")
                else:
                    print("Invalid decimal input. Please enter a non-negative integer.")
            except ValueError:
                print("Invalid decimal input. Please enter a valid integer.")
        elif choice == "9":
            print("Thank you for using the Conversion Calculator. Goodbye!")
            break
        else:
            input("Invalid choice. Please enter a number from 1 to 9.")

if __name__ == "__main__":
    main()