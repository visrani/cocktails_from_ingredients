import sys

import SuggestCocktails



def main(argv):
    inputList = ['Vodka']
    cocktailList = list()
    cocktailList = SuggestCocktails.GetCocktailList(inputList)
    if len(cocktailList) > 90:
        print("Test 1 Pass")
    else:
        print("Test 1 Fail")

    cocktailList.clear()
    inputList = ['Bourbon', 'Benedictine']
    cocktailList = SuggestCocktails.GetCocktailList(inputList)
    if len(cocktailList) >= 2:
        if cocktailList[0] in ['Kentucky B And B', 'Kentucky Colonel'] and cocktailList[1] in ['Kentucky B And B',
                                                                                               'Kentucky Colonel']:
            print("Test 2 Pass")
    else:
        print("Test 2 Fail")

if __name__ == '__main__':
    main(sys.argv[1:])
