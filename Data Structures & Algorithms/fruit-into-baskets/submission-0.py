import collections
from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = collections.defaultdict(int)
        l = 0
        res = 0
        
        for r in range(len(fruits)):
            count[fruits[r]] += 1
            
            # Shrink window until we only have at most 2 distinct fruit types
            while len(count) > 2:
                f = fruits[l]
                count[f] -= 1
                if count[f] == 0:
                    del count[f]
                l += 1  # Move left pointer forward
            
            # Current valid window length is (r - l + 1)
            res = max(res, r - l + 1)
            
        return res