class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}
        for ch in tasks:
            counts[ch] = counts.get(ch,0) + 1
        
        h = [-val for key,val in counts.items()]
        heapq.heapify(h)
        res = 0
        while h:
            cycles = 0
            processed = []
            for i in range(n+1):
                if not h:
                    break
                popped = -heapq.heappop(h)-1
                cycles += 1
                processed.append(popped)
            for val in processed:
                if val > 0:
                    heapq.heappush(h, -val)
            if h:
                # Still have tasks → add full cycle (n+1) including idle time
                res += n + 1
            else:
                # No more tasks → only add the tasks we actually processed
                res += cycles
        return res