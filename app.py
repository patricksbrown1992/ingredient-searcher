from flask import Flask, render_template, request
import pdb
import json
import os
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])

def index():
    

    name = None
 

    if request.method == 'POST':
        
        name = request.form['ingredient']
    else:
        name = '' 

    def fetch_json(file_name):
        root = os.path.realpath(os.path.dirname(__file__))
        url = os.path.join(root, 'static', file_name)
        parsed_json = json.load(open(url))
        return parsed_json

    def fetch_ingredients():
        fetched_ingredients = fetch_json('ingredients.json')
       
        return fetched_ingredients

    def fetch_products(resources, ingredients, name):
        fetched_products = fetch_json('products.json')
        resources["products"] = []
        already_added = {}
        for product in fetched_products:
            for ingredientID in product["ingredientIds"]:
                
                ingredient = ingredients[ingredientID-1]["name"]
                length = len(name)
                
                if name == ingredient[0:length] and product["id"] not in already_added:
                    already_added[product["id"]] = True
                    resources["products"].append(product)
                    
    

      
        return resources
  
    resources = {}
    resources['reversed_resources'] = {}
    ingredients = fetch_ingredients()
    resources['ingredients'] = ingredients
   
    resources = fetch_products(resources, ingredients, name)
    
    

    
    
  
    
    return render_template('index.html', resources=resources)


if __name__ == "__main__":
    app.run(debug=True)