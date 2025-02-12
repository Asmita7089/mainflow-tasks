#1Q
# Get input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate the sum
sum_result = num1 + num2

# Print the result
print("The Sum of the numbers is:", sum_result)

#2Q
# Check if the number is odd or even
num = int(input("Enter a number: "))

print("Even" if num % 2 == 0 else "Odd")

#3Q
# Calculate the factorial
import math
num = int(input("Enter a number for factorial calculation: "))
print("Factorial:", math.factorial(num))

#4Q
# Generate the Fibonacci sequence
num = int(input("Enter the number of Fibonacci terms: "))
fibonacci_sequence = [0, 1]
for i in range(2, num):
    fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
print("Fibonacci sequence:", fibonacci_sequence[:num])

#5Q
# Reverse a string
text = input("Enter a string: ")
print("Reversed string:", text[::-1])

#6Q
# Check if the string is a palindrome
print("Is palindrome:", text == text[::-1])

#7Q
# Check if it's a leap year
year = int(input("Enter a year: "))
is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print("Is leap year:", is_leap_year)

#8Q
# Check if it's an Armstrong number
num = int(input("Enter a number: "))
num_str = str(num)
num_length = len(num_str)
is_armstrong = sum(int(digit) ** num_length for digit in num_str) == num
print("Is Armstrong number:", is_armstrong)


# Custom Encryption-Decryption System
import string
import numpy as np

# Substitution Cipher (Caesar Cipher)
def caesar_encrypt(plain_text, shift):
    result = ''
    for char in plain_text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def caesar_decrypt(cipher_text, shift):
    return caesar_encrypt(cipher_text, -shift)

# Testing the algorithms
if __name__ == "__main__":
    print("Substitution Cipher (Caesar Cipher):")
    plaintext = "Hello World!"
    shift_value = 3
    encrypted_text = caesar_encrypt(plaintext, shift_value)
    print(f"Original Text: {plaintext}")
    print(f"Encrypted Text: {encrypted_text}")
    print(f"Decrypted Text: {caesar_decrypt(encrypted_text, shift_value)}\n")
   
 # Vigenère Cipher Encryption and Decryption
def vigenere_encrypt(plain_text, key):
    result = []
    key = (key * (len(plain_text) // len(key))) + key[:len(plain_text) % len(key)]  # Repeat the key
    for pt_char, key_char in zip(plain_text, key):
        if pt_char.isalpha():
            shift = ord(key_char.lower()) - 97  # Key's letter shift (A=0, B=1, ..., Z=25)
            if pt_char.isupper():
                result.append(chr((ord(pt_char) - 65 + shift) % 26 + 65))  # Uppercase letter
            else:
                result.append(chr((ord(pt_char) - 97 + shift) % 26 + 97))  # Lowercase letter
        else:
            result.append(pt_char)  # Non-alphabetic characters remain unchanged
    return ''.join(result)

def vigenere_decrypt(cipher_text, key):
    result = []
    key = (key * (len(cipher_text) // len(key))) + key[:len(cipher_text) % len(key)]  # Repeat the key
    for ct_char, key_char in zip(cipher_text, key):
        if ct_char.isalpha():
            shift = ord(key_char.lower()) - 97  # Key's letter shift
            if ct_char.isupper():
                result.append(chr((ord(ct_char) - 65 - shift) % 26 + 65))  # Uppercase letter
            else:
                result.append(chr((ord(ct_char) - 97 - shift) % 26 + 97))  # Lowercase letter
        else:
            result.append(ct_char)  # Non-alphabetic characters remain unchanged
    return ''.join(result)

# Testing the Vigenère Cipher
if __name__ == "__main__":
    print("Vigenère Cipher:")
    plaintext = "This is a secret message!"
    key = "KEY"
    encrypted_text = vigenere_encrypt(plaintext, key)
    print(f"Original Text: {plaintext}")
    print(f"Encrypted Text: {encrypted_text}")
    print(f"Decrypted Text: {vigenere_decrypt(encrypted_text, key)}\n")
    import numpy as np

# Hill Cipher Decryption

class HillCipher:
    def __init__(self, key_matrix):
        self.key_matrix = np.array(key_matrix)
        self.modulo = 26
        self.inverse_key_matrix = self._invert_key_matrix()
    
    def _invert_key_matrix(self):
        det = int(np.round(np.linalg.det(self.key_matrix)))
        det_inv = pow(det, -1, 26)  # Modular inverse of determinant
        adjugate = np.round(det * np.linalg.inv(self.key_matrix)).astype(int) % 26
        return (det_inv * adjugate) % 26
    
    def text_to_numbers(self, text):
        return [ord(char) - ord('A') for char in text.upper() if char.isalpha()]
    
    def numbers_to_text(self, numbers):
        return ''.join(chr(num % 26 + ord('A')) for num in numbers)
    
    def encrypt(self, text):
        text = text.replace(" ", "").upper()
        n = len(self.key_matrix)
        while len(text) % n != 0:
            text += 'X'
        numbers = self.text_to_numbers(text)
        encrypted_numbers = []
        for i in range(0, len(numbers), n):
            block = np.array(numbers[i:i+n])
            encrypted_block = np.dot(self.key_matrix, block) % self.modulo
            encrypted_numbers.extend(encrypted_block)
        return self.numbers_to_text(encrypted_numbers)
    
    def decrypt(self, text):
        text = text.replace(" ", "").upper()
        numbers = self.text_to_numbers(text)
        decrypted_numbers = []
        n = len(self.inverse_key_matrix)
        for i in range(0, len(numbers), n):
            block = np.array(numbers[i:i+n])
            decrypted_block = np.dot(self.inverse_key_matrix, block) % self.modulo
            decrypted_numbers.extend(decrypted_block)
        return self.numbers_to_text(decrypted_numbers).rstrip('X')  # Remove padding

# Example Usage:
hill_cipher = HillCipher([[6, 24, 1], [13, 16, 10], [20, 17, 15]])  # 3x3 matrix

message = "HELLOEVERYONE"

# Hill Cipher
enc_hill = hill_cipher.encrypt(message)
dec_hill = hill_cipher.decrypt(enc_hill)
print(f"Hill Cipher:")
print(f"Original Text: {message}")
print(f"Encrypted Text: {enc_hill}")
print(f"Decrypted Text: {dec_hill}\n")
