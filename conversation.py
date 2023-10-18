def conversation():
    print("Welcome to my conversation")
    print("Do you like coding?")
    print("Answer yes or no")

    answer = input("")
    if answer.lower() == "yes":
        print("That's good")
    elif answer.lower() == "no":
        print("That's too bad!")
    print("Thanks for talking with me")
def main():
    conversation()

if __name__=="__main__":
    main()