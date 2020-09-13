from flask import Flask, render_template, request

import pdb
import json

import requests
import string

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])

def index():
    
    errors = search = None
   
    
    # if the submit button is clicked
    if request.method == 'POST':

        
        acceptable_chars = set(string.ascii_letters + "+-' ")
        # user input as a string
        searched_string = request.form['ingredient']
        # iterate over string to check that every character is acceptable
        errors_found = [char for char in searched_string if not (char in acceptable_chars)]
       
        errors = errors_found if len(errors_found) > 0 else ""
        search = "" if len(errors_found) > 0 else searched_string
   
    else:
        errors = ''
        search = ''

    def fetch_ingredients():
       
        fetched_ingredients = json.loads(requests.get("https://raw.githubusercontent.com/daily-harvest/opportunities/master/web-1/data/ingredients.json").text)
        return fetched_ingredients

    def fetch_and_search_products(resources, ingredients, search, errors):

        fetched_products = json.loads(requests.get("https://raw.githubusercontent.com/daily-harvest/opportunities/master/web-1/data/products.json").text)
        resources["products"] = []
        # use constant time to check if product has already been added
        already_added = {}
        # compare ingredient name against search
        length = len(search)
        # save pointless iteration if there is no ingredient to search for yet or there was an error
        if search == '' or len(errors) > 0:
            resources["products"] = fetched_products
        else:
            for product in fetched_products:
                for ingredientID in product["ingredientIds"]:
                    
                    ingredient = ingredients[ingredientID-1]["name"]
                    
                    # if the product has not already been added and the search partial matches the beginning of the ingredient name regardless of upper or lower case
                    if search.lower() == ingredient[0:length].lower() and product["id"] not in already_added:
                        already_added[product["id"]] = True
                        resources["products"].append(product)
                    
    
        return resources
  

    
    ingredients = fetch_ingredients()
    
    
    resources = fetch_and_search_products({}, ingredients, search, errors)
    resources["ingredients"] = ingredients
    resources["errors"] = errors
    resources["search"] = search

    
    
  
    
    return render_template('index.html', resources=resources)


if __name__ == "__main__":
    app.run(debug=True)