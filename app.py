from flask import Flask, render_template
import pdb
import json
import os
app = Flask(__name__)

@app.route('/')

def index():

    def fetch_json(file_name):
        root = os.path.realpath(os.path.dirname(__file__))
        url = os.path.join(root, 'static', file_name)
        parsed_json = json.load(open(url))
        return parsed_json

    def fetch_ingredients():
        fetched_ingredients = fetch_json('ingredients.json')
       
        return fetched_ingredients

    def fetch_products():
        fetched_products = fetch_json('products.json')
        return fetched_products

    resources = {}
    products = fetch_products()
    ingredients = fetch_ingredients()
    
    resources['products'] = products
    resources['ingredients'] = ingredients
    # pdb.set_trace()
    return render_template('index.html', resources=resources)


if __name__ == "__main__":
    app.run(debug=True)