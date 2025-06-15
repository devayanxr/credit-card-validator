# Credit Card Validator - Luhn Algorithm

A Python implementation of the Luhn algorithm to validate credit card numbers.

## 🎓 Learning Project
This project is part of my learning journey with **FreeCodeCamp**. It demonstrates understanding of:
- Algorithm implementation
- String manipulation
- Input validation
- Code documentation

## 🔍 What is the Luhn Algorithm?
The Luhn algorithm (also known as the "modulus 10" algorithm) is a checksum formula used to validate various identification numbers, including credit card numbers.

### How it works:
1. Starting from the rightmost digit, double every second digit
2. If doubling results in a number ≥ 10, add the digits of that number
3. Sum all the digits (both doubled and non-doubled)
4. If the total sum is divisible by 10, the number is valid

## 🚀 Features
- ✅ Validates credit card numbers using the Luhn algorithm
- ✅ Handles formatted input (removes spaces and hyphens)
- ✅ Clear, commented code for educational purposes
- ✅ Test cases included for learning
- ✅ Detailed algorithm explanation

## 📋 Usage

```bash
# Run the main program
python credit_card_validator.py
```

### Example Output:
```
Credit Card Validator - Luhn Algorithm
========================================
Testing card number: 4111-1111-4555-1141
Cleaned card number: 4111111145551141
Total sum: 33
❌ INVALID! This card number fails the Luhn algorithm.

Note: This only validates the format, not whether the card actually exists.
```

## 🧪 Test Cases
The program includes test cases with known valid and invalid card numbers to demonstrate the algorithm's effectiveness.

## 📚 What I Learned
- How the Luhn algorithm works mathematically
- String slicing and manipulation in Python
- Algorithm step-by-step implementation
- Code documentation best practices
- Input sanitization techniques

## ⚠️ Disclaimer
This tool only validates the format of credit card numbers using the Luhn algorithm. It does NOT:
- Verify if the card actually exists
- Check if the card is active
- Validate expiration dates or CVV codes
- Connect to any payment systems

**Test card numbers used are publicly available test numbers and are not real credit cards.**

## 🔗 Learning Resource
This project was created as part of the FreeCodeCamp curriculum. Check out their amazing free courses at [freecodecamp.org](https://www.freecodecamp.org/)

## 🛠️ Technologies Used
- Python 3.x
- Built-in string methods and mathematical operations

---
*This is a learning project created to understand algorithm implementation and code documentation.*
