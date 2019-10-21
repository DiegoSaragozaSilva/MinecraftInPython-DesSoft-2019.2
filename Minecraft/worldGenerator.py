from chunck import chunck
from world import world
from panda3d.core import*

class worldGenerator():

    def __init__(self, MainNode, Ids, taskMgr):
        self.world = PerlinNoise2(10, 10)
        self.MainNode = MainNode
        self.blocksIds = Ids
        self.blockCounter = 0
        self.worldChuncks = [[0] * 3] * 3
        self.taskMgr = taskMgr
        for i in range(len(self.worldChuncks)):
            for j in range(len(self.worldChuncks)):
                self.worldChuncks[i][j] = chunck(self.world, self.MainNode, self.blocksIds, self.blockCounter, i, j)
                self.blockCounter += self.worldChuncks[i][j].returnBlockCounter()