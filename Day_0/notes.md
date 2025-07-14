### Python Basics
- Python is a high-level, interpreted programming language

### Variables, Data Types, and Operators
- Variables are used to store data
- Data types define the type of data that can be stored in a variable
- Operators are used to perform operations on data

### Control Structures
- Control structures are used to control the flow of execution in a program
- Conditional statements (if, elif, else) are used to make decisions based on conditions
- Loops (for, while) are used to repeat a block of code multiple times

```python
# Example of a conditional statement
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")
```

```python
# Example of a loop
for i in range(5):
    print(i)
```

### Functions
- Functions are used to group a set of statements together
- Functions can take input parameters and return output values

```python
# Example of a function
def add(x, y):
    return x + y

result = add(3, 5)
print(result)
```

### Data Structures
- Data structures are used to store and organize data
- Common data structures include lists, tuples, sets, and dictionaries

### Understanding Lists
- Lists are ordered collections of items
- Lists can contain items of different data types

#### List Operations
```python
# Example of adding an item to a list
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)
```
```python
# Example of removing an item from a list
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana") 
```
```python
# Example of sorting a list
fruits = ["apple", "banana", "cherry"]
fruits.sort()
print(fruits)
```
### Understanding Tuples
- Tuples are ordered collections of items
- Tuples can contain items of different data types

#### Tuple Operations   
```python
# Example of adding an item to a tuple
coordinates = (10, 20)
coordinates += (30, 40)
print(coordinates)  
```
```python   
# Example of removing an item from a tuple
coordinates = (10, 20, 30, 40)
coordinates.remove(30)
print(coordinates)
```
```python   
# Example of sorting a tuple
coordinates = (10, 20, 30, 40)
coordinates.sort()
print(coordinates)
```
### Understanding Sets
- Sets are unordered collections of unique items
- Sets can contain items of different data types

#### Set Operations   
```python
# Example of adding an item to a set
numbers = {1, 2, 3, 4, 5}   
numbers.add(6)   
print(numbers)
```   
```python   
# Example of removing an item from a set    
numbers = {1, 2, 3, 4, 5}   
numbers.remove(3)   
print(numbers)   
```   
```python   
# Example of sorting a set   
numbers = {1, 2, 3, 4, 5}   
numbers.sort()
print(numbers)
```
### Understanding Dictionaries
- Dictionaries are unordered collections of key-value pairs
- Dictionaries can contain items of different data types

#### Dictionary Operations  
```python   
# Example of adding an item to a dictionary   
person = {"name": "John", "age": 30, "city": "New York"}   
person["occupation"] = "Engineer"   
print(person)   
```   
```python   
# Example of removing an item from a dictionary   
person = {"name": "John", "age": 30, "city": "New York"}   
del person["age"]   
print(person)   
```   
```python   
# Example of sorting a dictionary   
person = {"name": "John", "age": 30, "city": "New York"}   
person.sort()   
print(person)   
```
### Understanding File I/O
### File I/O
- File I/O allows you to read from and write to files on your computer
- File I/O is useful for storing and retrieving data

```python
# Example of reading from a file
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
```

```python
# Example of writing to a file
with open("data.txt", "w") as file:
    file.write("Hello, world!")
```

### Error Handling
- Error handling allows you to handle and recover from errors that occur during program execution
- Error handling is important for robust and reliable programs

```python
# Example of error handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero")
```

