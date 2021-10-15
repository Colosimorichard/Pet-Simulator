# pet dictionary
pet = {"name": "", "type": "", "age": 0, "hunger": 0, "toys": []}

# Pet toys data object
petToys = {"cat": ["scratching post", "toy mouse", "ball of yarn"], "dog": ["chew toy", "stick", "frisbee"], "fish": ["undersea castle", "fake coral", "buried treasure"]}
# Prompt for different options of pet type
def initPet():
    # get the input of what type of pet
    petType = ""
    petOptions = list(petToys.keys())

    # validate input
    while petType not in petOptions:
        print("Please intput a type of pet from the following options: ")
        for option in petOptions:
            print(option)
        petType = input("Please input one of the pets: ")
    print(petType)
    # write pet type into database
    pet["type"] = petType
    # name our pet
    pet["name"] = input("What would you like to name your " + pet["type"] + "? ")
    
    # write to pet dictionary to store

# Print menu
def printMenu(menuOptions):
    optionKeys = list(menuOptions.keys())

    print("Here are your options:")
    print("------")
    for key in optionKeys:
        print(key + ":\t" + menuOptions[key]["text"])

# Plays with our toys
def playToys():
    print(pet["name"] + " had a wonderful time playing with toys!")

# Get new toys
def getToys():
    print("Yay! Let's get some new toys!")
    toyOptions = petToys[pet["type"]]
  
# specific toy number to select from list
    toyNum = -1
    # get a valid toy to input
    while toyNum < 0 or toyNum > len(toyOptions) -1:
        for i in range(len(toyOptions)):
            print(str(i) + ": " + toyOptions[i])
        toyNum = int(input("Input the number of the toy you would like: "))
    # get selected toy option from our list
    chosenToy = toyOptions[toyNum]
    pet["toys"].append(chosenToy)
    print("Nice! You selected the " + chosenToy +"!")
# Quit Game
def quitSimulator():
    print("Quit the simulator, Thanks for playing!")

# Feed Pets
def feedPet():
    # handle negative edge cases
    newHunger = pet["hunger"] - 20
    if newHunger < 0:
        newHunger = 0
    pet["hunger"] = newHunger
    print("Fed your pet, decreasing hunger by 10!")

# print out stats about current status of the pet
def printStats():
    print("Your " + pet["type"] + " " + pet["name"] + " is doing great!")
    print("Your pet currently has: " + str(len(pet["toys"])) + " toys, which are")
    for toy in pet["toys"]:
        print(toy)
    print("Your pet is currently at a hunger of " + str(pet["hunger"]) +" of a max of 100")
    print("Your pet is " + str(pet["age"]) +" days old.")

# Main game loop
def main():
    # print the menu
    initPet()
    # menu options for printing and access
    menuOptions = {"Q": { "function": quitSimulator, "text": "Quit the game"}, "F": {"function": feedPet, "text": "Feed " + pet["name"] }, "P": {"function": playToys, "text": "Play with " + pet["name"]}, "G": {"function": getToys, "text": "Get new toys for " + pet["name"] + "!"}}

    keepPlaying = True
    while keepPlaying:
        # print the menu
        menuSelection = ""
        # validate the input
        while menuSelection not in menuOptions.keys():
            printMenu(menuOptions)
            menuSelection = input("Which of thse menu options would you like to use? ").upper()

        # quit game if user put in q
        if menuSelection == "Q":
            keepPlaying = False
        # invoke the function corresponding to the selected menu options
        menuOptions[menuSelection]["function"]()

        # increase hunger
        pet["hunger"] += 10
        pet["age"] += 10
        printStats()

        # print out an extra line between options
        print()
   

main()