class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        results = []
        nums.sort()
        
        for i in range(len(nums) - 2):
            
            # skip the duplicated value
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # calculate sum value using 2 points
            left, right = i+1, len(nums)-1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                
                if sum < 0:
                    left += 1
                
                elif sum > 0:
                    right -= 1
                
                # sum = 0
                else:
                    results.append([nums[i], nums[left], nums[right]])
                    
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left > right and nums[right] == nums[right-1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                    
        return results
                    