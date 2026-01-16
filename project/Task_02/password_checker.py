#!/usr/bin/env python3
"""
Password Security Check Program - Task 2
Author: Aadit kumar singh
"""

import sys
import random

# Function to check password length
def check_length(password):
    if len(password) < 9:
        print("\nPassword too short.")
        return False
    return True

# Function to perform random letter checks
def check_letters(password):
    length = len(password)
    # Pick 3 random positions in the password (1-based indexing)
    positions = random.sample(range(1, length+1), 3)

    for pos in positions:
        # Ask user for letter at that position
        user_letter = input(f"\nEnter letter at position {pos}: ")
        # Check if the input matches the actual letter
        if user_letter == password[pos-1]:
            print("Correct")
        else:
            print("Security check failed.")
            return False
    return True

# Function to read password from a file (optional)
def read_password_from_file(filename):
    try:
        with open(filename, "r") as f:
            passwords = [line.strip() for line in f if line.strip()]
        return passwords
    except FileNotFoundError:
        print(f"File '{filename}' not found!")
        return None

# Main program
def main():
    # Check if a filename is provided as command-line argument
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        passwords = read_password_from_file(filename)
        if passwords is None:
            return
        for password in passwords:
            print(f"\nChecking password: {password}")
            if not check_length(password):
                continue
            if check_letters(password):
                print("\nSecurity check passed.")
    else:
        # Manual input
        password = input("Enter your password: ")
        if not check_length(password):
            return
        if check_letters(password):
            print("\nSecurity check passed.")

# Run program
if __name__ == "__main__":
    main()
