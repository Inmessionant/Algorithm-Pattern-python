def getNextArray(str2):
    if len(str2) == 1:
        return [-1]

    next = [None for _ in range(len(str2))]
    next[0], next[1] = -1, 0  # 初始化
    pos, cn = 2, 0

    while pos < len(next):
        if str2[pos - 1] == str2[cn]: 
            cn += 1
            next[pos] = cn
            pos += 1
        elif cn > 0:
            cn = next[cn]
        else:
            next[pos] = 0
            pos += 1
    return next


def kmp(str1, str2):
    if str1 is None or str2 is None or len(str2) < 1 or len(str1) < len(str2):  return -1
    str1i, str2i = 0, 0
    next = getNextArray(str2)
    while str1i < len(str1) and str2i < len(str2):
        if str1[str1i] == str2[str2i]:
            str1i += 1
            str2i += 1
        elif next[str2i] == -1:
            str1i += 1
        else:
            str2i = next[str2i]
    return str1i - str2i if str2i == len(str2) else -1


str1 = "abcabcababaccc"
str2 = "ababa"
res = kmp(str1, str2)
print(res)
