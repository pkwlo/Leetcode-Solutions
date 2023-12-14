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


def isPowerOfFour(number):
    if number == 0:
        return False
    elif number == 1:
        return True
    else:
        return number % 4 == 0 and isPowerOfFour(number // 4)


def main():
    number = 64
    print(isPowerOfFour(number))


if __name__ == "__main__":
    main()
