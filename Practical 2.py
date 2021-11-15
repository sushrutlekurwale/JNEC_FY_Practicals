

# Q: Write a program to find area and perimeter of geometric objects
obj = input("Enter the shape of object (circle/square/triangle/rectangle)")
if obj == 'circle':
  r = int(input("Enter the radius of a circle: "))
  print("The area of a circle is ", 3.14 * r * r)
  print("The circumference of a circle is ", 2 * 3.14 * r)
elif obj == 'square':
  s = int(input("Enter the side of a square: "))
  print("The area of a square is ", a * a)
  print("The perimeter of a square is ", 4 * a)
elif obj == 'triangle':
  b = int(input("Enter the base of a triangle: "))
  h = int(input("Enter the height of a triangle: "))
  s1 = int(input("Enter the side 1 of a triangle: "))
  s2 = int(input("Enter the side 2 of a triangle: "))
  print("The area of a triangle is ", (h * b) / 2)
  print("The perimeter of a triangle is ", s1 + S2 + b)
elif obj == 'rectangle':
  l = int(input("Enter the length of a rectangle: "))
  b = int(input("Enter the breadth of a rectangle: "))
  print("The area of a rectangle is ", l * b)
  print("The perimeter of a square is ", 2 (l * b))
else:
  print("Enter the valid shape!")
  

# Q: The distance between two cities (in km.) is input through the keyboard. Write a program to convert and print this distance in metres, feets, inches and centimetres
km = int(input("Enter the disance between two cities in kms: ")) 
unit = input("Enter the unit for conversion (metres/feet/inches/centimetres): ")
if unit == 'metres':
  print("The distance in metres: ", km * 1000)
elif unit == 'feets':
  print("The distance in feets: ", km * 3281)
elif unit == 'inches':
  print("The distance in inches: ", km * 39370)
elif unit == 'centimetres':
  print("The distance in centimetres: ", km * 100000)
else:
    print("Enter the valid unit!")

    
# Q: Write a program to interchange two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
temp = a
a = b
b = temp
print("Interchanged numbers are as follows \n First number: ", a, "\n Second number: ", b)


# Q: Write a program to compute Fahrenheit from centigrade (f = 1.8 * c + 32)
c = int(input("Enter the temperature in Centigrade: "))
f = (1.8 * c) + 32
print("Temperature in Fahrenheit: ", f )


# Q: Create a datatype identifier
a = 5
print("type of a:", type(a))
b = 5.0
print("type of b:", type(b))
c = 2 + 4j
print("type of c:", type(c))
d ='Name'
print("type of d:", type(d))
e = [2, 4, 4.5, "ABC"]
print("type of e:", type(e))
f = (4, 7.4, 'abc')
print("type of f:", type(f))

# Q:Print whether the number is positive, negative or zero
def number():
    num = int(input("Enter the number:"))
    if num > 0:
        print("The entered number is positive!")
    elif num < 0:
        print("The entered number is negative!")
    elif num == 0:
        print("The entered number is zero!")
        
number()


# Q: String operations
a = 'My name is Sushrut!'
b = 'My surname is Lekurwale!'
print(a[11:18]) 
print(a[9])
print(a + b)
print(a*10)

# Q: Tuple operations
t = ("hi", "python", 2, 'hello')
print(t[1:])
print(t)
print(t + t)
print(t * 3)
print(type(t))
print(t[2])

#Q: Dictionary operations
d = {1:'Jimmy', 2:'Alex', 3:'John', 4:'Mike'}
print("First name is: " + d[1] )
print("Second is: "+ d[4])
print(d)
print(d.keys())
print(d.values())

#Q: Set operations
set1 = {1, 2, 3} #same datatype
print(set1)
set1 = {1.0, 'Hello', (123, 124, 125)} #mixed datatypes
print(set1)
set1 = {1, 2, 3, 4, 3, 2} #no duplicates allowed!
print(set1)

# Q: Write a program to input the basic salary of an employee and calculate the gross salary according to the given conditions:
# Basic Salary <= 10000: HRA=20% DA=80%
# Basic Salary is between 10001 to 20000: HRA=25% DA=90% 
# Basic Salary >= 20001: HRA=10% DA=95%
bs = int(input("Enter the basic salary of an employee:"))
if bs <= 10000:
  hra = (20*bs)/100
  da = (80*bs)/100
  gs = bs + hra + da
elif bs >= 10001 && bs <= 20000:
  hra = (20*bs)/100
  da = (80*bs)/100
  gs = bs + hra + da
elif bs > 20000:
  hra = (20*bs)/100
  da = (80*bs)/100
  gs = bs + hra + da
else:
  print(Enter valid basic salary!)
  
 print("The gross salary of an employee:", gs)
  

# Q: If the ages of three brothers are input through the keyboard, write a program to determine the youngest and oldest of three brothers
age1 = int(input("The age of brother 1 is :"))


# Q: Write a program to calculate the overtime pay of employee, overtime is paid at the rate of Rs.12.00/hour for every hour worked above 40 hours. Assume that employee do not work for fractional hours


#Q: Calculator program (Perform operations using all arithmetic operators)
x = int(input("Enter first number: "))
y = int(input("Enter the second number: "))
op = input("Enter the operator: ")
if op == '+':
    print('x + y = ', x + y)
if op == '-':
    print ('x - y =' ,x - y)
if op == '/':
    print('x / y = ', x / y)
if op == '//':
    print('x // y = ', x // y)
if op == '*':
    print('x * y = ', x * y)
if op == '**':
    print('x ** y = ', x ** y)
if op == '%':
    print('x % y =', x % y)
    
#Q: Write a program to convert the given days into years, months and days
n = int(input("Enter the number of days:"))
print("The number of years: ", n/365)
print("The number of months: ", n/30)

#Q: Write a program to convert a given seconds into hours, minutes and seconds
n = int(input("Enter the number of seconds:"))
print("The number of hours: ", int(n/3600))
print("The number of minutes: ", int(n/60))

#Q: Write a program to read an amount (in Rs.) and break the amount into smallest possible number of bank notes. The possible bank notes are: 100, 50, 20, 10, 5, 2, 1.
a = int(input("Enter the amount: "))
print("The number of notes of Rs.100: ", a//100)
print("The number of notes of Rs.50: ", a//50)
print("The number of notes of Rs.20: ", a//20)
print("The number of notes of Rs.10: ", a//10)
print("The number of notes of Rs.5: ", a//5)
print("The number of notes of Rs.2: ", a//2)
print("The number of notes of Rs.1: ", a//1)

#Q: Print the limited no. of Floating point objects
n = 12.45
n2 =34.67
sum = n + n2
print("The sum is: ", sum)
print("The sum is %.2f"%sum)
print("The sum is %.2d"%sum)
