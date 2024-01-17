def toLowerCase(s: str) -> str:
    new_string = ""
    for character in s:
        if character.islower():
            new_string += character
        else:
            new_string += character.lower()
    return new_string


def main():
    s = "Hello"
    print(toLowerCase(s))


if __name__ == "__main__":
    main()
