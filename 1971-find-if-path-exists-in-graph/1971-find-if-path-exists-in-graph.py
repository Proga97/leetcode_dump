class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        seen = set()
        route_map = defaultdict(list)
        for i in edges:
            route_map[i[0]].append(i[1])
            route_map[i[1]].append(i[0])
        # print(route_map)
        stack = [source]

        while stack:
            curr = stack.pop()
            if curr == destination:
                return True
            if curr not in seen:
                seen.add(curr)
                for i in route_map[curr]:
                    if i not in seen:
                        stack.append(i)

        return False


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna