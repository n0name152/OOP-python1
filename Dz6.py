result = []
def divider(a, b):
  try:
    if a < b:
     print("b більша за a")
     raise ValueError
    if b > 100:
     print("b більша за 100")
     raise IndexError
    return a / b
  except (TypeError,ValueError,IndexError,ZeroDivisionError) as error:
    print(error)
  return None
data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key in data:
  res = divider(key, data[key])
  result.append(res)

print(result)