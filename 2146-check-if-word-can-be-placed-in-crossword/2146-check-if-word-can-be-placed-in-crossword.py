class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        n, words = len(word), [word,word[::-1]]
        print(n, word)
        for brd  in (board, zip(*board)):
            brd = chain(*[''.join(row).split('#') for row in brd])
            
            for s, w in product(brd,words):
                if len(s) == n and all(s[i] in [' ', w[i]] for i in range(n)):
                    return True
            
        return  False