# Gen AI Starter - Data Structures Assignment

A comprehensive Python assignment exploring fundamental data structures including lists, tuples, sets, and dictionaries with practical examples.

## 📁 Project Structure

```
gen-ai_starter/
├── assignments/
│   └── data_structures_assignment.ipynb
├── README.md
└── .gitignore
```

## 📚 Assignment Overview

This project contains **Assignment 1: Python - Data Structures**, which covers four core tasks demonstrating essential Python data structures and operations.

### Task 1: Product Collections (Lists and Tuples)

**Objective**: Understand lists and tuples, their properties, and basic operations.

**Key Concepts**:
- Creating lists with multiple product names
- Creating tuples with heterogeneous data (product name, price, category)
- List indexing (positive and negative indices)
- List mutation (append operation)
- Type conversion between tuples and lists

**Example Output**:
```
Product list: ['Laptop', 'Mobile Phone', 'Headphones', 'Keyboard', 'Mouse', 'Monitor']
2nd product: Mobile Phone
Last product: Monitor
Updated list (after appending): [..., 'Webcam', 'USB Cable']
```

---

### Task 2: Categories (Sets)

**Objective**: Learn set operations and understand sets' unique properties.

**Key Concepts**:
- Creating sets from lists (automatically removes duplicates)
- Adding new elements to sets (.add() method)
- Set membership testing (in operator)
- Checking set size (.len() function)
- Understanding set immutability of elements

**Demonstrations**:
- Creating a `categories_set` from a list of categories
- Adding new categories and showing duplicates are automatically ignored
- Membership checks returning boolean values (True/False)
- Counting unique categories

**Example Output**:
```
Categories set: {'Electronics', 'Accessories'}
After adding 'Home & Garden': {'Electronics', 'Accessories', 'Home & Garden'}
Does 'Electronics' exist? True
Total unique categories: 3
```

---

### Task 3: Product Pricing (Dictionaries)

**Objective**: Master dictionary operations for key-value data management.

**Key Concepts**:
- Creating dictionaries with product names as keys and prices as values
- Adding new key-value pairs
- Updating values for existing keys
- Removing items safely using .pop() with default values
- Dictionary iteration over values
- Finding max/min using dictionary operations

**Operations Demonstrated**:
1. Add new product: `price_dict["Webcam"] = 4500.00`
2. Update price: `price_dict["Laptop"] = 65000.00`
3. Remove product: `del price_dict["Mouse"]` or `.pop()`
4. Calculate average: `sum(values) / len(dict)`
5. Find max/min products by price

**Example Output**:
```
Initial dictionary: {'Laptop': 60000.0, 'Mobile Phone': 25000.0, ...}
After adding Webcam: {..., 'Webcam': 4500.0}
Average price: Rs. 17500.0
Product with max price: Laptop - Rs. 65000.0
Product with min price: Mouse - Rs. 1500.0
```

---

### Task 4: Combined Operations

**Objective**: Integrate multiple data structures for complex data manipulation.

**Key Concepts**:
- Combining lists, tuples, and dictionaries in a single data structure
- Creating a catalog as a list of tuples
- Building mappings from one structure to another
- Finding categories with maximum products
- Aggregating related data by categories

**Operations Demonstrated**:
1. **Catalog Creation**: Merge products, prices, and categories into tuples
   - Format: `(product_name, price, category)`
   
2. **Category Mapping**: Group products by category
   - Format: `{'category': [products]}`
   
3. **Analysis**: Find the category with the most products and display all items

**Example Output**:
```
Catalog (first 3 items):
- ('Laptop', 65000.0, 'Electronics')
- ('Mobile Phone', 25000.0, 'Electronics')
- ('Headphones', 5000.0, 'Electronics')

Category to Products: {'Electronics': [6 products], 'Accessories': [1 product]}

Products in 'Electronics' category (max count):
- Laptop (Price: Rs. 65000.00)
- Mobile Phone (Price: Rs. 25000.00)
...
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- Jupyter Notebook or JupyterLab
- Conda environment (recommended)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/er-nihit/gen-ai_starter.git
cd gen-ai_starter
```

2. Set up the conda environment:
```bash
conda create -n tutedude python=3.11
conda activate tutedude
```

3. Install Jupyter:
```bash
conda install jupyter
```

### Running the Assignment

1. Activate your conda environment:
```bash
conda activate tutedude
```

2. Start Jupyter Notebook:
```bash
jupyter notebook
```

3. Navigate to `assignments/data_structures_assignment.ipynb`

4. Run cells sequentially (Shift+Enter) to see outputs for each task

## 📝 Key Learnings

| Data Structure | Mutable | Ordered | Duplicates | Use Case |
|---|---|---|---|---|
| **List** | ✅ Yes | ✅ Yes | ✅ Allowed | Ordered collections, modifications |
| **Tuple** | ❌ No | ✅ Yes | ✅ Allowed | Immutable collections, safe structures |
| **Set** | ✅ Yes | ❌ No | ❌ No | Unique values, membership testing |
| **Dictionary** | ✅ Yes | ✅ Yes (3.7+) | Keys: No, Values: Yes | Key-value mappings, lookups |

## 💡 Code Highlights

### List Operations
```python
products = ["Laptop", "Mobile Phone", ...]
products.append("Webcam")  # Add to end
print(products[1])          # Access by index
print(products[-1])         # Negative indexing
```

### Set Operations
```python
categories_set = set(categories)
categories_set.add("Home & Garden")
print("Electronics" in categories_set)  # Membership test
```

### Dictionary Operations
```python
price_dict = {"Laptop": 60000.0, ...}
price_dict["Webcam"] = 4500.00       # Add
price_dict["Laptop"] = 65000.00      # Update
del price_dict["Mouse"]               # Remove
average = sum(price_dict.values()) / len(price_dict)
```

### Combined Operations
```python
catalog = [(name, price, category) for ...]
category_to_products = {cat: [products] for ...}
max_category = max(category_to_products, key=lambda c: len(...))
```

## 📄 Assignment Source

[View Assignment in Google Docs](https://docs.google.com/document/d/1ddgbgRVFMOPDXZpNac_O0GER04-yo2qcUXOVN3r2tYE/edit?tab=t.0)

## 👤 Author

- **Name**: Nihit Kumar
- **Date**: February 10, 2025
- **Status**: Complete ✅

## 🔗 Repository

- **Repository**: [er-nihit/gen-ai_starter](https://github.com/er-nihit/gen-ai_starter)
- **Main Branch**: Public (visible to all)
- **Lab Branch**: Private (local development only)

## 📖 Additional Resources

- [Python Lists Documentation](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Python Tuples Documentation](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
- [Python Sets Documentation](https://docs.python.org/3/tutorial/datastructures.html#sets)
- [Python Dictionaries Documentation](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

## 📜 License

This project is part of the Gen AI Starter course materials.

---

**Last Updated**: February 11, 2026
