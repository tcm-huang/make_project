# Sarah Morrissey API Midterm

apiKey = '1af00afae62ff4c704eabc220f3da104'
apiID = 'd3ba4cd2'

import requests
import json
from pprint import pprint
import time
import key

apiKey = key.apiKey
apiID = key.apiID

# different diet categories as listed in the API documentation
dietLabels = ['balanced', 'high-fiber', 'high-protein',
              'low-fat', 'low-carb', 'low-sodium']

# different health categories as listed in the API documentation
healthLabels = ['vegan', 'vegetarian', 'paleo', 'dairy-free', 'gluten-free',
                'wheat-free', 'fat-free', 'low-sugar', 'egg-free', 'peanut-free', 'tree-nut-free',
                'soy-free', 'fish-free', 'shellfish-free']

# categories of cuisines available in the API documentation
cuisineType = ['American', 'Asian', 'British', 'Caribbean', 'Central Europe', 'Chinese', 'Eastern Europe',
               'French', 'Indian', 'Italian', 'Japanese', 'Kosher', 'Mediterranean', 'Mexican', 'Middle Eastern', 'Nordic',
               'South American', 'South East Asian']


# this function takes in the appropriate URL as a parameter and proceeds to extract the recipe information
def Choice(url):
    response = requests.get(url)
    response.raise_for_status()
    foodData = json.loads(response.text)
    hits = foodData["hits"]
    return Output(hits)


# This function gets the specific information from the json data, prints it in the terminal, and creates the external text file

def Output(hits):
    # this asks the user how many recipes they would like to see and stores it in the variable "number"
    print('How many recipes would you like to see?')
    number = input()
    number = int(number)
    given = 0

    # at the beginning, myCookbook (list) is empty, and myRecipe is empty (dictionary)
    myCookbook = []
    myRecipe = {}

    # This analyzes if the number of recipes wanted is >=1 to know what response to give
    if number == 1:
        Beginning = "We found a recipe!"
    elif number > 1:
        Beginning = "We found a few recipes!"

    for given in range(number):  # this for loop iterates through each recipe, starting with hit(recipe) 0, and for the range of the number that the user wants, looks at each individual recipe
        given = given

        # These variables are defined by pulling the appropriate list placement for each variable, returning the Nutritional information as floats, then rounding
        # the decimals to 2 places, then converting that final number to a string
        # the Final string for each variable will be printed in the terminal
        ServingsAndTime = 'Serves: ' + str(hits[given]['recipe']['yield']) + \
            ', Total Time: ' + \
            str(hits[given]['recipe']['totalTime']) + ' minutes'
        Name = 'Name: ' + "\033[1m" + \
            str(hits[given]['recipe']['label']) + "\033[0m"
        NumServings = int(hits[given]['recipe']['yield'])
        NutrInfo = 'Nutritional Info (per serving): '
        Calories = 'Calories: ' + str(
            round(float(hits[given]['recipe']['calories'])/NumServings, 2))
        Fat = 'Fat: ' + str(round(float(hits[given]['recipe']['totalNutrients']
                                        ['FAT']['quantity'])/NumServings, 2)) + ' g'
        Carbs = 'Carbohydrates: ' + str(round(float(hits[given]['recipe']['totalNutrients']
                                                    ['CHOCDF']['quantity'])/NumServings, 2)) + ' g'
        Fiber = 'Fiber: ' + str(round(float(hits[given]['recipe']['totalNutrients']
                                            ['FIBTG']['quantity'])/NumServings, 2)) + ' g'
        Sugar = 'Sugar: ' + str(round(float(hits[given]['recipe']['totalNutrients']
                                            ['SUGAR']['quantity'])/NumServings, 2)) + ' g'
        Protein = 'Protein: ' + str(round(float(hits[given]['recipe']['totalNutrients']
                                                ['PROCNT']['quantity'])/NumServings, 2)) + ' g'
        Cholestrol = 'Cholestrol: ' + str(round(float(hits[given]['recipe']['totalNutrients']
                                                      ['CHOLE']['quantity'])/NumServings, 2)) + ' mg'
        Sodium = 'Sodium: ' + str(round(float(hits[given]['recipe']['totalNutrients']
                                              ['NA']['quantity'])/NumServings, 2)) + ' mg'
        Ingredients = 'Ingredients: ' + \
            str(hits[given]['recipe']['ingredientLines'])
        url = 'Recipe URL: ' + str(hits[given]['recipe']['url'])

        # These variables are basically the same thing as above, however only have the string version of the number so they can be stored in the dictionary later on
        Servings2 = str(hits[given]['recipe']['yield'])
        Time2 = str(hits[given]['recipe']['totalTime']) + ' minutes'
        Name2 = str(hits[given]['recipe']['label'])
        NutrInfo2 = ''
        Calories2 = str(
            round(float(hits[given]['recipe']['calories'])/NumServings, 2))
        Fat2 = str(round(float(hits[given]['recipe']['totalNutrients']
                               ['FAT']['quantity'])/NumServings, 2)) + ' g'
        Carbs2 = str(round(float(hits[given]['recipe']['totalNutrients']
                                 ['CHOCDF']['quantity'])/NumServings, 2)) + ' g'
        Fiber2 = str(round(float(hits[given]['recipe']['totalNutrients']
                                            ['FIBTG']['quantity'])/NumServings, 2)) + ' g'
        Sugar2 = str(round(float(hits[given]['recipe']['totalNutrients']
                                            ['SUGAR']['quantity'])/NumServings, 2)) + ' g'
        Protein2 = str(round(float(hits[given]['recipe']['totalNutrients']
                                   ['PROCNT']['quantity'])/NumServings, 2)) + ' g'
        Cholestrol2 = str(round(float(hits[given]['recipe']['totalNutrients']
                                      ['CHOLE']['quantity'])/NumServings, 2)) + ' mg'
        Sodium2 = str(round(float(hits[given]['recipe']['totalNutrients']
                                  ['NA']['quantity'])/NumServings, 2)) + ' mg'
        Ingredients2 = str(hits[given]['recipe']['ingredientLines'])
        url2 = str(hits[given]['recipe']['url'])

        # This stores the needed variables in a list to be printed in the terminal
        Process = [Beginning, Name, ServingsAndTime, Ingredients, url,
                   NutrInfo]
        Process2 = [Calories, Fat, Carbs, Fiber,
                    Sugar, Protein, Cholestrol, Sodium]

        # These for loops print the above information in the terminal
        for line in Process:
            print(line)
            print()

        for line in Process2:
            print(line)

        # This moves the for loop to recipe #2 in the available options
        given = given + 1

        # This stores the information as a key value pair in the dictionary to be printed in the external file
        myRecipe['Name'] = Name2
        myRecipe['Serves'] = Servings2
        myRecipe['Time'] = Time2
        myRecipe['Ingredients'] = Ingredients2
        myRecipe['URL'] = url2
        myRecipe['Nutritional Info (per serving)'] = NutrInfo2
        myRecipe['Calories'] = Calories2
        myRecipe['Fat'] = Fat2
        myRecipe['Carbs'] = Carbs2
        myRecipe['Fiber'] = Fiber2
        myRecipe['Sugar'] = Sugar2
        myRecipe['Protein'] = Protein2
        myRecipe['Cholestrol'] = Cholestrol2
        myRecipe['Sodium'] = Sodium2

        # This adds copies of the dictionaries above as an item in the list of myCookbook, which is then updated to reflect new recipes
        eachRecipe = myRecipe.copy()
        myCookbook.append(eachRecipe)
        myCookbook = myCookbook

        # This code writes the text file for the recipes to be stored
        output = open("My List of Recipes.txt", "w")

        # this for loop iterates through each item (each set of dictionaries in the list) and for each key value pair in the
        # dictionary, it prints the key then the value, then it moves onto the next item in the list, and then the file is closed
        for item in myCookbook:
            # output.write(str(item))
            for k in item:
                output.write(k + ': ' + item[k] + "\n")
            output.write("\n")
        output.close()
        myCookbook = myCookbook

    print('Your recipe list from your most recent search are in the file!')

# this Intro function asks the user how they would like to search for a recipe, and processes the appropriate url


def Intro():
    print('''
    What would you like to look for today?

    A recipe by name? (R)
    A recipe by ingredient? (I)
    A recipe by nutritional info? (N)
    A recipe by cuisine type? (C)

    If you would like a combination of all of these, type all
    ''')

    # These different options allow the user to input how they would like to search for a recipe, and proceeds to complete the necessary steps including
    # a different URL for each
    answer = input().lower()

    if answer == 'r':
        print('Please enter the recipe name')
        recipe = input()
        recipeURL = f"https://api.edamam.com/search?q={recipe}&app_id={apiID}&app_key={apiKey}&dishType=Main-course&mealType=Lunch&mealType=Dinner"
        Choice(recipeURL)

    if answer == 'i':
        print('Please enter the ingredient')
        ingredient = input()
        ingredientURL = f"https://api.edamam.com/search?q={ingredient}&app_id={apiID}&app_key={apiKey}&mealType=Lunch&mealType=Dinner&dishType=Main-course"
        Choice(ingredientURL)

    if answer == 'c':
        print('Here is a list of the available Cuisine categories to choose from: ')
        for x in range(len(cuisineType)):
            print(cuisineType[x])
        print()
        print('Which type of cuisine would you like to look for today?')
        choice = input().lower()
        cuisineURL = f"https://api.edamam.com/search?q={choice}&app_id={apiID}&app_key={apiKey}&dishType=Main-course&mealType=Dinner"
        Choice(cuisineURL)

    if answer == 'n':
        # this prints the diet options from the list at the top
        print('Here is a list of the possible diet labels: ')
        time.sleep(1)
        for x in range(len(dietLabels)):
            print(dietLabels[x])
        print()
        time.sleep(2)

        # This prints the health options from the list at the top
        print('Here is a list of the possible health labels: ')
        time.sleep(1)
        for x in range(len(healthLabels)):
            print(healthLabels[x])
        print()
        time.sleep(2)
        # This allows you to pick if you would like to choose a diet option, a health option, or both
        print('''
        If you would like to find a recipe according to diet, enter diet.
        If you would like to find a recipe according to health restrictions, enter health. 
        If you would like to find a recipe that adheres to both, please enter both.''')
        print()
        answer = input().lower()
        if answer == 'diet':
            print('Which diet restriction would you like to search by?')
            diet = input().lower()
            dietURL = f"https://api.edamam.com/search?q={diet}&app_id={apiID}&app_key={apiKey}&dishType=Main-course&mealType=Lunch&mealType=Dinner"
            Choice(dietURL)

        if answer == 'health':
            print('Which health restriction would you like to search by?')
            health = input().lower()
            healthURL = f"https://api.edamam.com/search?q={health}&app_id={apiID}&app_key={apiKey}&dishType=Main-course&mealType=Lunch&mealType=Dinner"
            Choice(healthURL)

        if answer == 'both':
            print('Which health restriction?')
            health = input().lower()
            health = str(health)
            print('Which dietary restriction?')
            diet = input().lower()
            diet = str(diet)
            bothURL = f"https://api.edamam.com/search?q={health}&app_id={apiID}&app_key={apiKey}&dishType=Main-course&mealType=Lunch&mealType=Dinner&Diet={diet}"
            Choice(bothURL)

    # This function is a combination of all of the above options: searching for a recipe by ingredient, cuisine, and nutritional options
    if answer == 'all':
        print('What ingredient would you like to be included?')
        ingredient = input()
        print()
        print('Here is a list of the available Cuisine categories to choose from: ')
        for x in range(len(cuisineType)):
            print(cuisineType[x])
        print()
        print('Which type of cuisine would you like to look for today?')
        choice = input().lower()
        print()
        print('Here is a list of the possible diet labels: ')
        time.sleep(1)
        for x in range(len(dietLabels)):
            print(dietLabels[x])
        print()
        time.sleep(2)
        print('Here is a list of the possible health labels: ')
        time.sleep(1)
        for x in range(len(healthLabels)):
            print(healthLabels[x])
        print()
        time.sleep(2)
        print('Which diet constraint would you like to adhere to?')
        diet = input().lower()
        print()
        print('Which health constraint would you like to adhere to?')
        health = input().lower()
        allURL = f"https://api.edamam.com/search?q={ingredient}&app_id={apiID}&app_key={apiKey}&mealType=Lunch&mealType=Dinner&dishType=Main-course&cuisineType={choice}&diet={diet}&health={health}"
        Choice(allURL)


# main
print()
print('Hello chef! Welcome to your recipe search.')

again = 'yes'

# This while loop allows a user to keep searching for recipes
while again == 'yes' or again == 'y':
    Intro()
    print()
    print('Do you want to look for more recipes? (yes or no)')
    again = input()
