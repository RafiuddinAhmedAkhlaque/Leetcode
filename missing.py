class Solution: 
    def missing_number(self, nums: list[int]) -> int: 
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)+1):
            if i not in hashmap:
                return i

instance = Solution()
print(instance.missing_number([1,3,2,0,5]))