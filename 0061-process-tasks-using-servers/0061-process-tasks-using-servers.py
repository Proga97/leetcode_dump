class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        t = 0
        res = []
        busy = []
        idle = [(w,i) for i, w in enumerate(servers)]
        heapify(idle)

        def release():
            while busy and busy[0][0] <= t:
                td, idx = heappop(busy)
                heappush(idle, (servers[idx], idx))
        
        for i, task in enumerate(tasks):
            t = max(t, i)
            release()

            if not idle:
                t = busy[0][0]
                release()
            
            w, idx = heappop(idle)
            res.append(idx)
            heappush(busy, (t+task, idx))
        
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna