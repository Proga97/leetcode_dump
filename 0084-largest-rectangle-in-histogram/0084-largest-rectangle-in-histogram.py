class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i, curr in enumerate(heights):
            if not stack or stack[-1][1] < curr:
                stack.append((i,curr))
                # print("if",curr, stack,stack[-1][1])
            else :
                # print("else",curr, stack,stack[-1][1])
                start = i
                while stack and stack[-1][1] > curr:
                    index, height = stack.pop()
                    # print(index, height)
                    # print(curr, stack, (i - index))
                    area = height * (i - index)
                    if area > max_area:
                        max_area = area
                    # max_area = max(max_area, height * (i - index))
                    start = index
                stack.append((start,curr))
        # print(stack,max_area)
        while stack:
            index, height = stack.pop()
            area = height * (len(heights) - index)
            if area > max_area:
                max_area = area
            # max_area = max(max_area, height * (len(heights) - index))
        return max_area





        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna