class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit= int(''.join(map(str, digits)))
        digit+=1
        l1=[int(x) for x in str(digit)]
        return l1