class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        # if target>=letters[-1] or target<letters[0]: return letters[0]
        # low, high = 0, len(letters)-1
        # while low<=high:
        #     mid=(low+high)//2
        #     if target>=letters[mid]: low =mid+1
        #     if target < letters[mid]: right = mid

        # return letters[low]

        t_ord = ord(target)-ord('a')
        for i in letters:
            l_ord = ord(i)-ord('a')
            if l_ord > t_ord: return i
        return letters[0]