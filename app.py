from secrets import choice as choice_char
from string import ascii_letters, digits, punctuation
from pyperclip import copy as copy_token


def generate_token() -> str:
    characters = *ascii_letters, *digits, *punctuation
    token: list[str] = []

    for _ in range(128):
        token.append(choice_char(characters))

    token_string: str = "".join(token)
    copy_token(token_string)
    return token_string


if __name__ == '__main__':
    token = generate_token()
