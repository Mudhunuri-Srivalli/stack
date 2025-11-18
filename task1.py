Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #1.Assign two numbers to variables'a'and'b' and print their sum
>>> a=10
>>> b=20
>>> sum=a+b
>>> print("The sum of a and b is:",sum)
The sum of a and b is: 30
>>> #2. Write a Python program to subtract two numbers and print the result.
>>> a=15
>>> b=7
>>> result=a-b
>>> print("The result of subtraction is:",result)
The result of subtraction is: 8
>>> #3. Multiply two variables and store the result in a third variable. Print all three.
>>> a=6
>>> b=4
>>> c=a*b
>>> print("a=",a)
a= 6
>>> print("b=",b)
b= 4
>>> print("Multiplication result(c)=',c)
      
SyntaxError: EOL while scanning string literal
>>> print("Multiplication result(c)=",c)
Multiplication result(c)= 24
>>> #4.Divide 10 by 3 and print the result with and without decimals.
>>> result_with_decimal=10/3
>>> print("With decimals:",result_with_decimal)
With decimals: 3.3333333333333335
>>> result_without_decimal=10//3
>>> print("Without_decimal:",result_without_decimal)
Without_decimal: 3
>>> #5.Use floor division `//` to divide 17 by 4. Print the output.
>>> result=17//4
>>> print("Floor division result:",result)
Floor division result: 4
>>> #6. Use the modulo operator `%` to check the remainder when 25 is divided by 6.
>>> remainder=25%6
>>> print("Remainder:",remainder)
Remainder: 1
>>> #7. Calculate and print the square of a number stored in a variable.
>>> num=7
>>> square=num**2
>>> print("Square of",num,"is",square)
Square of 7 is 49
>>> #8. Assign values to three variables `x`, `y`, `z` and compute the average.
>>> x=10
>>> y=20
>>> z=30
>>> average=(x+y+z)/3
>>> print("Average is:",average)
Average is: 20.0
>>> #9. Take a number and find its cube using the `**` operator.
>>> number=5
>>> cube=number**3
>>> print('cube of",number,"is",cube)
      
SyntaxError: EOL while scanning string literal
>>> print("cube of",number,"is",cube)
cube of 5 is 125
>>> #10. Create two variables `length` and `width`. Calculate and print area of a rectangle.
>>> length=8
>>> width=5
>>> area=length*width
>>> print("Area of rectangle:",area)
Area of rectangle: 40
>>> #11. Assign a variable `total_marks = 450` and `obtained_marks = 375`. Find percentage.
>>> total_marks=450
>>> obtained_marks=375
>>> percentage=(obtained_marks/total_marks)*100
>>> print("percentage:",percentage)
percentage: 83.33333333333334
>>> #12. Write a Python statement that calculates `(a + b) * c` for some values of a, b, and c.
>>> 
>>> 
>>> a=10
>>> b=3
>>> c=4
>>> result=(a+b)*c
>>> print("Result of(a+b)*c=",result)
Result of(a+b)*c= 52
>>> #13. Draw and show how reassignment changes variable reference to a memory block.
>>> x=10
>>> y=20
>>> x->[10]
SyntaxError: invalid syntax
>>> x->[10]
SyntaxError: invalid syntax
>>> 