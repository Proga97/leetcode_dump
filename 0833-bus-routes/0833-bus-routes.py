class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        stops_map = defaultdict(list)
        for bus in range(len(routes)):
            for stop in routes[bus]:
                stops_map[stop].append(bus)
        if source not in stops_map or target not in stops_map:
            return -1
        # print(stops_map)
        seen = set()
        stopsVisited = set()
        queue = deque()
        queue.append(stops_map[source])
        for bus in stops_map[source]:
            seen.add(bus)
        bus_count = 1
        while queue:
            curr_buses = queue.popleft()
            next_buses = []
            for bus in curr_buses:
                for stop in routes[bus]:
                    if stop not in stopsVisited:
                        stopsVisited.add(stop)
                        # print("stop",stop)
                        if stop == target:
                            return bus_count
                        for next_bus in stops_map[stop]:
                            if next_bus not in seen:
                                next_buses.append(next_bus)    
                                seen.add(next_bus)
            if next_buses:
                queue.append(next_buses)
            bus_count += 1
        return -1




                        

                    



        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna