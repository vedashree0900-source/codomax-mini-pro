# Calculator Program
def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")

    while True:
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                if num2 == 0:
                    print("Error: Division by zero!")
                    continue
                result = num1 / num2
            else:
                print("Invalid operator!")
                continue

            print(f"Result: {result}")

        except ValueError:
            print("Invalid number entered!")

        again = input("Calculate again? (y/n): ")
        if again.lower() != 'y':
            break

if __name__ == "__main__":
    calculator()
quit




# Guessing Game
import random

def guessing_game():
    number = random.randint(1, 100)
    attempts = 0
    print("Guess the number between 1 and 100!")

    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1

            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(f"Correct! You got it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guessing_game()



# Student Grade Calculator
def grade_calculator():
    name = input("Enter student name: ")
    num_subjects = int(input("Enter number of subjects: "))

    total = 0
    for i in range(num_subjects):
        marks = float(input(f"Enter marks for subject {i+1}: "))
        total += marks

    average = total / num_subjects

    if average >= 90:
        grade = 'A'
    elif average >= 75:
        grade = 'B'
    elif average >= 60:
        grade = 'C'
    elif average >= 40:
        grade = 'D'
    else:
        grade = 'F'

    print(f"\nStudent: {name}")
    print(f"Total Marks: {total}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    grade_calculator()



# Expense Tracker
expenses = []

def add_expense():
    desc = input("Expense description: ")
    amount = float(input("Amount: "))
    expenses.append({"description": desc, "amount": amount})
    print("Expense added!\n")

def view_expenses():
    if not expenses:
        print("No expenses recorded.\n")
        return
    total = 0
    print("\n--- Expenses ---")
    for i, e in enumerate(expenses, 1):
        print(f"{i}. {e['description']} - ${e['amount']:.2f}")
        total += e['amount']
    print(f"Total: ${total:.2f}\n")

def expense_tracker():
    while True:
        print("1. Add Expense\n2. View Expenses\n3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            break
        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    expense_tracker()



# Password Generator
import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    try:
        length = int(input("Enter desired password length (default 12): ") or 12)
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input, using default length of 12.")
        print(f"Generated Password: {generate_password()}")

if __name__ == "__main__":
    password_generator()