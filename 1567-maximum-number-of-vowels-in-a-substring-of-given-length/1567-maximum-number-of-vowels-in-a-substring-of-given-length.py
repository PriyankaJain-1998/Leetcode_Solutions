class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        max_vowels = vowels_temp = sum(s[i] in vowels for i in range(k)) #len(re.findall(vowels, s[:k]))
        # max_vowels = 0

        for i in range(k,len(s)):
            vowels_temp += (s[i] in vowels)-(s[i-k] in vowels)
            max_vowels = max(max_vowels, vowels_temp)
        return max_vowels

        # for i in range(0,len(s)):
        #     num_vowels = sum(s[i:i+k].count(vowel) for vowel in vowels)
        #     if max_vowels < num_vowels:
        #         max_vowels = num_vowels
        # return max_vowels
        
        