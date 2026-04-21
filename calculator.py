def calculate():
    print("--- Simple Python Calculator ---")
    print("Select operation: +, -, *, /")
    
    while True:
        operator = input("\nEnter operator (or 'q' to quit): ")
        
        if operator.lower() == 'q':
            print("Exiting calculator. Goodbye!")
            break

        if operator in ('+', '-', '*', '/'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if operator == '+':
                    print(f"Result: {num1} + {num2} = {num1 + num2}")
                elif operator == '-':
                    print(f"Result: {num1} - {num2} = {num1 - num2}")
                elif operator == '*':
                    print(f"Result: {num1} * {num2} = {num1 * num2}")
                elif operator == '/':
                    if num2 == 0:
                        print("Error! Division by zero.")
                    else:
                        print(f"Result: {num1} / {num2} = {num1 / num2}")
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        else:
            print("Invalid operator! Please use +, -, *, or /.")

if __name__ == "__main__":
    calculate()