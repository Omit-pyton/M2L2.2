# творіть функцію, яка приймає два числа від користувача та обробляє помилку, якщо введені дані не є числами.

try:
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    print("All right")

except ValueError:
    print("You choice is not a number")
