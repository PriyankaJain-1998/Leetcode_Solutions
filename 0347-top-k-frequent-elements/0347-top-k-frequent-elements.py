class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = Counter(nums)
        print(nums)
        sorted_num = dict(sorted(nums.items(), key=lambda item: item[1], reverse=True))
        print(sorted_num.keys())
        return list(sorted_num.keys())[:k]