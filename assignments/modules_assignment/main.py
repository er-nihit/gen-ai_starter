## 1. Using Functions from math_utils.py
import math_utils
from math_utils import square

# Using functions from imported math_utils
print("5 + 10 =",math_utils.sum(5,10))
print("20 - 2 =",math_utils.subtract(20,2))

# Using function which was directly imported from math_utils
print("Square of 6 =",square(6))


## 2. Using functions from string_utils.py
import string_utils

print("Capitalizing 'hello':",string_utils.capilatize_words("Hello"))
print("Reversing word 'America':",string_utils.reverse_string("America"))
print("Word count of statement 'This is Gen AI Course':",string_utils.word_count("This is Gen AI Course"))

## 4. Using shop_package module
import shop_package.discount as disc
from shop_package.billing import calculate_total
from shop_package.billing import apply_tax as tax

print("5% Percent discount on 1000: ",disc.apply_discount(1000,5))
print("Flat discount in 5000: ",disc.flat_discount(5000))
print("Calculate Total of 100, 200, 500:",calculate_total([100,200,500]))
print("Apply Tax on 3000:",tax(3000))
