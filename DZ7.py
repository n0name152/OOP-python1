def checker(function):
    def checker(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except Exception as exc:
            print(f"We have problems {exc}")
        else:
            print(f"No problems. Result – {result}")
    return checker

@checker
def calculate(expression):
    return eval(expression)

num1 = input("Put number your number: ")
num2 = input("Put number your number: ")
calculate(f"{num1} + {num2}")