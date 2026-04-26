# Variables & data types
name = "Muneeb"
age = 18
gpa = 3.7
is_enrolled = True
print(f"{name} is {age} years old, GPA: {gpa}, Enrolled: {is_enrolled}")

# Logical operators
has_ticket = False

if age > 18 and has_ticket:
    print("VIP entry")
else:
    print("Denied")

if age > 18 or has_ticket:
    print("Can enter")
else:
    print("Cannot enter")

print(not has_ticket)

# Identity vs equality
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(x == y)
print(x is y)
print(x == z)
print(x is z)