import random
import string

def base64_encode(input_string):
    binary_string = ''
    
    for char in input_string:
        binary_string += f'{ord(char):08b}'
        
    print(binary_string)
    for i in range(6 - (len(binary_string) % 6)):
        binary_string += '0'
        
    result = ''
    base64_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    for i in range(0, len(binary_string), 6):
        integer = int(binary_string[i:i+6], 2)
        result += base64_characters[integer]
    
    padding = 4 - (len(result) % 4)
    if 4 > padding > 0:
        result += ('=' * padding)
    
    return result

def generate_strong_password():
    passwordLength = 8
    remaining_length = passwordLength - 4
    
    lowercase_letter = random.choice(string.ascii_lowercase)
    uppercase_letter = random.choice(string.ascii_uppercase)
    number = random.choice(string.digits)
    special_character = random.choice(string.punctuation)

    all_characters_without_selected = (string.ascii_letters + string.digits + string.punctuation
    ).replace(lowercase_letter, '').replace(uppercase_letter, '').replace(number, '').replace(special_character, '')
    
    remaining_letters = []
    for i in range(remaining_length):
        remaining_letters.append(random.choice(all_characters_without_selected))

    password = (lowercase_letter +
        uppercase_letter +
        number +
        special_character +
        ''.join(remaining_letters))

    password_list = list(password)
    random.shuffle(password_list)
    return ''.join(password_list)
    

if __name__ == '__main__':
    base64_encoded_string = base64_encode('Hello world!')
    print(base64_encoded_string)
    
    strong_password = generate_strong_password()
    print(strong_password)
