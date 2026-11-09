class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        count = [0] * k
        idle_servers = list(range(k))
        busy = []

        for i in range(len(arrival)):
            arr = arrival[i]
            l = load[i]

            while busy and busy[0][0] <= arr:
                end, server = heappop(busy)
                heappush(idle_servers, i + (server - i) % k)
            
            if idle_servers:
                server = heappop(idle_servers) % k
                heappush(busy, (arr + l, server))
                count[server] += 1
        
        busy_load = max(count)
        res = []
        for k, v in enumerate(count):
            if v == busy_load:
                res.append(k)
        return res
            

            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna