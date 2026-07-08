class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Think about the length comparision here
        return len(set(nums)) != len(nums)
        
