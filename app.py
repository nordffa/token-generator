from secrets import choice as choice_char
from string import ascii_letters, digits, punctuation
from pyperclip import copy as copy_token


def generate_token():
    caracteres = *ascii_letters, *digits, *punctuation
    token = []
    for _ in range(128):
        token.append(choice_char(caracteres))
    token_string = "".join(token)
    copy_token(token_string)
    return token_string


token = generate_token()
print(f"Token: {token}")
