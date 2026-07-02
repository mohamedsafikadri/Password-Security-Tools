import string
import getpass
def check_pwd():
    pwd= getpass.getpass("Enter your Password :")
    strength = 0
    notes = ''
    lower_count=upper_count=num_count=space_count=symbols_count =0   
    for char in list(pwd):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char == ' ' :
            space_count += 1
        else:
            symbols_count += 1
    if lower_count >= 1 :
        strength += 1      
    if upper_count >= 1:
        strength += 1
    if num_count >= 1 :
        strength +=1
    if space_count >= 1 :
        strength += 1
    if symbols_count >= 1:
        strength += 1
    if strength ==1 :
        notes= "Easily guessed or cracked."
    elif strength == 2:
        notes = "contains limited character variety or insufficient length"
    elif strength == 3:
        notes="Meets minimum security requirements but could be stronger"
    elif strength == 4 :
        notes="Good combination of length and character diversity"
    elif strength == 5 :
        notes="Highly resistant to guessing and brute-force attacks "
    print("*******Password analysis and results********")
    print(f"{lower_count} lowercase characters")
    print(f"{upper_count} uppercase characters")
    print(f"{num_count} numeric characters")
    print(f"{space_count} whitespace characters")
    print(f"{symbols_count} special characters")
    print(f"Password compexity :{strength}")
    print(f"Hint : {notes}")
def ask_pwd(another_pwd=False):
    valid = False
    if another_pwd:
        choice=input("do you want to enter another pwd (y/n):")
    else:
        choice=input("do you want to change pwd (y/n)")
    while not valid:
        if choice.lower() == "y":
            return True
        elif choice.lower() == "n":
            return False
        else:
            print("Try again")
if __name__ == '__main__':
    print("******welcome to password cheker******")
    test_pwd=ask_pwd()
    while check_pwd:
        check_pwd()
        test_pwd= ask_pwd(True)