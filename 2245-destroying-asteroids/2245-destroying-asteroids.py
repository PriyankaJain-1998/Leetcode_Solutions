class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        sorted_asteroids = sorted(asteroids)
        #  if sum(sorted_asteroids[:-1]) < max(asteroids): return False
        for a in sorted_asteroids:
            if mass<a:
                return False
            mass+=a
        return True
