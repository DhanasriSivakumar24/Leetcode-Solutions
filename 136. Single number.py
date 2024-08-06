class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique = [i for i in nums if nums.count(i)== 1]
        return unique[0]