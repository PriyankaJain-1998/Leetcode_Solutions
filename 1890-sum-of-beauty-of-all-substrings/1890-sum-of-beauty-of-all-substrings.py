class Solution:
    def beautySum(self, s: str) -> int:
        n, ans = len(s), 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                sub_str = s[i:j]
                char_count = Counter(sub_str)
                most_common = max(char_count, key=char_count.get)
                least_common = min(char_count, key=char_count.get)
                beauty_number = char_count[most_common]-char_count[least_common]
                if beauty_number != 0: ans+=beauty_number
                
        return ans