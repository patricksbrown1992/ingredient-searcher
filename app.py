from flask import Flask, render_template, request
import pdb
import json
import os
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])

def index():
    

    search = None
 
    if request.method == 'POST':
        
        search = request.form['ingredient']
    else:
        search = '' 

    def fetch_json(file_name):
        root = os.path.realpath(os.path.dirname(__file__))
        url = os.path.join(root, 'static', file_name)
        parsed_json = json.load(open(url))
        return parsed_json

    def fetch_ingredients():
        fetched_ingredients = fetch_json('ingredients.json')
       
        return fetched_ingredients

    def fetch_and_search_products(resources, ingredients, search):
        # grab products
        fetched_products = fetch_json('products.json')
        
        resources["products"] = []
        # use constant time to check if product has already been added
        already_added = {}
        # compare ingredient name against search
        length = len(search)
        # save pointless iteration if there is no ingredient to search for yet
        if search == '':
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
    
    
    resources = fetch_and_search_products({}, ingredients, search)
    resources["ingredients"] = ingredients
    

    
    
  
    
    return render_template('index.html', resources=resources)


if __name__ == "__main__":
    app.run(debug=True)