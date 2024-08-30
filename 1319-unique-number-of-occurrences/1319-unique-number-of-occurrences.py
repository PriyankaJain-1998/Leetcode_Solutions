class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr_set = set(arr)
        count = []
        for i in arr_set:
            # print(arr.count(i), i)
            if arr.count(i) in count:
                return False
            else: count.append(arr.count(i))
        
        return True
        