from world import world
from player import player
from block import Block
from worldGenerator import worldGenerator
from chunck import chunck
from direct.showbase.ShowBase import*
from panda3d.core import*
from direct.task import Task
import math


class main(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        #cores para o fundo da tela
        base.setBackgroundColor(41 / 255, 148 / 255, 255 / 255)
        #sub nó dentro do render
        self.MainNode = render.attachNewNode('MainNode')
        #mais um sub nó, dessa vez dentro do propio mainNode
        self.blocksNode = self.MainNode.attachNewNode('blocksNode')
        self.worldGen = worldGenerator(self.MainNode, taskMgr, self.blocksNode, self.accept)
        self.world = world(DisplayRegion.getPixelWidth, DisplayRegion.getPixelHeight, self.MainNode)
        self.world.setupWorld()
        taskMgr.add(self.updateDebugMode, 'updateDebugMode')

    def updateDebugMode(self, task):
        if self.worldGen.player.victory == True:
            self.world.victoryRoyale()
        self.world.debugMode(True, [self.worldGen.cToRender, self.worldGen.cToDelete, self.worldGen.worldChuncks])
        return task.cont


app = main()
app.run()
