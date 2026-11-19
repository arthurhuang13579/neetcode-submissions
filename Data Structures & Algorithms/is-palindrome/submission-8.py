class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = "qwertyuioplkjhgfdsazxcvbnm1234567890"
        #string = s.strip().lower()
        
        front = 0
        back = len(s) - 1
        #string = "Was it a car or a cat I saw?"

        while front < back:
            while front < back and not s[front].isalnum():
                front += 1
            while front < back and not s[back].isalnum():
                back -= 1
            if s[front].lower() != s[back].lower():
                return False
            front += 1
            back -= 1
        return True
            