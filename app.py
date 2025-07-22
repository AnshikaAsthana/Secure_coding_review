#app.py

import os
import getpass

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")  # insecure input

    if username == "admin" and password == "admin123":  # hardcoded credentials
        print("Login successful!")
    else:
        print("Invalid credentials")

def execute_command():
    command = input("Enter a system command to run: ")
    os.system(command)  # vulnerable to command injection

def insecure_eval():
    expression = input("Enter an expression to evaluate: ")
    print(eval(expression))  # dangerous use of eval

def main():
    try:
        login()
        execute_command()
        insecure_eval()
    except:
        pass  # suppresses all errors

if __name__ == "__main__":
    main()
