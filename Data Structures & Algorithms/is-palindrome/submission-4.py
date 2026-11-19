class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = "qwertyuioplkjhgfdsazxcvbnm1234567890"
        string = s.strip().lower()
        
        front = 0
        back = len(string) - 1
        #string = "Was it a car or a cat I saw?"

        while front < back:
            while front < len(string) and string[front] not in valid:
                front += 1
                if front == len(string):
                    return True
            while back > -1 and string[back] not in valid:
                back -= 1
            if not string[front] == string[back]:
                return False
            front += 1
            back -= 1
        return True
            