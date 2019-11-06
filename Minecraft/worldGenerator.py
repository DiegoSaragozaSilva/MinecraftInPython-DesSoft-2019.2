from chunck import chunck
from player import player
from world import world
import random
from panda3d.core import*
import numpy as np
from itertools import chain 

class worldGenerator():

    def __init__(self, MainNode, taskMgr, player, blocksNode):
        #criacao do mundo como um perilinNoise de tamanhos digitados
        self.Forest = PerlinNoise2(50, 50)
        self.Desert = PerlinNoise2(80, 80)
        self.Snow   = PerlinNoise2(35, 100)

        #dentro do mundo nos temos o atributo do player
        self.player = player

        #Node dos Blocos, o modelo de cada bloco e a caixa de colisao
        self.MainNode = MainNode
        self.blocksNode = blocksNode
        self.blockModel = loader.loadModel("assets/box.egg")
        self.blockModel.setCollideMask(BitMask32.bit(0))

        #tamanhos do mundo a ser renderizado
        self.height = 10
        self.width = 10
        self.taskMgr = taskMgr

        #Lista de chunks a serem renderizados, ja renderizados, e chunks deletados
        self.worldChuncks = []
        self.cToRender = []
        self.cToDelete = []
        

        #criacao do parametro da distancia de chuncks que o plaver consegue ver a partir dde sue coordenada
        self.renderDistance = 2

        #Criacao dos chunks dentro do espcado do mundo
        for i in range(self.width):
            for j in range(self.height):
                self.worldChuncks.append(chunck(self.Forest, self.MainNode, i, j, self.blockModel, self.blocksNode))

        self.blocksNode.flattenStrong()
        self.blocksNode.clearModelNodes()

        self.spawnPCToshi()
        self.taskMgr.add(self.checkRender, 'checkRender')
    #Verificacao de renderizacao de todos os chunks
    def checkRender(self, task):
        ppos = self.player.returnPos()
        a = self.returnChuncksToRender(ppos[0], ppos[1])
        if not a[0] == self.cToRender:
            self.cToRender = a[0]
            for i in range(len(self.cToRender)):
                if not self.cToRender[i].rendered == True:
                    self.cToRender[i].renderChunck()
    #Verificacao dos chunks a serem deletados 
        if not a[1] == self.cToDelete:
            self.cToDelete = a[1]
            for i in range(len(self.cToDelete)):
                if self.cToDelete[i].rendered == True:
                    self.cToDelete[i].deleteChunck()

        return task.cont
    #Armazenamento de chunks ainda nao renderizados, para depois renderizar baseado na renderDistance
    def returnChuncksToRender(self, px, py):
        #normalizacao de um chunk sendo 16 blocos por 16
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

    def spawnPCToshi(self):
        self.pcdotoshi = loader.loadModel('assets/toshismac.egg')
        self.pcdotoshi.setCollideMask(BitMask32.bit(0))
        self.pcdotoshi.reparentTo(self.MainNode)
        self.t = loader.loadTexture('textures/toshismac.png')
        self.t.setMagfilter(SamplerState.FT_nearest)
        self.pcdotoshi.setTexture(self.t)
        self.pcdotoshi.setScale(0.25, 0.25, 0.25)
        self.pcdotoshi.setPos(random.randint(0, 16 * self.height), random.randint(0, 16 * self.width), random.randint(0, 10))
        print(self.pcdotoshi.getPos())