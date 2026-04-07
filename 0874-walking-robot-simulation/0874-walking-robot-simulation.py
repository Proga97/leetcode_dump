class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs = set()
        for (x,y) in obstacles:
            obs.add((x,y))
        # print (obs)

        d = "n"
        x, y = 0, 0
        max_d = 0
        for c in commands:
            if c == -2:
                if d == "n": d = "w"
                elif d == "w": d = "s"
                elif d == "s": d = "e"
                else: d = "n"
            elif c == -1:
                if d == "n": d = "e"
                elif d == "e": d = "s"
                elif d == "s": d = "w"
                else: d = "n"
            else:
                if d == "n":
                    for _ in range(c):
                        if (x, y + 1) in obs:
                            break
                        y += 1
                        max_d = max(max_d, x**2 + y**2)
                elif d == "s":
                    for _ in range(c):
                        if (x, y - 1) in obs:
                            break
                        y -= 1
                        max_d = max(max_d, x**2 + y**2)

                elif d == "w":
                    for _ in range(c):
                        if (x - 1, y) in obs:
                            break
                        x -= 1
                        max_d = max(max_d, x**2 + y**2)

                else:
                    for _ in range(c):
                        if (x + 1, y) in obs:
                            break
                        x += 1
                        max_d = max(max_d, x**2 + y**2)

        # print(x,y, (x**2 + y**2))        
        return max_d






        