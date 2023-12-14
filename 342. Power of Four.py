"""
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.



Example 1:

Input: n = 16
Output: true

Example 2:

Input: n = 5
Output: false

Example 3:

Input: n = 1
Output: true

"""


def isPowerOfFour(number, exponent):
    if number == 0:
        return False
    elif number == 1:
        return True
    elif number == 4 * exponent:
        return True
    elif number >= 4 * exponent * 4:
        return isPowerOfFour(number, exponent * 4)
    else:
        return False


def main():
    number = 16
    exponent = 1
    print(isPowerOfFour(number, exponent))


if __name__ == "__main__":
    main()
