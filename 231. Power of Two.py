"""
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1

Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16

Example 3:

Input: n = 3
Output: false

"""


def isPowerOfTwo(number):
    if number == 0:
        return False
    elif number == 1:
        return True
    else:
        return number % 2 == 0 and isPowerOfTwo(number // 2)


def main():
    number = 32
    print(isPowerOfTwo(number))


if __name__ == "__main__":
    main()
