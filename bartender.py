""" bartender assistant -- helps beginners learn how to mix drinks """

import urllib.request as request
import json

cocktailURL = "https://www.thecocktaildb.com/api.php"
drinkByNameURL = "https://www.thecocktaildb.com/api/json/v1/1/search.php?s="

def getDrinksByName(drinkname):
    response = request.urlopen("https://www.thecocktaildb.com/api/json/v1/1/search.php?s="+drinkname)
    source = response.read()
    data = json.loads(source)
    return data['drinks']

def getDrinkById(drinkId):
    response = request.urlopen("https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i="+str(drinkId))
    source = response.read()
    data = json.loads(source)
    return data['drinks'][0]

def getDrinksByIngredient(ingredient):
    """ get list of drink names and ids for all drinks containing an ingredient """
    response = request.urlopen("https://www.thecocktaildb.com/api/json/v1/1/filter.php?i="+ingredient)
    source = response.read()
    data = json.loads(source)
    return data['drinks']

def listDrinks():
    """ ask user for an ingredient and print out all drinks using that ingredient """
    alcohol = input("What is the main ingredient? ")
    drinks = getDrinksByIngredient(alcohol)
    for d in drinks:
        print(d['strDrink'],d['idDrink'])

def printDrink(d):
    print(d['strDrink'])
    print('in '+d['strGlass'])
    print(d['strInstructions'])
    for i in range(1,16):
        z = d['strIngredient'+str(i)]
        if z:
            print(z,d['strMeasure'+str(i)])
    print('')



if __name__ == "__main__":
    listDrinks()
