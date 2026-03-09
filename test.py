#All optimal solutions
class Solution: 
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        hashmap={}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [hashmap[complement],i]
            else: 
                hashmap[nums[i]] = i
            
instance = Solution()
print(instance.two_sum([2,3,4,6,7],11))

class Solution2: 
    def duplicate_number(self, nums: list[int]) -> bool: 
        hashmap={}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                return True
            else: 
                hashmap[nums[i]]=i
        return False

instance2 = Solution2()
print(instance2.duplicate_number([2,3,4,5,6]))

class Solution3: 
    def missing_number(self, nums: list[int]) -> int: 
        hashmap={}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)+1):
            if i not in hashmap: 
                return i

instance3 = Solution3()
print(instance3.missing_number([0,1,3,4]))