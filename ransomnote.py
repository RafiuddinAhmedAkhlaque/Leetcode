class Solution: 
    def ransomNote(self, ransomNote: str, magazine: str) -> bool: 
        ransom={}
        mag={}
        for i in ransomNote:
            if i in ransom:
                ransom[i] += 1
            else:
                ransom[i]=1
        for i in magazine:
            if i in mag:
                mag[i] += 1
            else:
                mag[i]=1
        if len(magazine) < len(ransomNote):
            return False
        for i in ransom:
            if i not in mag:
                return False
            if ransom[i] > mag[i]:
                return False
        return True

