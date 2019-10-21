class Block():
    def __init__(self, x, y, z, n, t, MainNode):
        self.x = x
        self.y = y
        self.t = t
        self.z = z
        self.n = n
        self.iN = 0
        self.block = loader.loadModel("box.egg")
        self.MainNode = MainNode
        self.textlocation = ''
        self.createBlock()

    def createBlock(self):
        if self.t == "grass":
            self.texlocation = "icons/grass.png"

        if self.t == "sand":
            self.texlocation = "icons/sand.png"

        if self.t == "gravel":
            self.texlocation = "icons/gravel.png"

        if self.t == "oak":
            self.texlocation = "icons/oak.png"

        if self.t == "leaf":
            self.texlocation = "icons/leaf.png"
            self.block.setTransparency(True)

        if self.t == "dirt":
            self.texlocation = "icons/dirt.png"

        if self.t == "water":
            self.texlocation = "icons/water.png"
            self.block.setTransparency(True)

    def updateBlocks(self):
        self.block.reparentTo(self.MainNode)
        self.t = loader.loadTexture(self.texlocation)
        self.block.setTexture(self.t)
        self.block.setScale(0.5, 0.5, 0.5)
        self.block.setPos(self.x, self.y, self.z)
        self.block.setTag('block', str(self.n))

    def destroy(self):
        self.block.removeNode()

    def returnZ(self, z):
        if z >= 0 and z <= 0.1:
            self.t = 'water'
            return 0
        elif z >= 0.1 and z <= 0.2:
            self.t = 'sand'
            return 1
        elif z >= 0.2 and z <= 0.3:
            self.t = 'grass'
            return 2
        elif z >= 0.3 and z <= 0.4:
            self.t = 'grass'
            return 3
        elif z >= 0.4 and z <= 0.5:
            self.t = 'grass'
            return 4
        elif z >= 0.5 and z <= 0.6:
            self.t = 'grass'
            return 5
        elif z >= 0.6 and z <= 0.7:
            self.t = 'grass'
            return 6
        elif z >= 0.7 and z <= 0.8:
            self.t = 'grass'
            return 7
        elif z >= 0.8 and z <= 0.9:
            self.t = 'grass'
            return 8
        elif z >= 0.9 and z <= 1:
            self.t = 'grass'
            return 9
        elif z >= 1:
            self.t = 'grass'
            return 10

        elif z <= -0.1 and z >= -0.2:
            self.t = 'water'
            return -1
        elif z <= -0.2 and z >= -0.3:
            self.t = 'water'
            return -2
        elif z <= -0.3 and z >= -0.4:
            self.t = 'water'
            return -3
        elif z <= -0.4 and z >= -0.5:
            self.t = 'water'
            return -4
        elif z <= -0.5 and z >= -0.6:
            self.t = 'water'
            return -5
        elif z <= -0.6 and z >= -0.7:
            self.t = 'water'
            return -6
        elif z <= -0.7 and z >= -0.8:
            self.t = 'water'
            return -7
        elif z <= -0.8 and z >= -0.9:
            self.t = 'water'
            return -8
        elif z <= -0.9 and z >= -1:
            self.t = 'water'
            return -9
        elif z <= -1:
            self.t = 'water'
            return -10
        elif z < -0.0:
            self.t = 'dirt'
            return 0
        return None

