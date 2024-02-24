import random , string

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation
password = letters + digits + symbols

game = True
while game:
    user_input = int(input("Enter the desired password length: "))
    s = ''
    for _ in range(user_input):
        s+= random.choice(password)
    
    result = ''.join(s)
    print(f"Your password is {result}")
    ask = input("Do you want to generate password again-'y'/'n'?: ")
    if ask == 'y':
        continue
    else:
        break
        game = False













   







