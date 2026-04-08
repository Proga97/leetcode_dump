class Robot:

    def __init__(self, width: int, height: int):
        self.x, self.y = 0, 0
        self.width, self.height = width, height
        self.dir_idx = "East"
        self.perimeter =  2*width + 2*height - 4



    def step(self, num: int) -> None:
        i = 0
        num %= self.perimeter
        if num == 0:
            num = self.perimeter
            
        

        while i < (num):
            if self.dir_idx == "East":
                if self.x + 1 < self.width:
                    self.x += 1
                    i += 1
                else:
                    self.dir_idx = "North"
            elif self.dir_idx == "North":
                if self.y + 1 < self.height:
                    self.y += 1
                    i += 1

                else:
                    self.dir_idx = "West"
            elif self.dir_idx == "West":
                if self.x - 1 >= 0:
                    self.x -= 1
                    i += 1
                else:
                    self.dir_idx = "South"
            elif self.dir_idx == "South":
                if self.y - 1 >= 0:
                    self.y -= 1
                    i += 1
                else:
                    self.dir_idx = "East"   

    def getPos(self) -> List[int]:
        return [self.x, self.y]
    
    def getDir(self) -> str:
        return self.dir_idx
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()