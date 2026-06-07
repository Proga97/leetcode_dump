class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        seen = set()
        route_map = defaultdict(list)
        for i in edges:
            route_map[i[0]].append(i[1])
            route_map[i[1]].append(i[0])
        # print(route_map)
        stack = [source]
        seen.add(source)

        while stack:
            curr = stack.pop()
            
            # if curr not in seen:
            for i in route_map[curr]:
                if i == destination:
                    return True
                if i not in seen:
                    seen.add(i)
                    stack.append(i)

        return destination in seen


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna