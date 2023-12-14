"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]

Input: head = []
Output: []
"""


def reverseList(head):
    return head[::-1]


def main():
    head = []
    print(reverseList(head))


if __name__ == "__main__":
    main()
