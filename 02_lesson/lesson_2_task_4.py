def fizz_buzz(number):
    for show_n in range(1, number + 1):
        if show_n % 3 == 0 and show_n % 5 == 0:
            print("FizzBuzz")
        elif show_n % 3 == 0:
            print("Fizz")
        elif show_n % 5 == 0:
            print("Buzz")
        else:
            print(show_n)

fizz_buzz(15)