from world import world
from block import Block
import random

class chunck():
    def __init__(self, n, MainNode, i, j, blockModel, blocksNode):
        self.maxDepth = 1
        self.width = 16
        self.height = 16
        self.world = n
        self.MainNode = MainNode
        self.blocksNode = blocksNode
        self.blocks = []
        self.n1 = i
        self.n2 = j
        self.rendered = False
        self.blockModel = blockModel
        self.createChunck()
        
    def createChunck(self):
        for i in range(self.n1 * self.width, self.n1 * self.width + self.width):
            for j in range(self.n2 * self.height, self.n2 * self.height + self.height):
                z = float('{0:.1f}'.format(self.returnZ(self.world.noise(i, j))))
                treeRandomizer = random.randint(0, 100)
                if z >= 1:
                    self.blocks.append(Block(
                        i, j, z, 'grass', self.MainNode, self.blockModel, self.blocksNode))
                    if (treeRandomizer <= 1):
                       self.createTree(i, j, z)
                    self.fill(i, j, z - 1)
                elif z == 0:
                    self.blocks.append(Block(
                        i, j, z, 'sand', self.MainNode, self.blockModel, self.blocksNode))

                    self.fill(i, j, z - 1)
                elif z <= -1:
                    self.blocks.append(Block(
                        i, j, -1, 'water', self.MainNode, self.blockModel, self.blocksNode))

                    self.blocks.append(Block(
                        i, j, -2, 'gravel', self.MainNode, self.blockModel, self.blocksNode))

                    self.fill(i, j, -2)
            

    def fill(self, i, j, z):
            for w in range(int(z) - (-self.maxDepth)):
                self.blocks.append(Block(
                    i, j, z - w, 'dirt', self.MainNode, self.blockModel, self.blocksNode))
                 

    def createTree(self, x, y, z):
        leafRandomizer = random.randint(0, 2)
        for i in range(4):
            self.blocks.append(Block(
                x, y, z + i + 1, 'oak', self.MainNode, self.blockModel, self.blocksNode))
             
        if leafRandomizer == 1:
            self.blocks.append(Block(
                x + 1, y, z + 4, 'leaf', self.MainNode, self.blockModel, self.blocksNode))
             
            self.blocks.append(Block(
                x - 1, y, z + 4, 'leaf', self.MainNode, self.blockModel, self.blocksNode))
             
            self.blocks.append(Block(
                x + 1, y + 1, z + 4, 'leaf', self.MainNode, self.blockModel, self.blocksNode))
             
            self.blocks.append(Block(
                x - 1, y - 1, z + 4, 'leaf', self.MainNode, self.blockModel, self.blocksNode))
             
            self.blocks.append(Block(
                x - 1, y + 1, z + 4, 'leaf', self.MainNode, self.blockModel, self.blocksNode))
             
            self.blocks.append(Block(
                x + 1, y - 1, z + 4, 'leaf', self.MainNode, self.blockModel, self.blocksNode))
             
            self.blocks.append(Block(
                x, y + 1, z + 4, 'leaf', self.MainNode, self.blockModel, self.blocksNode))
             
            self.blocks.append(Block(
                x, y - 1, z + 4, 'leaf', self.MainNode, self.blockModel, self.blocksNode))
             
            self.blocks.append(Block(
                x, y, z + 5, 'leaf', self.MainNode, self.blockModel, self.blocksNode))
             
    
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
    
    def renderChunck(self):
        self.rendered = True
        for i in range(len(self.blocks) - 1):
            self.blocks[i].updateBlock()

    def deleteChunck(self):
        self.rendered = False
        for i in range(len(self.blocks) - 1):
            self.blocks[i].destroyBlock()
