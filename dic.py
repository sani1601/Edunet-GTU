# Re-initializing dict_1 for fresh examples
dict_1 = {"name": "Alice", "age": 30, "city": "New York"}
print(f"Initial Dictionary: {dict_1}")

# 1. get(): Safely retrieve value, returns None or default if key not found
print(f"1. Using get('name'): {dict_1.get('name')}")
print(f"   Using get('country', 'USA'): {dict_1.get('country', 'USA')}")

# 2. pop(): Removes item with specified key and returns its value
age_popped = dict_1.pop('age')
print(f"2. After pop('age'): {dict_1}, Popped age: {age_popped}")

# 3. popitem(): Removes and returns an arbitrary (key, value) pair
item_popped = dict_1.popitem()
print(f"3. After popitem(): {dict_1}, Popped item: {item_popped}")

# 4. setdefault(): Inserts key with a value if key is not already present.
#    If the key is present, it does nothing and returns the existing value.
dict_1.setdefault('city', 'London')
dict_1.setdefault('occupation', 'Engineer')
print(f"4. After setdefault: {dict_1}")

# 5. clear(): Removes all items from the dictionary
dict_1.clear()
print(f"5. After clear(): {dict_1}")
