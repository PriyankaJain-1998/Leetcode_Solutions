class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        return [index for index in range(1, len(height)) if height[index-1]>threshold]
        