class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        output = [0,gain[0]]
        for i in range(1, len(gain)): 
            output.append(output[-1] + gain[i])

        return max(output)

        