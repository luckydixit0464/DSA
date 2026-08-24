class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        fre={}
        for i in magazine:
            if i not in fre:
                fre[i]=1
            else:
                fre[i]+=1
        for j in ransomNote:
            if j not in fre:
                return False
            fre[j]-=1
            if fre[j]==-1:
                return False
        return True

