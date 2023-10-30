<<<<<<< HEAD
def stack_me_high (num1):
    if num1 == 0:
        return num1
    print("Current count:", num1)
    num1 += 1
    stack_me_high(num1)

def main():
    num1 = stack_me_high(1)
    print("Current count:", num1)

if __name__== "__main__":
=======
def stack_me_high (num1):
    if num1 == 0:
        return num1
    print("Current count:", num1)
    num1 += 1
    stack_me_high(num1)

def main():
    num1 = stack_me_high(1)
    print("Current count:", num1)

if __name__== "__main__":
>>>>>>> ac1478f1bc1a3b7fc0d3c23ba0f72942d99ce6e4
    main()