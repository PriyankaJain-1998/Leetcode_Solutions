class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start_points = {}
        for i, interval in enumerate(intervals):
            start_points[interval[0]] = i
        print(start_points)
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        print(sorted_intervals)
        result = [-1] * len(intervals)
        
        # Iterate over the sorted intervals
        for i, interval in enumerate(intervals):
            # Find the index of the right interval using binary search
            index = bisect_left(sorted_intervals, [interval[1], -float('inf')])
            # If a right interval is found, update the result list with its index
            if index != len(intervals):
                result[i] = start_points[sorted_intervals[index][0]]
        
        return result
