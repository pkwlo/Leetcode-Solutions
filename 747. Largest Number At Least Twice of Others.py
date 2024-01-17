def dominantIndex(nums) -> int:
    nums_new = sorted(nums)
    for index in range(len(nums_new) - 1):
        if nums_new[-1] < nums_new[index] * 2:
            return -1
    for index in range(len(nums)):
        if nums_new[-1] == nums[index]:
            return index


def main():
    nums = [0, 0, 0, 1]
    print(dominantIndex(nums))


if __name__ == "__main__":
    main()
