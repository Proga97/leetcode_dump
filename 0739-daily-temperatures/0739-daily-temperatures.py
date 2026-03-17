class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # l = 0 
        # r = 1
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
                while stack and temperatures[stack[-1]] < temperatures[i]:
                    x = stack.pop()
                    print(x,i)
                    res[x] = i - x
                stack.append(i)

            

        # while r < len(temperatures):
        #     if temperatures[l] < temperatures[r]:
        #         res.append(r-l)
        #         l += 1
        #         r = l + 1
        #     else:
        #         r+=1
        # # print(res)
        # while l < len(temperatures):
        #     res.append(0)
        #     l+=1
        print(res)
        return res

