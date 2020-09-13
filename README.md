# README

# Ingredient Searcher


## Live version deployed to Heroku
### [Ingredient Searcher](https://ingredient-searcher.herokuapp.com)



## How to run


## Features

## Other thoughts

Time complexity is O(n) where n is the total number of ingredients used across the products. It has to iterate over every ingredient in every product. O(n * m) where n is the number of products and m is the average number of ingredients per product is another way to characterize it if you want to show that there is a nested loop. 

One fix I'd make is that a user is allowed to just type in cherry and it returns all the products with cherry instead of having to type out organic sweet cherry to match "Your solution should return only products that contain the specified ingredient as output" in the requirements. This would add a tad more time complexity as you'd have to split the word in an ingredient on a space and iterate over that to check if one of the words was cherry, so you'd add average number of words in product as part of time complexity.