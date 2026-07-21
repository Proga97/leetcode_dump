from heapq import *

class FreqStack:

    def __init__(self):
        self.group = defaultdict(list)
        self.max_freq = 0
        self.freq_map = defaultdict(int)

    def push(self, val: int) -> None:
        self.freq_map[val] += 1
        if self.freq_map[val] > self.max_freq:
            self.max_freq = self.freq_map[val]
        self.group[self.freq_map[val]].append(val)

    def pop(self) -> int:
        x = self.group[self.max_freq].pop()
        self.freq_map[x] -= 1
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return x
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna