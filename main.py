"""
Simple Calculator Application - Main Program
"""
from calculator import Calculator
from utils import display_menu, get_user_choice, get_numbers

def main():
    calc = Calculator()
    
    print("=" * 40)
    print("Welcome to Simple Calculator!")
    print("=" * 40)
    
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == '5':
            print("\nThank you for using the calculator. Goodbye!")
            break
        
        num1, num2 = get_numbers()
        
        if choice == '1':
            result = calc.add(num1, num2)
            print(f"\n{num1} + {num2} = {result}")
        elif choice == '2':
            result = calc.subtract(num1, num2)
            print(f"\n{num1} - {num2} = {result}")
        elif choice == '3':
            result = calc.multiply(num1, num2)
            print(f"\n{num1} × {num2} = {result}")
        elif choice == '4':
            result = calc.divide(num1, num2)
            if result is not None:
                print(f"\n{num1} ÷ {num2} = {result}")
        
        print()

if __name__ == "__main__":
    main()