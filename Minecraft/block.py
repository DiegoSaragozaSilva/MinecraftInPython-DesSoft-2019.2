from panda3d.core import*

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
        self.blockModel = blockModel
        self.createBlock()

    def createBlock(self):
        self.placeholder = self.blocksNode.attachNewNode("block")
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
        self.createBlock()
        self.t = loader.loadTexture(self.texlocation)
        self.placeholder.setTexture(self.t)
        self.placeholder.setScale(0.5, 0.5, 0.5)
        self.placeholder.setPos(self.x, self.y, self.z)
        self.placeholder.reparentTo(self.MainNode)
        self.blockModel.instanceTo(self.placeholder)

    def destroyBlock(self):
        self.placeholder.detachNode()