class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        stops_map = defaultdict(list)
        for bus,stops in enumerate(routes):
            for stop in stops:
                if stop in stops_map:
                    stops_map[stop].append(bus)
                else: stops_map[stop] = [bus]
        # print(stops_map)
        buses = 1
        queue = collections.deque()
        seen = set()
        queue.append(stops_map[source])
        # print(queue)
        while queue:
            current_buses = queue.popleft()
            new_buses = []
            for bus in current_buses:
                if bus not in seen:
                    seen.add(bus)
                    for stop in routes[bus]:
                        if stop == target:
                            return buses
                        for next_bus in stops_map[stop]:
                            # print("next bus",next_bus)
                            if next_bus not in seen:
                                new_buses.append(next_bus)
            if new_buses:
                queue.append(new_buses)
            buses += 1

        return -1   

                        

                    



        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna