class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        z=[]
        for i in s:
            if i in 'abcdefghijklmnopqrstuvwxyz0123456789':
                z.append(i)
            else:
                continue
        return z[::-1]==z
            
        