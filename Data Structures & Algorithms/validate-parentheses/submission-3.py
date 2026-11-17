class Solution:
    def isValid(self, s: str) -> bool:
        matching = []
        for i in s:
            if (i == "("):
                matching.append(")")
            elif (i == "{"):
                matching.append("}")
            elif (i == "["):
                matching.append("]")
        
            if (i == ")" or
                i == "}" or
                i == "]"):
                if (len(matching) == 0 or i != matching[len(matching) - 1]):
                    return False
                else:
                    matching.pop()
        if len(matching) != 0:
            return False
        return True
        