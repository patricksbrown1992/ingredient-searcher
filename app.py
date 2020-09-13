from flask import Flask, render_template, request
import pdb
import json
import os
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])

def index():
    
    errors = None
    search = None
 
    # if the submit button is clicked
    if request.method == 'POST':
        errors_found = []
        
        acceptable_chars = {'-': True, '+': True, "'": True, ' ': True, 'a': True, 'A': True, 'b': True, 'B': True, 'C': True, 'c': True, 'D': True, 'd': True, 'E': True, 'e': True, 'F': True, 'f': True, 'G': True, 'g': True, 'H': True, 'h': True, 'I': True, 'i': True, 'J': True, 'j': True, 'K': True, 'k': True, "L": True, 'l': True, 'M': True, 'm': True, 'N': True, 'n': True, "O": True, 'o': True, "P": True, 'p': True, "Q": True, 'q': True, "R": True, "r": True, "S": True, 's': True, "T": True, 't': True, "U": True, 'u': True, "V": True, "v": True, "W": True, 'w': True, "X": True, "x": True, "Y": True, "y": True, "Z": True, "z": True}
        # user input as a string
        searched_string = request.form['ingredient']
        # iterate over string to check that every character is acceptable
        for char in searched_string:
            if char not in acceptable_chars:
                errors_found.append(char)
        
        if len(errors_found) > 0:
            search = ''
            errors = errors_found
        else:
            errors = ''
            search = searched_string
    else:
        errors = ''
        search = '' 

    def fetch_json(file_name):
        root = os.path.realpath(os.path.dirname(__file__))
        url = os.path.join(root, 'static', file_name)
        parsed_json = json.load(open(url))
        return parsed_json

    def fetch_ingredients():
        fetched_ingredients = fetch_json('ingredients.json')
       
        return fetched_ingredients

    def fetch_and_search_products(resources, ingredients, search, errors):
        # grab products
        fetched_products = fetch_json('products.json')
        
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
                    
    

        # if len(resources["products"]) == 0:
        #     resources["products"] = [{"name": "There are no recipes with" + search + '. please try again', "ingredientId": "", "image": {"url": ''}}]
        return resources
  

    
    ingredients = fetch_ingredients()
    
    
    resources = fetch_and_search_products({}, ingredients, search, errors)
    resources["ingredients"] = ingredients
    resources["errors"] = errors
    resources["search"] = search

    
    
  
    
    return render_template('index.html', resources=resources)


if __name__ == "__main__":
    app.run(debug=True)