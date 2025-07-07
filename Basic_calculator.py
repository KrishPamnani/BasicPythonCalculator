def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "INVALID: Division by zero is not possible. Choose another number."
    return x / y

def main():
    print("Welcome to your personal Calculator!")
    print("Select an operation:")
    print("  1. Addition (+)")
    print("  2. Subtraction (-)")
    print("  3. Multiplication (*)")
    print("  4. Division (÷)")
    print("  5. Others (coming soon)")
    print("  q. Quit")

    while True:
        choice = input("\nEnter choice (1/2/3/4/5) or 'q' to quit: ").strip()

        if choice.lower() == 'q':
            print("Goodbye!.,Visit Again!!")
            break

        if choice not in {'1', '2', '3', '4', '5'}:
            print("Invalid option. Please choose from 1–5 or 'q'.")
            continue

        if choice == '5':
            print("Stay tuned for more operations!")
            continue

        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
        except ValueError:
            print("Invalid entry. Please enter numeric values.")
            continue

        
        if choice == '1':
            result = addition (num1, num2)
            operator = '+'
        elif choice == '2':
            result = subtraction (num1, num2)
            operator = '-'
        elif choice == '3':
            result = multiplication (num1, num2)
            operator = '*'
        else:  
            result = division (num1, num2)
            operator = '÷'

       
        print(f"\nResult: {num1} {operator} {num2} = {result}")

if __name__ == "__main__":
    main()