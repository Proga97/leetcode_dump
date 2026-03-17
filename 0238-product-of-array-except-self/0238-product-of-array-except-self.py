class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        res[0] = 1
        for i in range(1,len(nums)):
            res[i] = res[i-1] * nums[i-1]
        # print(res)
        prod = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            # print(prod)
            res[i] = res[i] * prod
            prod *= nums[i]
        # for n in nums:
        #     if n != 0:
        #         suf = suf/ n
        #     else:
        #         suf = 0
        #     print("strt",n,"res",res,"pre",pre,"suf",suf)
        #     res.append(pre * suf)
        #     pre *= n
            
        #     print("end",n,"res",res,"pre",pre,"suf",suf)
        return res
        

        

        