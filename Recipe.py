recipe1 = {"dish": "Meatball", "ing1": "mince", "ing2": "oil", "qua1": 500, "qua2": 50, "cal": 196,
           "rec": "\n-Roll the mince and make it round.\n-Pour 50 gr oil into a non-stick skillet and heat over "
                  "medium heat.\n-Cook meatballs until golden brown on bottom, about 4 – 6 minutes. \n-Then rotate to "
                  "opposite side and cook opposite side until golden brown.\n-Transfer to paper towels to drain "
                  "\n-Enjoy!\n"}
recipe2 = {"dish": "Macaroni", "ing1": "pasta", "ing2": "cheese", "qua1": 250, "qua2": 25, "cal": 371,
           "rec": "\n-Cook your pasta in a large pot of salted boiling water according to the package directions."
                  "\n-After the pasta is cooked add the cheese into it and mix until the cheese thoroughly coats it."
                  "\n-Enjoy! \n"}
recipe3 = {"dish": "Steak", "ing1": "meat", "ing2": "margarine", "qua1": 200, "qua2": 10, "cal": 270,
           "rec": "\n-Season the meat \n-Place cast iron skillet on a burner set to high heat and allow to warm up "
                  "\n-Place steak inside hot skillet \n-After 2 minutes,turn over steak. "
                  "\n-Top steak with margarine; move to grill or oven. \n-Enjoy! \n"}
recipe4 = {"dish": "Brownie", "ing1": "dark chocolate", "ing2": "sugar",
           "ing3": "flour", "qua1": 100, "qua2": 10, "qua3": 200, "cal": 466,
           "rec": "\n-Mix together the flour, water, sugar and dark chocolate that you melt before, make a batter "
                  "\n-Then, pour the batter into an baking pan  \n-Transfer the pan to a 325-degree oven and bake "
                  "for 40 to 45 minutes\n-Allow the brownies to cool completely before slicing and serving.\n-Enjoy!\n"}
recipe5 = {"dish": "Cake", "ing1": "flour", "ing2": "egg", "qua1": 300, "qua2": 3, "cal": 251,
           "rec": "\nMix together the flour and egg \n-Pour the batter into a cake mold when it's be homogeneous "
                  "\n-Transfer the mold to a 325-degree oven and bake for 30-35 minutes \n-Allow the cake to cool "
                  "completely before slicing and serving. \n-Enjoy! \n"}
recipe6 = {"dish": "Cheesecake", "ing1": "cream cheese", "ing2": "lemon sauce", "qua1": 400, "qua2": 4, "cal": 321,
           "rec": "\n-Get a base with cream cheese \n-Transfer the mold to a 325-degree oven and bake for 15 minutes "
                  "\n-Allow to cool \n-Then pour the lemon sauce to cover the mold. \n-Enjoy! \n"}


def recipe(a, b, c, d, e, f, g, h, i):
    x = d * unit - quantity1
    y = e * unit - quantity2
    z = f * unit - quantity3
    if x <= 0 and y <= 0 and z <= 0:
        print("\nYou can make", g, "with", unit * d, "gr", a, unit * e, "gr", b,
              "and", f*unit, "gr/unit", c, "for", unit, "person.\n", i)
    elif x > 0 and y > 0 and z > 0:
        print("\nYou can make", g, "with", unit * d, "gr", a, unit * e, "gr", b,
              "and", f * unit, "gr/unit", c, "for", unit, "person.\n", "\n*** You need extra", d * unit - quantity1,
              "gr", a, e * unit - quantity2, "gr", b, "and", f * unit - quantity3, "gr", c, "to cook for",
              unit, "people. *\n", i)
    elif x > 0 and y > 0 and z <= 0:
        print("\nYou can make", g, "with", unit * d, "gr", a, unit * e, "gr", b,
              "and", f*unit, "gr/unit", c, "for", unit, "person.\n", "\n*** You need extra", d * unit - quantity1,
              "gr", a, e * unit - quantity2, "gr", b, "for", unit, "people. *\n", i)
    elif x > 0 and y <= 0 and z > 0:
        print("\nYou can make", g, "with", unit * d, "gr", a, unit * e, "gr", b,
              "and", f*unit, "gr/unit", c, "for", unit, "person.\n", "\n*** You need extra", d * unit - quantity1,
              "gr", a, f * unit - quantity3, "gr", c, "for", unit, "people. *\n", i)
    elif x <= 0 and y > 0 and z > 0:
        print("\nYou can make", g, "with", unit * d, "gr", a, unit * e, "gr", b,
              "and", f*unit, "gr/unit", c, "for", unit, "person.\n", "\n*** You need extra", e * unit - quantity2,
              "gr", b, f * unit - quantity3, "gr", c, "for", unit, "people. *\n", i)
    elif x > 0 and y <= 0 and z <= 0:
        print("\nYou can make", g, "with", unit * d, "gr", a, unit * e, "gr", b,
              "and", f*unit, "gr/unit", c, "for", unit, "person.\n",
              "\n** You need extra", d * unit - quantity1, "gr", a, "for", unit, "people. **\n", i)
    elif x <= 0 and y > 0 and z <= 0:
        print("\nYou can make", g, "with", unit * d, "gr", a, unit * e, "gr", b,
              "and", f*unit, "gr/unit", c, "for", unit, "person.\n",
              "\n** You need extra", e * unit - quantity2, "gr", b, "for", unit, "people. **\n", i)
    else:
        print("\nYou can make", g, "with", unit * d, "gr", a, unit * e, "gr", b,
              "and", f*unit, "gr/unit", c, "for", unit, "person.\n",
              "\n** You need extra", f * unit - quantity3, "gr", c, "for", unit, "people. **\n", i)
    cal = input("Do you want to see calorie of the dish? [y/n]: ")
    if not cal.lower() in ("n", "no"):
        print(g, "have", unit * h, "calorie for", unit, "people")


def dish(a, b, c, d, e, f, g):
    x = c * unit - quantity1
    y = d * unit - quantity2
    if x <= 0 and y <= 0:
        print("\nYou can make", e, "with", unit * c, "gr", a, "and", unit * d, "gr/unit", b, "for", unit, "people.\n", g)
    elif x > 0 and y > 0:
        print("\nYou can make", e, "with", unit * c, "gr", a, "and", unit * d, "gr/unit", b, "for", unit, "people.\n",
              "\n***  You need extra", unit * c - quantity1, "gr", a, "and", unit * d - quantity2, "gr/unit", b,
              "to cook for", unit, "people. *\n", g)
    elif x <= 0 and y > 0:
        print("\nYou can make", e, "with", unit * c, "gr", a, "and", unit * d, "gr/unit", b, "for", unit, "people.",
              "\n** You need extra",  unit * d - quantity2, "gr/unit", b, "to cook for", unit, "people. **\n", g)
    else:
        print("\nYou can make", e, "with", unit * c, "gr", a, "and", unit * d, "gr/unit", b, "for", unit, "people.\n",
              "\n**  You need extra", unit * c - quantity1, "gr/unit", a, "to cook for", unit, "people. **\n", g)
    cal = input("Do you want to see calorie of the dish? [y/n]: ")
    if not cal.lower() in ("n", "no"):
        print(e, "have", unit * f, "calorie for", unit, "person")


go_back = True
print("Hello! Are you starving? I am here for you:)")
while go_back == True:
    print("\n 1. I want to enter the ingredients to find a recipe "
          "\n 2. I want to see all the recipes."
          "\n 3. I want to look for the main course recipes."
          "\n 4. I want to look for the dessert course recipes.")
    try:
        the_choice = int(input("Choose your purpose (1,2,3,4): "))
    except ValueError:
        print("please enter a number")
        continue

    if the_choice == 1:
        print("INGREDIENTS: mince, pasta, meat, cheese, dark chocolate, flour, cream cheese, oil, margarine, sugar, "
              "egg, lemon")
        inp_ingredients = []
        while True:
            in_ing = input("Please enter ingredients that you have: ")
            inp_ingredients.append(in_ing)
            cont = input("Do you want continue adding ingredients? [y/n]: ")
            if not cont.lower() in ("y", "yes"):
                break

        choice = input("Do you want remove any ingredient that you have entered? [y/n]: ")
        choice = choice.lower()
        while choice == "y":
            remove = input("Which ingredient do you want to remove?: ")
            inp_ingredients.remove(remove)
            choice2 = input("Do you want continue remove ingredient? [y/n]: ")
            if not cont.lower() in ("y", "yes"):
                break

        ingredients1 = list(recipe1.values())[1:3]
        ingredients2 = list(recipe2.values())[1:3]
        ingredients3 = list(recipe3.values())[1:3]
        ingredients4 = list(recipe4.values())[1:4]
        ingredients5 = list(recipe5.values())[1:3]
        ingredients6 = list(recipe6.values())[1:3]
        similarity1 = set(ingredients1).intersection(inp_ingredients)
        similarity2 = set(ingredients2).intersection(inp_ingredients)
        similarity3 = set(ingredients3).intersection(inp_ingredients)
        similarity4 = set(ingredients4).intersection(inp_ingredients)
        similarity5 = set(ingredients5).intersection(inp_ingredients)
        similarity6 = set(ingredients6).intersection(inp_ingredients)

        if len(similarity1) == 2:
            print("* We find a dish to prepare for you:", recipe1["dish"], "*")
            try:
                quantity1 = int(input("Please enter your mince's quantity (gr): "))
                quantity2 = int(input("Please enter your oil's quantity: "))
                unit = int(input("How many people do you want to cook for?: "))
            except ValueError:
                print("Please enter a number")
                continue
            dish(recipe1["ing1"], recipe1["ing2"], recipe1["qua1"],
                 recipe1["qua2"], recipe1["dish"], recipe1["cal"], recipe1["rec"])

        elif len(similarity2) == 2:
            print("* We find a dish to prepare for you:", recipe2["dish"], "*")
            try:
                quantity1 = int(input("Please enter your pasta's quantity (gr): "))
                quantity2 = int(input("Please enter your cheese's quantity: "))
                unit = int(input("How many people do you want to cook for?: "))
            except ValueError:
                print("Please enter a number")
                continue
            dish(recipe2["ing1"], recipe2["ing2"], recipe2["qua1"],
                 recipe2["qua2"], recipe2["dish"], recipe2["cal"], recipe2["rec"])
        elif len(similarity3) == 2:
            print("* We find a dish to prepare for you:", recipe3["dish"], "*")
            try:
                quantity1 = int(input("Please enter your meat's quantity (gr): "))
                quantity2 = int(input("Enter your margarine's quantity: "))
                unit = int(input("How many people do you want to cook for?: "))
            except ValueError:
                print("Please enter a number")
                continue
            dish(recipe3["ing1"], recipe3["ing2"], recipe3["qua1"],
                 recipe3["qua2"], recipe3["dish"], recipe3["cal"], recipe3["rec"])
        elif len(similarity4) == 3:
            print("* We find a dish to prepare for you:", recipe4["dish"], "*")
            try:
                quantity1 = int(input("Please enter your dark chocolate's quantity (gr): "))
                quantity2 = int(input("Enter your sugar's quantity: "))
                quantity3 = int(input("Enter your flour's quantity: "))
                unit = int(input("How many people do you want to cook for?: "))
            except ValueError:
                print("Please enter a number")
                continue
            recipe(recipe4["ing1"], recipe4["ing2"], recipe4["ing3"], recipe4["qua1"], recipe4["qua2"],
                   recipe4["qua3"], recipe4["dish"], recipe4["cal"], recipe4["rec"])
        elif len(similarity5) == 2:
            print("* We find a dish to prepare for you:", recipe5["dish"], "*")
            try:
                quantity1 = int(input("Please enter your flour's quantity (gr): "))
                quantity2 = int(input("Enter your egg's quantity: "))
                unit = int(input("How many people do you want to cook for?: "))
            except ValueError:
                print("Please enter a number")
                continue
            dish(recipe5["ing1"], recipe5["ing2"], recipe5["qua1"],
                 recipe5["qua2"], recipe5["dish"], recipe5["cal"], recipe5["rec"])
        elif len(similarity6) == 2:
            print("* We find a dish to prepare for you:", recipe6["dish"], "*")
            try:
                quantity1 = int(input("Please enter your cream cheese's quantity (gr): "))
                quantity2 = int(input("Enter your lemon's quantity: "))
                unit = int(input("How many people do you want to cook for?: "))
            except ValueError:
                print("Please enter a number")
                continue
            dish(recipe6["ing1"], recipe6["ing2"], recipe6["qua1"],
                 recipe6["qua2"], recipe6["dish"], recipe6["cal"], recipe6["rec"])
        else:
            print("Sorry, we can't find any dish to prepare for you")

    elif the_choice == 2:
        print("*****", "\n1.", recipe1["dish"], "\n2.", recipe2["dish"], "\n3.", recipe3["dish"], "\n4.",
              recipe4["dish"], "\n5.", recipe5["dish"], "\n6.", recipe6["dish"], "\n*******")
        try:
            the_all = int(input("Which dish do you want to cook? (1,2,3,4,5):"))
        except ValueError:
            print("Please enter a number")
            continue
        if the_all == 1:
            try:
                quantity1 = int(input("Please enter your mince's quantity (gr): "))
                quantity2 = int(input("Please enter your oil's quantity: "))
                unit = int(input("How many people do you want to cook for?: "))
            except ValueError:
                print("Please enter a number")
                continue
            dish(recipe1["ing1"], recipe1["ing2"], recipe1["qua1"],
                 recipe1["qua2"], recipe1["dish"], recipe1["cal"], recipe1["rec"])
        elif the_all == 2:
            try:
                quantity1 = int(input("Please enter your pasta's quantity (gr): "))
                quantity2 = int(input("Please enter your cheese's quantity: "))
                unit = int(input("How many people do you want to cook for?: "))
            except ValueError:
                print("Please enter a number")
                continue
            dish(recipe2["ing1"], recipe2["ing2"], recipe2["qua1"],
                 recipe2["qua2"], recipe2["dish"], recipe2["cal"], recipe2["rec"])

        elif the_all == 3:
            try:
                quantity1 = int(input("Please enter your meat's quantity (gr): "))
                quantity2 = int(input("Enter your margarine's quantity: "))
                unit = int(input("How many people do you want to cook for?: "))
            except ValueError:
                print("Please enter a number")
                continue
            dish(recipe3["ing1"], recipe3["ing2"], recipe3["qua1"],
                 recipe3["qua2"], recipe3["dish"], recipe3["cal"], recipe3["rec"])

        elif the_all == 4:
            try:
                quantity1 = int(input("Please enter your dark chocolate's quantity (gr): "))
                quantity2 = int(input("Enter your sugar's quantity: "))
                quantity3 = int(input("Enter your flour's quantity: "))
                unit = int(input("How many people do you want to cook for?: "))
            except ValueError:
                print("Please enter a number")
                continue
            recipe(recipe4["ing1"], recipe4["ing2"], recipe4["ing3"],
                   recipe4["qua1"], recipe4["qua2"],
                   recipe4["qua3"], recipe4["dish"], recipe4["cal"], recipe4["rec"])

        elif the_all == 5:
            try:
                quantity1 = int(input("Please enter your flour's quantity (gr): "))
                quantity2 = int(input("Enter your egg's quantity: "))
                unit = int(input("How many people do you want to cook for?: "))
            except ValueError:
                print("Please enter a number")
                continue
            dish(recipe5["ing1"], recipe5["ing2"], recipe5["qua1"],
                 recipe5["qua2"], recipe5["dish"], recipe5["cal"], recipe5["rec"])

        elif the_all == 6:
            try:
                quantity1 = int(input("Please enter your cream cheese's quantity (gr): "))
                quantity2 = int(input("Enter your lemon's quantity: "))
                unit = int(input("How many people do you want to cook for?: "))
            except ValueError:
                print("Please enter a number")
                continue
            dish(recipe6["ing1"], recipe6["ing2"], recipe6["qua1"],
                 recipe6["qua2"], recipe6["dish"], recipe6["cal"], recipe6["rec"])

    elif the_choice == 3:
        print("****", "\n 1.Meatball", "\n 2.Macaroni", "\n 3.Steak", "\n******")
        try:
            the_main = input("which dish do you want to cook? (1,2,3): ")
            the_main = int(the_main)
        except ValueError:
            print("Please enter a number")
            continue
        if the_main == 1:
            try:
                quantity1 = int(input("Please enter your mince's quantity (gr): "))
                quantity2 = int(input("Please enter your oil's quantity: "))
                unit = int(input("How many people do you want to cook for?: "))
            except ValueError:
                print("Please enter a number")
                continue
            dish(recipe1["ing1"], recipe1["ing2"], recipe1["qua1"],
                 recipe1["qua2"], recipe1["dish"], recipe1["cal"], recipe1["rec"])
        elif the_main == 2:
            try:
                quantity1 = int(input("Please enter your pasta's quantity (gr): "))
                quantity2 = int(input("Please enter your cheese's quantity: "))
                unit = int(input("How many people do you want to cook for?: "))
            except ValueError:
                print("Please enter a number")
                continue
            dish(recipe2["ing1"], recipe2["ing2"], recipe2["qua1"],
                 recipe2["qua2"], recipe2["dish"], recipe2["cal"], recipe2["rec"])
        elif the_main == 3:
            try:
                quantity1 = int(input("Please enter your meat's quantity (gr): "))
                quantity2 = int(input("Enter your margarine's quantity: "))
                unit = int(input("How many people do you want to cook for?: "))
            except ValueError:
                print("Please enter a number")
                continue
            dish(recipe3["ing1"], recipe3["ing2"], recipe3["qua1"],
                 recipe3["qua2"], recipe3["dish"], recipe3["cal"], recipe3["rec"])
        else:
            print("Please enter a number")
    elif the_choice == 4:
        print("****", "\n 1.Brownie", "\n 2.Cake", "\n 3.Cheesecake", "\n******")
        the_dessert = int(input("Which dessert do you want to make? (1,2,3):"))
        if the_dessert == 1:
            try:
                quantity1 = int(input("Please enter your dark chocolate's quantity (gr): "))
                quantity2 = int(input("Enter your sugar's quantity: "))
                quantity3 = int(input("Enter your flour's quantity: "))
                unit = int(input("How many people do you want to cook for?: "))
            except ValueError:
                print("Please enter a number")
                continue
            recipe(recipe4["ing1"], recipe4["ing2"], recipe4["ing3"],
                   recipe4["qua1"], recipe4["qua2"],
                   recipe4["qua3"], recipe4["dish"], recipe4["cal"], recipe4["rec"])

        elif the_dessert == 2:
            try:
                quantity1 = int(input("Please enter your flour's quantity (gr): "))
                quantity2 = int(input("Enter your egg's quantity: "))
                unit = int(input("How many people do you want to cook for?: "))
            except ValueError:
                print("Please enter a number")
                continue
            dish(recipe5["ing1"], recipe5["ing2"], recipe5["qua1"],
                 recipe5["qua2"], recipe5["dish"], recipe5["cal"], recipe5["rec"])

        elif the_dessert == 3:
            try:
                quantity1 = int(input("Please enter your cream cheese's quantity (gr): "))
                quantity2 = int(input("Enter your lemon's quantity: "))
                unit = int(input("How many people do you want to cook for?: "))
            except ValueError:
                print("Please enter a number")
                continue
            dish(recipe6["ing1"], recipe6["ing2"], recipe6["qua1"],
                 recipe6["qua2"], recipe6["dish"], recipe6["cal"], recipe6["rec"])
        else:
            print("Please enter a number")
    else:
        print("Please enter a number between 1 and 4")
    answer = input('Would you like to return to the Main Menu? (Y/N):').upper()
    if answer == 'N':
        print("See you")
        go_back = False
