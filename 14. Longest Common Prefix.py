def longestCommonPrefix(strs) -> str:
    common_prefix = strs[0]
    if "" in strs:
        return ""
    for word in strs:
        if len(common_prefix) < len(word):
            for index in range(len(common_prefix)):
                if word[index] != common_prefix[index]:
                    common_prefix = common_prefix[0: index]
                    break
        else:
            for index in range(len(word)):
                if word[index] != common_prefix[index]:
                    common_prefix = common_prefix[0: index]
                    break
                else:
                    if len(word) == index+1:
                        common_prefix = common_prefix[0: index+1]
    return common_prefix


if __name__ == "__main__":
    strs = ["aa", "aaa", "aa"]
    print(longestCommonPrefix(strs))
