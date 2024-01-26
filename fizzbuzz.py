x = 0
while (x <= 20):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    if x % 3 == 0:
        print("Fizz")
    if x % 5 == 0:
        print("Buzz")
    x+1
