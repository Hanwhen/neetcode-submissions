class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        arr = [0]*k
        for n in nums:
            if n in m:
                m[n]+=1 # val:freq
            else:
                m[n]=1
        for i in range(0,k):
            max_freq = max(m.values()) 
            max_key = max(m,key=m.get)
            arr[i] = max_key
            del m[max_key]
        return arr
