class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1: 
            ##heaviest stone
            heaviest = -(heapq.heappop(stones))
            secHeaviest = -(heapq.heappop(stones))

            if heaviest == secHeaviest:
                continue
            else:
                stones.append(-(heaviest-secHeaviest))
                heapq.heapify(stones)
        if not stones:
            return 0
        return -stones[0]
