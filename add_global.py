Var = 42
def add(num):
      return(num  + Var) 

def main():

    number = input("Provide a number:")
    number = add(10)

    print("Sum:", number ,"is a whole number")

if __name__ == "__main__":
        main()