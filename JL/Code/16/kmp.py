class Solution:
    def kmp(str1, str2):
        def getNextArray(str2):
            if len(str2) == 1:  return [-1]

            next = [None for _ in range(len(str2))]
            next[0], next[1] = -1, 0
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
