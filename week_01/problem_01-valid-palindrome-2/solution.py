class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalin(left, right):
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True

        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                """ check if bad char is at left or right index
                    by testing palindrome existence (1) need to skip left index,
                    compare indices s[l+1:r] (2) or need to skip right index, 
                    compare indices s[l:r-1]
                """
                return isPalin(l+1, r) or isPalin(l, r-1)
        return True
