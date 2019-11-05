from panda3d.core import*
import copy

class Block():
    def __init__(self, x, y, z, t, MainNode, blockModel, blocksNode):
        #posicao do bloco
        self.x = x
        self.y = y
        #basicamente a camada em que o bloco esta, o que resulta do nome do bloco no aba chunk
        self.t = t
        self.z = z
        self.MainNode = MainNode
        self.blocksNode = blocksNode
        #qual o "nome do bloco"
        self.texlocation = ''
        #qual eh o modelo desse bloco
        self.blockModel = copy.copy(blockModel)
    #Retorna a textura apropiada para cada bloco baseado em sua coordenada no mundo
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
            self.blockModel.setTransparency(True)

        if self.t == "dirt":
            self.texlocation = "textures/dirt.png"

        if self.t == "water":
            self.texlocation = "textures/water.png"
    #Pega a textura do bloco e a coloca por cima do bloco
    def updateBlock(self):
        self.getTexture()
        self.t = loader.loadTexture(self.texlocation)
        self.t.setMagfilter(SamplerState.FT_nearest)
        self.blockModel.setTexture(self.t)
        self.blockModel.setPos(self.x, self.y, self.z)
        self.blockModel.reparentTo(self.blocksNode)
    #Destruir blocos
    def destroyBlock(self):
        self.blockModel.detachNode()