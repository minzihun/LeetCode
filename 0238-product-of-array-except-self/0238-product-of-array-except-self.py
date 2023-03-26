class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # assign result array's element with 1
        res = [1] * (len(nums))
        
        # compute prefix job
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        # compute postfix job
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res