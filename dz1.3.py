score = int(input("Введіть кількість балів (0-100): "))
def get_grade(score):
    if 0 <= score <= 49:
        print("незадовільно")
    elif 50 <= score <= 69:
        print("задовільно")
    elif 70 <= score <= 89:
        print("добре")
    elif 90 <= score <= 100:
        print("відмінно")
    else:
        print("Неправельний ввід. Введіть число від 0 до 100.")

print("Оцінка:")
print(get_grade(score))