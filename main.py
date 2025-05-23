# user_name = parameter
# "=" is default parameter
def say_hello(user_name="anonymous", user_age=0):
  print("hello", user_name, "how are you?")
  print(user_name, "is", user_age, "years old.")


# tami = argument
say_hello("tami", 20)
say_hello()


# calculator
def plus(a=0, b=0):
  print(a + b)

def minus(a=0, b=0):
  print(a - b)

def multiply(a=0, b=0):
  print(a * b)

def divide(a=0, b=1):
  print(a / b)

def power(a=0, b=1):
  print(a ** b)

plus(3, 4)
minus(5, 3)
multiply(2, 8)
divide(6, 3)
power(3, 3)

plus()
minus()
multiply()
divide()
power()