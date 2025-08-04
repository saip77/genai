print("Hello World")

### Variables
x = 10
y = 20
z = x + y
print(z)

### Conditionals
x = int(input("Enter a number: "))
y = 15
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equal to y")

### Loops
for i in range(10):
    print(i)

while x < 20:
    x += 1
    print(x)

### Functions
def add(x, y):
    return x + y

print(add(10, 20))