class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = {}
        n2 = {}
        ans = []
        for i in nums1:
            if i not in n1:
                n1[i] = 1
            else:
                n1[i] += 1
        for i in nums2:
            if i not in n2:
                n2[i] = 1
            else:
                n2[i] += 1
        for element in n1:
            if element in n2:
                times = min(n1[element],n2[element])
                while times:
                    ans.append(element)
                    times -= 1
        return ans