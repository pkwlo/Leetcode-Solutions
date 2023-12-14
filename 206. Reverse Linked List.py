"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]

Input: head = []
Output: []
"""


# def reverseList(head):
#     return head[::-1]


# using looping
# def reverseList(head):
#     result = []
#     while len(head) > 0:
#         result.append(head[-1])
#         head.pop(-1)
#     return result


# using list comprehension
# def reverseList(head):
#     return [head[i] for i in range(len(head) - 1, -1, -1)]


# using recursion
def reverseList(head):
    if not head:
        return []
    else:
        return [head[-1]] + reverseList(head[:-1])


def main():
    head = [1, 2, 3, 4, 5]
    print(reverseList(head))


if __name__ == "__main__":
    main()
