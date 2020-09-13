# README

# Ingredient Searcher


## Live version deployed to Heroku
### [Ingredient Searcher](https://ingredient-searcher.herokuapp.com)



## How to run

either use the live app or download the app. Unzip it. works with either python or python3. You will need flask if you want to run it locally. pip install flask for python or pip3 install flask for python3. pip install requests. make sure you're in the root directory and run python app.py or python3 app.py

## Features

## Allows partial searches by prefix

------

### DH logo in tab. 

![tab](/static/tab.png)

-------- 

### Helpful errors on unapproved characters

![error](/static/error.png)

------

### Clean UI and easy UX

![searched](/static/searched.png)

----- 

### reset button when no products match search

![no-results](/static/no-results.png)





## Other thoughts

Time complexity is O(n) where n is the total number of ingredients used across the products. It has to iterate over every ingredient in every product. O(n * m) where n is the number of products and m is the average number of ingredients per product is another way to characterize it if you want to show that there is a nested loop. 

One fix I'd make is that a user is allowed to just type in cherry, and it returns all the products with cherry instead of having to type out organic sweet cherry or a sub-prefix to match "Your solution should return only products that contain the specified ingredient as output" in the requirements. This would add a tad more time complexity as you'd have to split the word in an ingredient on a space and iterate over that to check if one of the words was cherry. You'd add average number of words in an ingredient as part of time complexity. In return, it would be much easier for the average user, so I think the trade off would be worth it. 

I can take it down from Heroku after I hear back either way. Just wanted to make it as easy as possible for you all to try it out. 

If I had more time, I'd probably add a prefix tree to make search for ingredients faster and give suggestions to the user. Afterwards, it would be the opposite of the Ingredient IDs in the products JSON. It would have an ingredient, organic sweet cherry, as the key with the value as an array/list of all of the ids of products which need it (1 acia + cherry and 67 cherry and almond) to index - 1 into the products array in contstant time after the O(n) iteration over the the Ids. 

Another thing I'd add is responsivity. It doesn't look terrible on iPad or mobile. Just doesn't have css specialized for it. 