def user_selection(answer):
    if answer == int(1):
        print("Good intuition!")
    elif answer == int(2):
        print("Hum...")
    elif answer == int(3):
        print("Best answer!")
    elif answer == int(4):
        print("Thank you and goodbye!!") 
        
    else:
        print("This is not an option!Please choose from 1 to 4")
        
           

def main():
     print("Welcome!")
        
     while True:
         print("If you were attacked what will you do?")
         print("1.Run")
         print("2.Fight")
         print("3.Run, hide and then call the police") 
         print("4.I don't want to answer,Quit")       
         answer = int(input())
         user_selection(answer)
          
       
    


if __name__ == "__main__":
    main()