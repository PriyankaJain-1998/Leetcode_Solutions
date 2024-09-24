class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        onecnt, onecntlst =0,{}
        for i in mat:
            onecntlst[onecnt] = sum(i)
            onecnt +=1
        onecntlst = sorted(onecntlst.items(), key=lambda x:x[1])
        onecntlst = dict(onecntlst)
        return list(onecntlst.keys())[0:k]

        
        