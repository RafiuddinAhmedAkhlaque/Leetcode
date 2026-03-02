#Brute force method
class Solution: 
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

instance = Solution()
print(instance.two_sum([2,4,6,7], 11))

#Optimized hashmap method
class Solution2: 
    def two_sum(self, nums: list[int], target: int) -> list[int]: 
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap: 
                return [hashmap[complement], i]
            else: 
                hashmap[nums[i]] = i


instance2 = Solution2()
print(instance2.two_sum([1,3,5,7], 10))