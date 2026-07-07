# range(): Generates a sequence of numbers
print("1. Using range(5):")
for i in range(5):
    print(i, end=' ')
print("\n")

print("   Using range(2, 8, 2):") # start, stop (exclusive), step
for i in range(2, 8, 2):
    print(i, end=' ')
print("\n")

# len(): Returns the number of items in an object (length)
my_list = [10, 20, 30, 40, 50]
my_string = "Python"
print(f"2. Length of my_list: {len(my_list)}")
print(f"   Length of my_string: {len(my_string)}")

# type(): Returns the type of an object
my_variable = 123
my_another_variable = "hello"
print(f"3. Type of my_variable ({my_variable}): {type(my_variable)}")
print(f"   Type of my_another_variable ('{my_another_variable}'): {type(my_another_variable)}")
