import argparse
import sys
import requests

from json.decoder import JSONDecodeError

# Base endpoint
BASE_ENDPOINT = "http://www.thecocktaildb.com/api/json/v1/1/"
# The api has max 15 ingredients
MAX_INGREDIENTS = 15

# Print list in new line
def PrintCocktails(inputList):
    for tmp in inputList:
        print(tmp)

# Type used in argparser to split inputs based on comma
def comma_separated_list(string):
    return string.split(',')

# Function returns list of cocktails that can be prepared
# Input - List of Ingredients supplied by the user
# Return - List of cocktails that can be made using the provided ingredients
def GetCocktailList(userItemList):
    print("Trying to Fetch Cocktails - Kindly Wait ...")
    ingredientsCount = len(userItemList)
    cocktailList = list()
    allDrinks = list()
    try:
        Response = requests.get(BASE_ENDPOINT + 'filter.php?i=' + userItemList[0])
        try:
            allDrinks = Response.json()['drinks']
        except ValueError:
            print(
                'The server returned a blank response. Probably incorrect ingredient supplied or no Cocktail recipe found using this ingredient !!')
            sys.exit(1)
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    except requests.exceptions.RequestException as err:
        raise SystemExit(err)

    # List all drinks possible with the single ingredient and return
    if ingredientsCount == 1:
        for drink in allDrinks:
            cocktailList.append(drink["strDrink"])
        return cocktailList
    else:
        # We iterate all drinks - check their ingredients and compare them with user provided ingredients
        # If all user ingredients are found in one cocktail, we add that to our return list
        for drink in allDrinks:
            allItemsPresent = 0
            try:
                Response = requests.get(BASE_ENDPOINT + 'lookup.php?i=' + drink['idDrink'])
                try:
                    drinkDetails = Response.json()['drinks']
                    for num in range(1, MAX_INGREDIENTS + 1):
                        cocktail_ingredient = drinkDetails[0][f"strIngredient{num}"]

                        # Observed from the API calls that all valid ingredients are placed at the top
                        # Hence break calculation when the first None is encountered
                        # Tomorrow if API provides ingredients in random manner, break can be replaced with continue
                        if cocktail_ingredient is None:
                            break
                        else:
                            if cocktail_ingredient in userItemList:
                                allItemsPresent += 1

                    # If all user ingredients have been found in this cocktail
                    if allItemsPresent == ingredientsCount:
                        cocktailList.append(drink["strDrink"])

                except ValueError:
                    print(
                        'The server returned a blank response. Probably incorrect cocktail id - ' + drink['idDrink'])
                    sys.exit(1)
            except requests.exceptions.HTTPError as err:
                raise SystemExit(err)
            except requests.exceptions.RequestException as err:
                raise SystemExit(err)

    return cocktailList


def main(argv):
    parser = argparse.ArgumentParser(
        description="A tool to quickly figure out what cocktails can be made from the ingredients present in your kitchen !.")
    parser.add_argument('-i', '--ingredients', type=comma_separated_list, dest='ingredients',
                        help='Provide Ingredient List(Comma Separated)')
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    args = parser.parse_args()

    itemList = [tmp.strip(' ') for tmp in args.ingredients]

    if len(itemList) > MAX_INGREDIENTS:
        print("Too many Ingredients. Max allowed is ", MAX_INGREDIENTS)
        sys.exit(1)
    else:
        cocktailList = GetCocktailList(itemList)
        PrintCocktails(cocktailList)
        sys.exit(0)


if __name__ == '__main__':
    main(sys.argv[1:])
