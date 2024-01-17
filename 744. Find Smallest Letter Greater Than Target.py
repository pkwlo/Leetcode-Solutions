def nextGreatestLetter(letters, target: str) -> str:
    letters.append(target)
    letters_new = sorted(letters)
    print(letters_new)
    counter = 0
    for number in range(len(letters_new) - 1):
        if letters_new[number] == target:
            counter += 1
            if counter >= 1 and letters_new[number + 1] > letters_new[number]:
                return letters_new[number + 1]
            else:
                continue
    return letters_new[0]


def main():
    letters = ["c", "f", "j"]
    target = "a"
    print(nextGreatestLetter(letters, target))


if __name__ == "__main__":
    main()
