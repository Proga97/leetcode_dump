class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        stops_map = defaultdict(list)
        for bus,stops in enumerate(routes):
            for stop in stops:
                stops_map[stop].append(bus)
        # print(stops_map)
        que = deque()
        seen = set()
        que.append(stops_map[source])
        for buses in stops_map[source]:
            seen.add(buses)
        buses_count = 1
        while que:
            curr_buses = que.popleft()
            next_buses = []
            for curr_bus in curr_buses:
                for stop in routes[curr_bus]:
                    # print(que,seen,curr_bus,stop)
                    if stop == target:
                        return buses_count
                    for next_bus in stops_map[stop]:
                        if next_bus not in seen:
                            # print("next_bus",next_bus,que,seen,curr_bus,stop)
                            next_buses.append(next_bus)
                            seen.add(next_bus)
            if next_buses:
                que.append(next_buses)  
                buses_count += 1             

        return -1   

                        

                    



        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna