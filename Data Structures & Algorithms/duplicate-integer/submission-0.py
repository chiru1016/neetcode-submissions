class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       pre = []
       for i in nums:
        if i not in pre:
            pre.append(i)
        else:
            return True
       return False

        
