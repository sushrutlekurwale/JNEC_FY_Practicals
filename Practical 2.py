# Q:1 Write a program to simulate a simple calculator (+ - / * %) that takes two operands as an input and displays the result

# Q:2 Write a program to find area and perimeter of geometric objects
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
  

# Q:3 The distance between two cities (in km.) is input through the keyboard. Write a program to convert and print this distance in metres, feets, inches and centimetres
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

  

# Q:4 Write a program to interchange two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
temp = a
a = b
b = temp
print("Interchanged numbers are as follows \n First number: ", a, "\n Second number: ", b)


# Q:5 Write a program to compute Fahrenheit from centigrade (f = 1.8 * c + 32)
c = int(input("Enter the temperature in Centigrade: "))
f = (1.8 * c) + 32
print("Temperature in Fahrenheit: ", f )
