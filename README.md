[Running] python -u "c:\Users\hp\Desktop\PYTHON WEEK7 ASSIGNMENT\list_report.py"
Numbered Shopping List:
1. bread
2. avocado
3. milk
4. sweet potatoes
5. tea

Items with more than 4 letters: 3
The longest item name is: sweet potatoes

[Done] exited with code=0 in 0.247 seconds

[Running] python -u "c:\Users\hp\Desktop\PYTHON WEEK7 ASSIGNMENT\list_warmup.py"
First fruit: apple
Last fruit: date
After append: ['apple', 'banana', 'cherry', 'date', 'elderberry']
After remove: ['apple', 'cherry', 'date', 'elderberry']
Remaining fruits count: 4

[Done] exited with code=0 in 0.406 seconds

[Running] python -u "c:\Users\hp\Desktop\PYTHON WEEK7 ASSIGNMENT\shopping_list.py"

Would you like to (add / remove / show / done)? 
[Done] exited with code=1 in 709.088 seconds


# PLP Python Week 7: Shopping List Manager

## File Descriptions
- **list_warmup.py**: Demonstrates basic list manipulation including indexing, appending, removing items, and checking length.
- **shopping_list.py**: An interactive command-line shopping list manager featuring robust membership checks to prevent runtime errors.
- **list_report.py**: Analyzes a collection of items using loops to display a numbered list, count long names, and determine the longest item.

## Reflection Question
**Why is it safer to check `in` before calling `.remove()`?**
Checking if an item exists using the `in` keyword before calling `.remove()` prevents the program from throwing a `ValueError` and crashing when a non-existent item is targeted. It allows the program to handle missing inputs gracefully by displaying a user-friendly message instead of terminating unexpectedly.