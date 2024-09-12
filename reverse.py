class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Initialize the reversed number to 0
        rev = 0
        # Determine the sign of x
        sign = -1 if x < 0 else 1
        # Work with the absolute value of x
        x = abs(x)
        
        while x != 0:
            # Get the last digit
            pop = x % 10
            x //= 10
            # Check for overflow
            if rev > (2**31 - 1) // 10 or (rev == (2**31 - 1) // 10 and pop > 7):
                return 0
            rev = rev * 10 + pop
        
        return sign * rev
