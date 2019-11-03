from panda3d.core import*
import copy

class Block():
    def __init__(self, x, y, z, t, MainNode, blockModel, blocksNode):
        self.x = x
        self.y = y
        self.t = t
        self.z = z
        self.iN = 0
        self.MainNode = MainNode
        self.blocksNode = blocksNode
        self.texlocation = ''
        self.blockModel = copy.copy(blockModel)

    def getTexture(self):
        if self.t == "grass":
            self.texlocation = "textures/grass.png"

        if self.t == "sand":
            self.texlocation = "textures/sand.png"

        if self.t == "gravel":
            self.texlocation = "textures/gravel.png"

        if self.t == "oak":
            self.texlocation = "textures/oak.png"

        if self.t == "leaf":
            self.texlocation = "textures/leaf.png"

        if self.t == "dirt":
            self.texlocation = "textures/dirt.png"

        if self.t == "water":
            self.texlocation = "textures/water.png"

    def updateBlock(self):
        self.getTexture()
        self.t = loader.loadTexture(self.texlocation)
        self.blockModel.setTexture(self.t)
        self.blockModel.setScale(0.5, 0.5, 0.5)
        self.blockModel.setPos(self.x, self.y, self.z)
        self.blockModel.reparentTo(self.blocksNode)

    def destroyBlock(self):
        self.blockModel.detachNode()