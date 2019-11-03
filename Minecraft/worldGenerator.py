from chunck import chunck
from player import player
from world import world
from panda3d.core import*
import numpy as np
from itertools import chain 

class worldGenerator():

    def __init__(self, MainNode, taskMgr, player, blocksNode):
        self.world = PerlinNoise2(100, 100)
        self.player = player
        self.MainNode = MainNode
        self.blocksNode = blocksNode
        self.blockModel = loader.loadModel("assets/box.egg")
        self.blockModel.setCollideMask(BitMask32.bit(0))
        self.height = 10
        self.width = 10
        self.taskMgr = taskMgr
        self.worldChuncks = []
        self.cToRender = []
        self.cToDelete = []
        self.renderDistance = 2

        for i in range(self.width):
            for j in range(self.height):
                self.worldChuncks.append(chunck(self.world, self.MainNode, i, j, self.blockModel, self.blocksNode))

        self.blocksNode.flattenStrong()
        self.blocksNode.clearModelNodes()

        self.taskMgr.add(self.checkRender, 'checkRender')

    def checkRender(self, task):
        ppos = self.player.returnPos()
        a = self.returnChuncksToRender(ppos[0], ppos[1])
        if not a[0] == self.cToRender:
            self.cToRender = a[0]
            for i in range(len(self.cToRender)):
                if not self.cToRender[i].rendered == True:
                    self.cToRender[i].renderChunck()

        if not a[1] == self.cToDelete:
            self.cToDelete = a[1]
            for i in range(len(self.cToDelete)):
                if self.cToDelete[i].rendered == True:
                    self.cToDelete[i].deleteChunck()

        return task.cont

    def returnChuncksToRender(self, px, py):
        coord = [int(px / 16), int(py / 16)]
        
        start_x = coord[0] - self.renderDistance
        start_y = coord[1] - self.renderDistance

        self.chuncksToRender = []
        self.chuncksToDelete = []

        r = np.array(self.worldChuncks).reshape(self.width, self.height)
        r = r.tolist()
        
        if start_x < 0:
            start_x = 0
        if start_y < 0:
            start_y = 0

        for chunck in (r[start_x : coord[0] + self.renderDistance]):
            self.chuncksToRender.append(chunck[start_y : coord[1] + self.renderDistance])
        
        self.chuncksToRender = list(chain.from_iterable(self.chuncksToRender))

        self.chuncksToDelete = list(set(self.worldChuncks) - set(self.chuncksToRender))

        return self.chuncksToRender, self.chuncksToDelete
