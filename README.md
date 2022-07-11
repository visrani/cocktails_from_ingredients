# cocktails_from_ingredients
A tool to quickly figure out what cocktails can be made from the ingredients present in your kitchen !

Pre-Requisite - Python 2.7 and above

Execution
python SuggestCocktails.py
usage: SuggestCocktails.py [-h] [-i INGREDIENTS]

A tool to quickly figure out what cocktails can be made from the ingredients present in your kitchen !.

options:
  -h, --help            show this help message and exit
  -i INGREDIENTS, --ingredients INGREDIENTS
                        Provide Ingredient List(Comma Separated)
						

Example
All ingredients need to be provided with the -- ingredients or the -i tag
The ingredients need to be passed as a string and should be comma separated
python SuggestCocktails.py --ingredients "Cherry brandy, Dark rum"


The Fine Print
1. The user is expected to input the ingredients similar and case-sensitive to how they are referred in https://www.thecocktaildb.com/
2. The tool will match all user provided ingredients and only the cocktails that consume all the ingredients will be listed.


