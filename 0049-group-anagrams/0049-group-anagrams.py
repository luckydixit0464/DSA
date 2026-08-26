class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp={}
        for i in range(len(strs)):
          j="".join(sorted(strs[i]))
          if j not in grp:
            grp[j]=[]
          grp[j].append(strs[i])
        return list(grp.values())