class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height:
            return 0
        
        volume = 0
        
        # set the initial value
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        
        # loop for checking all and will be stopped if it's checked all
        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            
            # check min of max side toward max of max side
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        
        return volume