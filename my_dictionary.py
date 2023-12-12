def display_menu():
    menu_dict = {
        '1':'Apples',
        '2':'Pears',
        '3':'Bananas',
    }
    for items, values in menu_dict.items():
        print(items+"."+values)

def main():
    display_menu()


if __name__ == "__main__":
    main()  