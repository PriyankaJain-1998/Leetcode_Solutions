class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        ## not all test cases passed
        # left, right = sorted(changed[:len(changed)//2]), sorted(changed[len(changed)//2:])
        # print(left, right)

        # if list(map(lambda x: x * 2, left)) == right: return left
        # elif list(map(lambda x: x * 2, right)) == left: return right
        # else: return []

        if len(changed)%2 !=0: return []

        changed = sorted(changed)
        c = Counter(changed)
        output = []
        for num in changed:
            if num in c and c[num]>=1:
                c[num]-=1
                if (num*2) in c and c[(num*2)]>=1:
                    output.append(num)
                    c[num*2]-=1
            if len(output)==len(changed)//2: return output 
        return []