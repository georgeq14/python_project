ian_fruits = {
    
    "apples", 
    "bananas",
    "watermelon",
    "oranges",
    "mangoes"
    
}

gen_fruits = {
    
    "pineapples",
    "strawberries",
    "blueberries",
    "raspberries",
    "apples"
    
}

union = ian_fruits.union(gen_fruits)
intersetion = ian_fruits.intersection(gen_fruits)

print(union)
print(intersetion)