def isValid(s: str) -> bool:
    if s[0] == ")" or s[0] == "}" or s[0] == "]":
        return False
    parentheses_list = []
    for c in s:
        if c == "(" or c == "{" or c == "[":
            parentheses_list += c
        elif c == ")":
            if len(parentheses_list) == 0 or parentheses_list[-1] != "(":
                return False
            else:
                parentheses_list.pop(-1)
        elif c == "}":
            if len(parentheses_list) == 0 or parentheses_list[-1] != "{":
                return False
            else:
                parentheses_list.pop(-1)
        else:
            if len(parentheses_list) == 0 or parentheses_list[-1] != "[":
                return False
            else:
                parentheses_list.pop(-1)
    if len(parentheses_list) == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    print(isValid("(){}]"))
