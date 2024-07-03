def lengthOfLongestSubstring(s):
    n = len(s)
    max_lentgh = 0
    left = 0
    seen_chars = set()

    for right in range(n):
        while s[right] in seen_chars:
            seen_chars.remove(s[left])
            left += 1
        seen_chars.add(s[right])
        max_lentgh = max(max_lentgh, right-left+1)
    return max_lentgh        
        


s = 'abdaaabdsaaae'
print(lengthOfLongestSubstring(s))