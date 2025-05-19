# if,else,if else, if else if
# Comparison & Logical Operators

# Simple if
print("Example of simple if")
temperature = 12
if temperature < 15:
    print('It is a cold day')

print("Example of if and else")
age = 25
if age >= 18:
    print("He is an adult")
else:
    print("He is an minor")

age = 15
if age >= 18:
    print("He is an adult")
else:
    print("He is an minor")

print("Example of if elif and else")

mark = 80
if mark <= 100 and mark <= 90:
    print("Grade is A+")
elif mark <= 89 and mark <= 70:
    print("Grade is A")
elif mark <= 50 and mark <=69:
    print("Grade is B")
else:
    print("D")
print("---------------------------------------------")

mark = -80
if mark <= 100 and mark >= 90:
    print("Grade is A+")
elif mark <= 89 and mark >= 70:
    print("Grade is A")
elif mark <= 50 and mark >=69:
    print("Grade is B")
else:
    print("D")
