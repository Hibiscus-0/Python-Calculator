"""
Utility functions for the calculator application
"""

def display_menu():
    """Display the calculator menu"""
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

def get_user_choice():
    """Get and validate user's menu choice"""
    while True:
        choice = input("\nEnter choice (1/2/3/4/5): ")
        if choice in ['1', '2', '3', '4', '5']:
            return choice
        print("Invalid input. Please enter a number between 1 and 5.")

def get_numbers():
    """Get two numbers from the user"""
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter valid numbers.")