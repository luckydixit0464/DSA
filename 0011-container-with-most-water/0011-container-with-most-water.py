class Solution:
    def maxArea(self, height: list[int]) -> int:
        # brute force
        # maxa=0
        # for i in range(len(height)):
        #     for j in range(i+1,len(height)):
        #         ht=min(height[i],height[j])
        #         wid=j-i
        #         area=wid*ht
        #     maxa=max(maxa,area)
        # return maxa
        l=0
        r=len(height)-1
        maxa=0
        while(l<r):
            ht=min(height[l],height[r])
            wid=r-l
            area=ht*wid
            maxa=max(area,maxa)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maxa
         