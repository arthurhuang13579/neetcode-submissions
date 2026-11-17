class Solution:
    def isValid(self, s: str) -> bool:
        matching = []
        for i in s:
            if (i == "("):
                matching.insert(0, ")")
            elif (i == "{"):
                matching.insert(0, "}")
            elif (i == "["):
                matching.insert(0, "]")
        
            if (i == ")" or
                i == "}" or
                i == "]"):
                if (len(matching) == 0 or i != matching[0]):
                    return False
                else:
                    matching.pop(0)
        if len(matching) != 0:
            return False
        return True
        