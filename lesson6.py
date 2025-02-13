# try:
#     print("start code")
#     print(abc)
#     print(10/0)
#     print("No errors")
# except NameError:
#     print("We have an NameError")
# except ZeroDivisionError as error:
#     print(error)
# print("code after capsule")
try:
    print("start")
    print(start)
    print("No errors")
except (SyntaxError,NameError) as error:
    print(error)
else:
    print("I am ELSE")
finally:
    print("Finally code")