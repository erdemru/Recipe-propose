recipe_book = open('recipes.txt','r') #recipes book, should be in the same directory with the py file
print("Hello! Are you starving? I am here for you:)") #welcome, only one time
def main_menu(): #main menu, we want to go back to this list to keep the user in the software
    go_back = True
    while go_back == True:
        print("\n 1. I want to enter the ingredients to find a recipe "
              "\n 2. I want to see all the recipes."
              "\n 3. I want to look for the main course recipes."
              "\n 4. I want to look for the dessert course recipes."
              "\n 5. Quit")
        try:
            the_choice = int(input("Choose your purpose (1,2,3,4,5): "))
            return(the_choice)
            break
        except ValueError:
            print("please enter a number")
            continue

def desserts():
    for line in recipe_book:
        line = line.strip()
        if line.find('dessert') == -1:continue #this is to continue the loop (find modulunde eger aranan bulunmazsa deger -1 olarak doner)
        #print(line) #this prints our options
        print(line[0:(line.find(':'))]) #this is to remive to colons

def main_course():
    for line in recipe_book:
        line = line.strip()
        if line.find('main') == -1:continue
        print(line[0:(line.find(':'))])

def dish_name():
    for line in recipe_book:
        line = line.strip()
        if line.find(':') == -1:continue #all of the dishnames in the recipe book has ':'
        print(line[0:(line.find(':'))])



option = main_menu()


if option == 1: #list the ingredients
    print('ahah')
if option == 2: #list the recipes
    dish_name()
if option == 3: #list main courses
    main_course()
if option == 4: #list desserts
    desserts()
if option == 5: #quit
    print('Goodbye.')
    quit()
