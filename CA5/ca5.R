# CA5 part A - is designed to test your R skills, .
# Take your calculator program from CA1 and implement it as a set of 10 functions in R.
# Submit an R script of your program to moodle and github.
# Also submit some calls to prove your 10 functions work.

# 1. Funciton to compute the sum of two numbers.
add<-function(x,y)
{
  x+y  #  add 2 floats
}

x<-4
y<-5
add(x,y)

# 2. Funciton to compute the difference of two numbers.
subtract<-function(x, y)
{
  x - y
}

x<-4
y<-5
subtract(x,y)

# 3. Funciton to compute the product of two numbers.
multiply<-function(x, y)
{
  x * y
}

x<-4
y<-5
multiply(x,y)
  
# 4. Funciton to compute the division of two numbers.
divide<-function(x, y)    
{
  if(y!=0)
    x / y
  else 
    NaN
}

x<-4
y<-2
divide(x,y)

x<-4
y<-0
divide(x,y)

# 5. Funciton to compute the power of on number to another.
power<-function(x, y) 
{
x**y
}

x<-2
y<-2
power(x,y)

x<-2
y<--1
power(x,y)

x<-2
y<-0
power(x,y)

# 6. Funciton to compute the square of a number.
square<-function(x)
{
  x*x
}
 
x<-2
square(x)

x<-0.5
square(x)

x<-2
square(x)

# 7. Funciton to compute the sine of a number.
sin_func<-function(x)
{
  sin(x) 
}

sin_func(pi)
sin_func(90)

# 8. Funciton to compute the cosine of a number.
cos_func<-function(x)
{
  cos(x) 
}

cos_func(pi)
cos_func(90)

# 9. Funciton to compute the tangent of a number.
tan_func<-function(x)
{
  tan(x) 
}

tan_func(pi)
tan_func(90)

# 10. Funciton to compute the log of a number to a specified base.
logarithm<-function(x,base)
{
  log(x,base) 
}

logarithm(1,2)
logarithm(0,10)
logarithm(0.5,3)

calc<-function()
{
  # take input from the user
  print("Welcome to the calculator!")
  print("Please select an operation from the following options:")
  print("1.Add")
  print("2.Subtract")
  print("3.Multiply")
  print("4.Divide")
  print("5.Power")
  print("6.Square")
  print("7.Sin")
  print("8.Cos")
  print("9.Tan")
  print("10.Log")
  print("11 to Quit")
  
  c = readline(prompt="Enter choice[1/2/3/4/5/6/7/8/9/10/11]: ")
  if (c == "Q") 
  {
    return ("Thank you for using the calculator!")
  } else 
  {
    c = as.integer(c)
    if ((c == 1)|(c ==2)|(c ==3)|(c ==4)|(c ==5))
    {
      print("First")
      num1 = as.numeric(readline(prompt="Please enter first number: "))
      num2 = as.numeric(readline(prompt="Please enter second number: "))
      operator <- switch(c,"+","-","*","/","^","^2","sin","cos","tan","log")
      result <- switch(c, add(num1, num2), subtract(num1, num2), multiply(num1, num2), divide(num1, num2), power(num1, num2),square(num),sin_func(num), cos_func(num), tan_func(num),logarithm(num,base))
      print(paste(num1, operator, num2, "=", result, sep = " ")) 
    } else if (c == 6) 
    {
      print("Second")
      num = as.numeric(readline(prompt="Please enter a number: "))
      operator <- switch(c,"+","-","*","/","^","^2","sin","cos","tan","log")
      result <- switch(c, add(num1, num2), subtract(num1, num2), multiply(num1, num2), divide(num1, num2), power(num1, num2),square(num),sin_func(num), cos_func(num), tan_func(num),logarithm(num,base))
      print(paste(num, operator, "=", result, sep = " ")) 
    } else if ((c == 7)|(c == 8)|(c == 9))
    {
      print("Third")
      num = as.numeric(readline(prompt="Please enter a number in radians: "))
      operator <- switch(c,"+","-","*","/","^","^2","sin","cos","tan","log")
      result <- switch(c, add(num1, num2), subtract(num1, num2), multiply(num1, num2), divide(num1, num2), power(num1, num2),square(num),sin_func(num), cos_func(num), tan_func(num),logarithm(num,base))
      print(paste(operator, num,  "=", result, sep = " ")) 
    } else if (c == 10)
    {
      print("Fourth")
      num = as.numeric(readline(prompt="Please enter a number: "))
      base = as.integer(readline(prompt="Please enter the log base: "))
      operator <- switch(c,"+","-","*","/","^","^2","sin","cos","tan","log")
      result <- switch(c, add(num1, num2), subtract(num1, num2), multiply(num1, num2), divide(num1, num2), power(num1, num2),square(num),sin_func(num), cos_func(num), tan_func(num),logarithm(num,base))
      print(paste(operator, " of ", num, " to the base ", base, " = ", result)) 
    } 
  }
}

calc()