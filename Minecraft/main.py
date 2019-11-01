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
        base.setBackgroundColor(41 / 255, 148 / 255, 255 / 255)
        self.MainNode = render.attachNewNode('MainNode')
        self.blocksNode = self.MainNode.attachNewNode('blocksNode')
        self.xoffset = 0
        self.yoffset = 0
        self.playerSpeed = 0
        self.player = player(1, 1, 5, taskMgr, self.accept, self.MainNode, self.blocksNode)
        self.worldGen = worldGenerator(self.MainNode, taskMgr, self.player, self.blocksNode)
        self.heading = 0
        self.pitch = 0
        self.row = 0
        self.world = world(DisplayRegion.getPixelWidth, DisplayRegion.getPixelHeight)
        self.world.setupLights()
        taskMgr.add(self.updateDebugMode, 'updateDebugMode')

    def updateDebugMode(self, task):
        self.world.debugMode(False, [self.worldGen.cToRender, self.worldGen.cToDelete, self.worldGen.worldChuncks])
        return task.cont

app = main()
app.run()
