class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for i in range(len(intervals)):
            # Case 1: newInterval comes strictly BEFORE the current interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            
            # Case 2: newInterval comes strictly AFTER the current interval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            # Case 3: Overlap occurs -> merge into newInterval
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]
                
        # Append newInterval if it was not added inside the loop
        res.append(newInterval)
        return res