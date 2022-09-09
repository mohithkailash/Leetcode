class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        myset = set()
        for i in nums:
            if i != 0 and i not in myset:
                myset.add(i)
        return len(myset)