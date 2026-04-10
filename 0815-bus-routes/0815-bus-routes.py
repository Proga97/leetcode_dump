class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        bus_stops = defaultdict(list)
        for i, bus in enumerate(routes):
            for stop in bus:
                bus_stops[stop].append(i)
        # print(bus_stops)

        queue = collections.deque()
        # print(bus_stops[source])
        queue.append(bus_stops[source])
        # print(queue)
        buses_count = 1
        visited = set()
        while queue:
            buses = queue.popleft()
            # print(buses)
            new_buses = []
            for bus in buses:
                # print(bus,"bus")
                
                if bus not in visited:
                    visited.add(bus)
                    # print(bus)
                    for stop in routes[bus]:
                        # print("stop",stop)
                        if stop == target:
                            return buses_count
                        for bus in bus_stops[stop]:
                            # print("next bus",bus)
                            if bus not in visited:
                                new_buses.append(bus)
                                
            if new_buses:
                queue.append(new_buses)
            buses_count += 1    



        return -1