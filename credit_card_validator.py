"""
Credit Card Validator using Luhn Algorithm
==========================================

This program validates credit card numbers using the Luhn algorithm (also known as the "modulus 10" algorithm).
The Luhn algorithm is widely used to validate various identification numbers, including credit card numbers.

Learning Project from FreeCodeCamp
Author: [Your Name]
Date: June 2025

How the Luhn Algorithm Works:
1. Starting from the rightmost digit (excluding check digit), double every second digit
2. If doubling results in a number >= 10, add the digits of that number
3. Sum all the digits (both doubled and non-doubled)
4. If the total sum is divisible by 10, the card number is valid

Example with card number 4111-1111-4555-1141:
- Reversed: 1415554111111114
- Odd positions (1st, 3rd, 5th...): 1, 1, 5, 4, 1, 1, 1, 1 = 15
- Even positions doubled: 4*2=8, 5*2=10→1+0=1, 5*2=10→1+0=1, 5*2=10→1+0=1, 1*2=2, 1*2=2, 1*2=2, 1*2=2 = 18
- Total: 15 + 18 = 33, 33 % 10 = 3 ≠ 0, so INVALID (but this is just an example)
"""

def verify_card_number(card_number):
    """
    Validates a credit card number using the Luhn algorithm.
    
    Args:
        card_number (str): Credit card number as a string (digits only)
    
    Returns:
        bool: True if the card number is valid, False otherwise
    
    Algorithm Steps:
    1. Reverse the card number to process from right to left
    2. Sum digits at odd positions (1st, 3rd, 5th, etc. from right)
    3. Double digits at even positions (2nd, 4th, 6th, etc. from right)
    4. If doubled digit >= 10, add its individual digits (e.g., 14 → 1+4=5)
    5. Sum all processed digits
    6. Return True if sum is divisible by 10
    """
    
    # Step 1: Initialize sum for odd positioned digits
    sum_of_odd_digits = 0
    
    # Step 2: Reverse the card number to process from right to left
    card_number_reversed = card_number[::-1]
    
    # Step 3: Extract digits at odd positions (1st, 3rd, 5th, etc.)
    # In reversed string, these are at indices 0, 2, 4, etc.
    odd_digits = card_number_reversed[::2]
    
    # Step 4: Sum all odd positioned digits
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)
    
    # Step 5: Process even positioned digits (2nd, 4th, 6th, etc.)
    sum_of_even_digits = 0
    # In reversed string, these are at indices 1, 3, 5, etc.
    even_digits = card_number_reversed[1::2]
    
    for digit in even_digits:
        # Double the digit
        doubled_number = int(digit) * 2
        
        # If doubled number is >= 10, add its digits
        # Example: 14 becomes 1 + 4 = 5
        if doubled_number >= 10:
            doubled_number = (doubled_number // 10) + (doubled_number % 10)
        
        sum_of_even_digits += doubled_number
    
    # Step 6: Calculate total sum
    total_sum = sum_of_odd_digits + sum_of_even_digits
    
    # Debug: Print the total sum (remove this in production)
    print(f"Total sum: {total_sum}")
    
    # Step 7: Check if sum is divisible by 10
    return total_sum % 10 == 0


def clean_card_number(card_number):
    """
    Removes spaces and hyphens from card number string.
    
    Args:
        card_number (str): Raw card number with possible spaces/hyphens
    
    Returns:
        str: Cleaned card number with only digits
    """
    # Create translation table to remove spaces and hyphens
    card_translation = str.maketrans({'-': '', ' ': ''})
    return card_number.translate(card_translation)


def main():
    """
    Main function to demonstrate credit card validation.
    """
    print("Credit Card Validator - Luhn Algorithm")
    print("=" * 40)
    
    # Test card number (this is a test number, not a real credit card)
    card_number = '4111-1111-4555-1141'
    print(f"Testing card number: {card_number}")
    
    # Clean the card number (remove spaces and hyphens)
    cleaned_card_number = clean_card_number(card_number)
    print(f"Cleaned card number: {cleaned_card_number}")
    
    # Validate the card number
    if verify_card_number(cleaned_card_number):
        print('✅ VALID! This card number passes the Luhn algorithm.')
    else:
        print('❌ INVALID! This card number fails the Luhn algorithm.')
    
    print("\nNote: This only validates the format, not whether the card actually exists.")


# Additional test cases for learning purposes
def run_test_cases():
    """
    Test the validator with known valid and invalid card numbers.
    """
    print("\n" + "=" * 50)
    print("RUNNING TEST CASES")
    print("=" * 50)
    
    test_cards = [
        ("4532015112830366", "Valid Visa"),
        ("4111111111111111", "Valid Visa (test card)"),
        ("4111111111111112", "Invalid Visa"),
        ("5555555555554444", "Valid Mastercard (test card)"),
        ("1234567890123456", "Invalid number"),
    ]
    
    for card, description in test_cards:
        result = "VALID" if verify_card_number(card) else "INVALID"
        print(f"{description}: {card} → {result}")


if __name__ == "__main__":
    main()
    
    # Uncomment the line below to run additional test cases
    # run_test_cases()
