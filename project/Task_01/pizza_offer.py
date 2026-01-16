#!/usr/bin/env python3
"""
Pizza Pricing Program - Task 1
Beckett Pizza Plaza 4-for-3 Offer
Author: Aadit kumar singh
"""

import sys

# Function to validate user input and ensure it is a positive number
def get_price_input(prompt):
    while True:
        try:
            price = float(input(prompt))
            if price <= 0:
                print("Please enter a valid price!")
                continue
            return price
        except ValueError:
            print("Please enter a valid number!")

# Function to calculate total and discount
def calculate_total(prices):
    # Find the cheapest pizza
    cheapest = min(prices)
    # Total is sum minus cheapest pizza
    total = sum(prices) - cheapest
    # Calculate discount percentage
    discount = (cheapest / sum(prices)) * 100
    return total, discount

# Function to read prices from a file
def read_prices_from_file(filename):
    prices = []
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if line == "":
                    continue
                price = float(line)
                if price <= 0:
                    print(f"Invalid price in file: {line}")
                    continue
                prices.append(price)
        if len(prices) != 4:
            print("File must contain exactly 4 valid prices!")
            return None
        return prices
    except FileNotFoundError:
        print(f"File '{filename}' not found!")
        return None
    except ValueError as e:
        print(f"Invalid number in file: {e}")
        return None

# Main program function
def main():
    print("Beckett Pizza Plaza 4-for-3 Offer")
    print("=================================")

    # Check if user passed a filename as command line argument
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        prices = read_prices_from_file(filename)
        if prices is None:
            # If file failed, exit program
            return
    else:
        # Otherwise, ask user to input prices manually
        prices = []
        for i in range(4):
            price = get_price_input(f"Enter Price of Pizza #{i+1}: ")
            prices.append(price)

    # Calculate total and discount
    total, discount = calculate_total(prices)

    # Display result with 2 decimal points
    print(f"Order Total is £{total:.2f}, a fabulous discount of {discount:.0f}%!")

# Run main() if this script is executed
if __name__ == "__main__":
    main()
