class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)):
            for y in range(x+1,len(nums)):
                if(nums[y]==target-nums[x]):
                    return [x,y]