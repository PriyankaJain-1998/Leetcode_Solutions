class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        fractions, decimals = [], []
        numerator = 1
        while numerator<n:
            denominator = 2
            while denominator<=n:
                fraction = numerator/denominator
                if fraction < 1:
                    if fraction not in decimals:
                        decimals.append(fraction)
                        fractions.append(str(numerator)+"/"+str(denominator))
                denominator+=1
            numerator+=1

        return fractions