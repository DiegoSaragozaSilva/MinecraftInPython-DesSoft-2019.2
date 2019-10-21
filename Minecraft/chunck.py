from world import world
from block import Block
import random

class chunck():
    def __init__(self, n, MainNode, Ids, blockCounter, i, j):
        self.maxDepth = 1
        self.width = 16
        self.height = 16
        self.world = n
        self.blockCounter = blockCounter
        self.MainNode = MainNode
        self.blocksIds = Ids
        self.r = i
        self.r2 = j
        self.x = self.width * self.r
        self.y = self.height * self.r2
        self.createChunck()
        
    def createChunck(self):
        for i in range(self.x, self.width + self.x):
            for j in range(self.y, self.height + self.y):
                z = float('{0:.1f}'.format(self.returnZ(self.world.noise(i, j))))
                treeRandomizer = random.randint(0, 100)
                if z >= 2:
                    self.blocksIds[self.blockCounter] = Block(
                        i, j, z, self.blockCounter, 'grass', self.MainNode)
                    self.blockCounter += 1
                    if (treeRandomizer <= 2):
                        self.createTree(i, j, z)
                    self.fill(i, j, z - 1)
                elif z == 1:
                    self.blocksIds[self.blockCounter] = Block(
                        i, j, z, self.blockCounter, 'sand', self.MainNode)
                    self.blockCounter += 1
                    self.fill(i, j, z - 1)
                elif z == 0:
                    self.blocksIds[self.blockCounter] = Block(
                        i, j, 0, self.blockCounter, 'water', self.MainNode)
                    self.blockCounter += 1
                    self.blocksIds[self.blockCounter] = Block(
                        i, j, -1, self.blockCounter, 'gravel', self.MainNode)
                    self.blockCounter += 1
                    self.fill(i, j, -1)
                elif z < 0:
                    for w in range(-(int(z))):
                        self.blocksIds[self.blockCounter] = Block(
                            i, j, -w, self.blockCounter, 'water', self.MainNode)
                        self.blockCounter += 1
                    self.blocksIds[self.blockCounter] = Block(
                        i, j, z, self.blockCounter, 'gravel', self.MainNode)
                    self.blockCounter += 1
                    self.fill(i, j, z - 1)

        for block in self.blocksIds:
            self.blocksIds[block].updateBlocks()
            

    def fill(self, i, j, z):
            for w in range(int(z) - (-self.maxDepth)):
                self.blocksIds[self.blockCounter] = Block(
                    i, j, z - w, self.blockCounter, 'dirt', self.MainNode)
                self.blockCounter += 1

    def createTree(self, x, y, z):
        leafRandomizer = random.randint(0, 2)
        for i in range(4):
            self.blocksIds[self.blockCounter] = Block(
                x, y, z + i + 1, self.blockCounter, 'oak', self.MainNode)
            self.blockCounter += 1
        if leafRandomizer == 1:
            self.blocksIds[self.blockCounter] = Block(
                x + 1, y, z + 4,self.blockCounter, 'leaf', self.MainNode)
            self.blockCounter += 1
            self.blocksIds[self.blockCounter] = Block(
                x - 1, y, z + 4, self.blockCounter, 'leaf', self.MainNode)
            self.blockCounter += 1
            self.blocksIds[self.blockCounter] = Block(
                x + 1, y + 1, z + 4, self.blockCounter, 'leaf', self.MainNode)
            self.blockCounter += 1
            self.blocksIds[self.blockCounter] = Block(
                x - 1, y - 1, z + 4, self.blockCounter, 'leaf', self.MainNode)
            self.blockCounter += 1
            self.blocksIds[self.blockCounter] = Block(
                x - 1, y + 1, z + 4, self.blockCounter, 'leaf', self.MainNode)
            self.blockCounter += 1
            self.blocksIds[self.blockCounter] = Block(
                x + 1, y - 1, z + 4, self.blockCounter, 'leaf', self.MainNode)
            self.blockCounter += 1
            self.blocksIds[self.blockCounter] = Block(
                x, y + 1, z + 4, self.blockCounter, 'leaf', self.MainNode)
            self.blockCounter += 1
            self.blocksIds[self.blockCounter] = Block(
                x, y - 1, z + 4, self.blockCounter, 'leaf', self.MainNode)
            self.blockCounter += 1
            self.blocksIds[self.blockCounter] = Block(
                x, y, z + 5, self.blockCounter, 'leaf', self.MainNode)
            self.blockCounter += 1
    
    def returnBlockCounter(self):
        counter = self.blockCounter
        return counter
    
    def returnZ(self, z):
        if z >= 0 and z <= 0.1:
            return 0
        elif z >= 0.1 and z <= 0.2:
            return 1
        elif z >= 0.2 and z <= 0.3:
            return 2
        elif z >= 0.3 and z <= 0.4:
            return 3
        elif z >= 0.4 and z <= 0.5:
            return 4
        elif z >= 0.5 and z <= 0.6:
            return 5
        elif z >= 0.6 and z <= 0.7:
            return 6
        elif z >= 0.7 and z <= 0.8:
            return 7
        elif z >= 0.8 and z <= 0.9:
            return 8
        elif z >= 0.9 and z <= 1:
            return 9
        elif z >= 1:
            return 10

        elif z <= -0.1 and z >= -0.2:
            return -1
        elif z <= -0.2 and z >= -0.3:
            return -2
        elif z <= -0.3 and z >= -0.4:
            return -3
        elif z <= -0.4 and z >= -0.5:
            return -4
        elif z <= -0.5 and z >= -0.6:
            return -5
        elif z <= -0.6 and z >= -0.7:
            return -6
        elif z <= -0.7 and z >= -0.8:
            return -7
        elif z <= -0.8 and z >= -0.9:
            return -8
        elif z <= -0.9 and z >= -1:
            return -9
        elif z <= -1:
            return -10
        elif z < -0.0:
            return 0
        return None
    

