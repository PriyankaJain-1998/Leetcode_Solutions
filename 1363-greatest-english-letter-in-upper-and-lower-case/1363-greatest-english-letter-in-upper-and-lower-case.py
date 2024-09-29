class Solution:
    def greatestLetter(self, s: str) -> str:
        uppercase_set = set(s) & set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        lowercase_set = set(s) & set('abcdefghijklmnopqrstuvwxyz')
        print(uppercase_set, lowercase_set)
        result = sorted({char for char in uppercase_set if char.lower() in lowercase_set}, reverse=True)
        print(result)
        if len(result)==0: return "" 
        return result[0]

