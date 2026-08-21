"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = []
        res = []
        for emp in schedule:
            intervals.extend(emp)
        intervals.sort(key = lambda x: x.start)
    
        prev = intervals[0]
        for i in range(1, len(intervals)):
            if prev.end < intervals[i].start:
                res.append(Interval(prev.end , intervals[i].start))
                prev = intervals[i]
            else:
                prev.end = max(prev.end, intervals[i].end)

        return res
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna