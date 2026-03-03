#Optimal solution
class Solution: 
    def contains_duplicate(self, nums: list[int]) -> bool:
        hashmap={}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                return True
            else: 
                hashmap[nums[i]] = i
        return False

instance = Solution()
print(instance.contains_duplicate([2,3,4,5,6]))

#Brute force solution
class Solution2: 
    def contains_duplicate2(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

instance2 = Solution2()
print(instance2.contains_duplicate2([3,3,4,5,6]))

            
