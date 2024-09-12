class Solution(object):
    def isPalindrome(self, x):
        org = x
        rev = 0
        sign = -1 if x < 0 else 1
        len1 = len(str(x))
        for i in range(len1):
            pop = int(x%10)
            x = int(x/10)
            if rev > (2**31 - 1) // 10 or (rev == (2**31 - 1) // 10 and x > 7):
                return 0
            rev = rev*10+pop

        if rev == org:
            return 1
        else:
            return 0