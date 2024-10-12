class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)/2
        arr = sorted(arr)
        
        # ------ tle
        # ans = {}
        # for i in range(len(arr)):
        #     for j in range(i+1, len(arr)):
        #         diff = arr[j]-arr[i]
        #         if diff not in ans: ans[diff] = [[arr[i],arr[j]]]
        #         else: ans[diff].append([arr[i],arr[j]])

        # print(ans, ans[min(ans.keys())])
        # return ans[min(ans.keys())]
        minDiff = math.inf
        dic = collections.defaultdict(list)
        arr.sort()                                         #O(n log n) time
        
        for i in range(len(arr)-1):                        #O(n) time
            diff = arr[i+1] - arr[i]
            dic[diff].append([arr[i], arr[i+1]])           #O(n) space if all the pairs have the same minimum difference
            minDiff = min(minDiff, diff)
        return dic[minDiff]