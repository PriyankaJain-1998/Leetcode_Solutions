class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]  # slice after expansion breaks

        longest = ""
        for i in range(len(s)):
            # Odd length palindrome
            longest = max(longest, expand(i, i), key=len)
            # Even length palindrome
            longest = max(longest, expand(i, i+1), key=len)

        return longest