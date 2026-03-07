class Solution: 
    def valid_anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_hashmap={}
        t_hashmap={}
        for i in s:
            if i in s_hashmap:
                s_hashmap[i] += 1
            else: 
                s_hashmap[i] = 1
        for i in t:
            if i in t_hashmap:
                t_hashmap[i] += 1
            else: 
                t_hashmap[i] = 1
        for i in t_hashmap:
            if i not in s_hashmap:
                return False
            if t_hashmap[i] != s_hashmap[i]:
                return False
        return True

instance = Solution()
print(instance.valid_anagram("xob","boxc"))

# {
#     a:3,
#     g:1,
#     m:1,
#     n:1,
#     r:1
# }

# {
#     a:3,
#     g:1,
#     m:1,
#     n:1,
#     r:1
# }