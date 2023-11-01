def meal_test(answer):
    if answer == int(1):
        print("Fried Chicken Yummy!")
    elif answer == int(2):
        print("Burger!")
    elif answer == int(3):
        print("Pizza!")
    else:
        print("This is not an option!")
    
def main ():
        print("Which is your favorite meal?")
        print("1.Chicken")
        print("2.Burger")
        print("3.Pizza")        
        answer = int(input())
        meal_test(answer)
    
if __name__ == "__main__":
        main()

