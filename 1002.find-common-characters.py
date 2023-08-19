#
# @lc app=leetcode id=1002 lang=python
#
# [1002] Find Common Characters
#

# @lc code=start
class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        i=0
        count = {}
        sum = 0
        output = []
        for letter in words[0]:
            # print(letter)
            for j in range(1, len(words)):
                print(letter," ",j)
                # print(letter," ",words[j])
                if letter in words[j]:
                    if letter in count.keys():
                        # print(letter)
                        count[letter] += 1
                        continue
                    else:
                        count[letter] = 1
                # if count == len(words):
                #     output.append(letter)   

        print(count)
        return output

        
# @lc code=end

