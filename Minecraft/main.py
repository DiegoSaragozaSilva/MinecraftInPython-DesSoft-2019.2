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
        base.setBackgroundColor(0, 0, 1)
        self.blocksIds = dict()
        self.MainNode = render.attachNewNode('MainNode')
        self.xoffset = 0
        self.yoffset = 0
        self.playerSpeed = 0
        self.PickerTraverser = CollisionTraverser()
        self.CollisionQueue = CollisionHandlerQueue()
        self.PickRay = CollisionRay()
        self.PickNode = CollisionNode('pickRay')
        self.mouseNode = base.mouseWatcherNode
        self.wordGen = worldGenerator(self.MainNode, self.blocksIds, taskMgr)
        self.player = player(0, 0, 10, taskMgr, self.accept, render,
                             self.PickerTraverser, self.CollisionQueue,
                             self.PickRay, self.PickNode, self.mouseNode,
                             self.MainNode, self.blocksIds)
        self.heading = 0
        self.pitch = 0
        self.row = 0
        world.setupLights(self)

app = main()
app.run()
