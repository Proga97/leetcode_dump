from heapq import *

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            return s
        max_count, letter = 0, ""
        freq_map = defaultdict(int)
        max_possible = ceil(len(s) / k)
        for char in s:
            freq_map[char] += 1
            if max_count < freq_map[char]:
                max_count = freq_map[char]
                letter = char
            if max_count > max_possible:
                return ""
        heap = [(-count, char) for char, count in freq_map.items()]
        heapify(heap)
        res = ""
        qu = deque()
        while heap:
            count, char = heappop(heap)
            count = -count - 1
            res += char
            qu.append((count, char))
            if len(qu) == k:
                count, char = qu.popleft()
                if count > 0:
                    heappush(heap, (-count, char))

        return res if len(res) == len(s) else ""

        # while freq_map[letter] > 0:
        #     arr[index] = letter
        #     freq_map[letter] -= 1
        #     index += k
        # # print(arr)
        
        # for char, count in freq_map.items():
        #     done = False
        #     while count > 0:
        #         if index >= len(s):
        #             if not done:
        #                 index_start += 1
        #                 index = index_start
        #                 done = not done
        #             else: return ""
        #         arr[index] = char
        #         count -= 1
        #         index += k
        # return "".join(arr)
                    






# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna