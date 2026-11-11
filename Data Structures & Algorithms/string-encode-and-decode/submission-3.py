class Solution:

    def encode(self, strs: List[str]) -> str:
        final = ""
        for s in strs:
            final += str(len(s)) + "#" + s
        return final

    def decode(self, s: str) -> List[str]:
        final = []
        start_num = 0
        c = 0
        while c < len(s):
            if s[c] == "#":
                #print("Start Num: " + str(start_num))
                #print("Index: " + str(c))
                num = int(s[start_num: c])
                #print("Num: " + str(num))
                final.append(s[c+1: c+1+num])
                start_num = c+1+num
                c = c+1+num
                #print()
            else:
                c += 1
        return final
            
