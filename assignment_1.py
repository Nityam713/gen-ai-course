# Task 1: Product Collections(Lists and Tuples)

# List named products with 6 products
products = ["Laptop","Phone","Earbuds","Watch","Speaker","SSD"]

# Tuple named sample_product with product name, price, category
sample_product = ("Laptop", 40000, "electronics")

# Print 2nd and last product from the lis
print(products[1], products[-1])

# Append 2 new products and print updated list
products.extend(["Mouse", "Keyboard"])
print(products)

# Converting sample_product into list, changing price and converting it back to tuple
temp = list(sample_product)
temp[1] = 50000
sample_product = tuple(temp)
print(sample_product)

# Task 2: Categories(Sets)

# From products list, creating set of categories called categories_set
categories = ["Electronics","Electronics","Accessories","Wearables","Audio","Storage","Accessories","Accessories"]

categories_set = set(categories)
print(categories_set)

# Demonstrating adding new category to the set and show the duplicates are ignored
categories_set.add("Gaming")
print(categories_set)

categories_set.add("Accessories")
print(categories_set)

# Checking weather a category exists in the set(printing boolean result)
print("Electronics" in categories_set)
print("Furniture" in categories_set)

# Showing total number of unique categories using a set
print(len(categories_set))

# Task 3: Product Pricing(Dictionaries)

# Creating dictionary price_dict where keys are product names and values are prices
price_dict = {"Laptop": 40000, "Phone":25000, "Earbuds": 3000, "Watch": 8000, "Speaker": 8000, "SSD": 6000}

# Adding new product with price, updating price of existing product and remove a product by name also handle a case when product does not exist
price_dict["Charger"] = 1000
print(price_dict)

price_dict.update({"SSD": 10000})
print(price_dict)

price_dict.pop("Earbuds")
print(price_dict)

removed = price_dict.pop("Powerbank", None)

if removed is None:
    print("Powerbank not found in price_dict")

print(price_dict)

