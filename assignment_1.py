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

# Average price of all products

total_price = sum(price_dict.values())
avg_price = total_price / len(price_dict)
print(avg_price)

#OR

total_price = 0

for price in price_dict.values():
    total_price += price

#print(total_price)

average_price = total_price / len(price_dict)
print("Average_price",average_price)

# Max and Min price product
max_price_product = max(price_dict, key=price_dict.get)
min_price_product = min(price_dict, key=price_dict.get)

print(max_price_product, price_dict[max_price_product])
print(min_price_product, price_dict[min_price_product])
print(max_price_product, min_price_product)

# Task 4: Combined Operations

#print(products)
#print(price_dict)
#print(categories)

# Catalog where each tuple is (product_name, price, category)
catalog = []

for i in range(len(products)):
    product = products[i]
    price = price_dict.get(product)
    category = categories[i]
    catalog.append((product, price, category))

print(catalog)

# Category_to_products dict
category_to_products = {}
for product, price, category in catalog:
    if category not in category_to_products:
        category_to_products[category] = []

    category_to_products[category].append(product)

print(category_to_products)

# Category that has maximum number of products
max_category = None
max_count = 0

for category, products in category_to_products.items():
    if len(products) > max_count:
        max_count = len(products)
        max_category = category

print("Category with maximum products:", max_category)
print("Products:", category_to_products[max_category])

