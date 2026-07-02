import string 
import random 
def generate_password(min_length, require_digits=True, require_symbols=True): 
    alpha_charset = string.ascii_letters 
    digit_charset = string.digits 
    symbol_charset = string.punctuation 
    charset = alpha_charset 
    if require_digits: 
        charset += digit_charset 
    if require_symbols: 
        charset += symbol_charset 
    generated_password = "" 
    criteria_satisfied = False 
    digit_flag = False 
    symbol_flag = False 
    while not criteria_satisfied or len(generated_password) < min_length: 
        candidate_char = random.choice(charset) 
        generated_password += candidate_char 
        if candidate_char in digit_charset: 
            digit_flag = True 
        elif candidate_char in symbol_charset: 
            symbol_flag = True 
        criteria_satisfied = True 
        if require_digits: 
            criteria_satisfied = digit_flag 
        if require_symbols: 
            criteria_satisfied = criteria_satisfied and symbol_flag 
    return generated_password 
min_length =int(input("Enter the minimum lenght : ")) 
digit_flag = input("Do you want to have numbers(y/n)").lower() =="y" 
symbol_flag = input("Do you want to have special characters (y/n)?").lower() == "y" 
generated_password = generate_password(min_length) 
print(generated_password) 