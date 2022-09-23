class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        z=len(set(nums))
        if len(nums)==z:
            return False
        else: 
            return True
        