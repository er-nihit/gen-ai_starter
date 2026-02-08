# Assignment 1.1: Lists and Tuples
# Author: Nihit Kumar
# Date: 2025-02-09
#


# 1. Create a list named products containing at least 6 product names
products = ["Laptop", "Mobile Phone", "Headphones", "Keyboard", "Mouse", "Monitor"]
print("Product list:", products)

# 2. Create a tuple named sample_product with (product_name, price, category)
laptop_tup = ("HP Elitebook", 60000.00, "Laptop")
print("Sample product (tuple):", laptop_tup)

# 3. Print the 2nd and last product from the products list
print("2nd product from the list:", products[1])
print("Last product from the list:", products[-1])

# 4. Append two new product names to products and then print the updated list
products.append("Webcam")
products.append("USB Cable")
print("Updated products list after appending:", products)

# 5. Extra: Convert sample_product into a list, change its price, and convert back to tuple
# Convert tuple to list
laptop_list = list(laptop_tup)
print("Confirming type: ",type(laptop_list))
laptop_list[1] = 70000.00

# Convert back to tuple
laptop_tup = tuple(laptop_list)
print("Converted back to tuple:", type(laptop_tup))
