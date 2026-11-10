class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h={}
        ans=[]
        for i in nums:
            if i in h.keys():
                h[i]=h[i]+1
            else:
                h[i]=1
        items = sorted(h.items(), key=lambda x: x[1], reverse=True)
        ans = [item[0] for item in items[:k]]

        return ans