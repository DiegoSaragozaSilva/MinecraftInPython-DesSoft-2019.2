from panda3d.core import*
import math
from worldGenerator import worldGenerator


class player():
    def __init__(self, x, y, z, taskMgr, accept, render,
                 PickerTraverser, CollisionQueue, PickRay,
                 PickNode, mouseNode, MainNode, blocksIds):
        self.x = x
        self.y = y
        self.z = z
        self.px, self.py = 0, 0
        self.accept = accept
        self.taskMgr = taskMgr
        self.render = render
        self.PickerTraverser = PickerTraverser
        self.CollisionQueue = CollisionQueue
        self.PickRay = PickRay
        self.PickNode = PickNode
        self.mouseNode = mouseNode
        self.MainNode = MainNode
        self.blocksIds = blocksIds
        self.player = loader.loadModel("box.egg")
        self.forward_button = KeyboardButton.ascii_key('w')
        self.backward_button = KeyboardButton.ascii_key('s')
        self.right_button = KeyboardButton.ascii_key('d')
        self.left_button = KeyboardButton.ascii_key('a')
        self.fly_button = KeyboardButton.ascii_key(' ')
        self.accept('mouse1', player.setupCollisions, extraArgs=[self])
        self.createPlayer()
        self.taskMgr.add(self.thirdPersonCameraTask, 'thirdPersonCameraTask')
        self.taskMgr.add(self.movePlayer, 'movePlayer')

    def createPlayer(self):

        self.player.reparentTo(render)
        self.player.setPos(self.x, self.y, self.z)
        base.cam.setPos(self.x, self.y, self.z)
        base.disableMouse()
        self.setupCollisions()

    def setupCollisions(self):

        self.PickRay.setOrigin(base.cam.getPos(self.render))
        self.PickRay.setDirection(
            self.render.getRelativeVector(base.cam, Vec3(0, 1, 0)))
        self.PickNode.addSolid(self.PickRay)
        self.PickNP = base.cam.attachNewNode(self.PickNode)
        self.PickNode.setFromCollideMask(GeomNode.getDefaultCollideMask())
        self.PickerTraverser.addCollider(self.PickNP, self.CollisionQueue)
        self.onMouseTask()

    def onMouseTask(self):
        if(self.mouseNode.hasMouse()):
            mpos = base.mouseWatcherNode.getMouse()
            self.PickRay.setFromLens(base.camNode, mpos.getX(), mpos.getY())
            self.PickerTraverser.traverse(self.MainNode)
            if(self.CollisionQueue.getNumEntries() > 0):
                self.CollisionQueue.sortEntries()
                entry = self.CollisionQueue.getEntry(0)
                pickedObj = entry.getIntoNodePath()
                pickedObj = pickedObj.getNetTag('block')
                if pickedObj is not None:
                    Obj = self.getObject(int(pickedObj))
                    Obj.destroy()

    def getObject(self, pickedObj):
        if pickedObj in self.blocksIds:
            return self.blocksIds[pickedObj]
        return None

    def thirdPersonCameraTask(self, task):
        for i in range(2):
            md = base.win.getPointer(0)
            x = md.getX()
            y = md.getY()
            if (x - self.px != 0 and y - self.py != 0):
                self.xoffset = x - float(base.win.getXSize() / 2)
                self.yoffset = y - float(base.win.getYSize() / 2)
                base.cam.setHpr(base.cam.getH() - self.xoffset,
                                base.cam.getP() - self.yoffset, 0)
                self.player.setHpr(base.cam.getH() - self.xoffset,
                                   base.cam.getP() - self.yoffset + 180, 0)
            else:
                base.win.movePointer(
                    0, int(base.win.getXSize() / 2), int(base.win.getYSize() / 2))
            self.px, self.py = x, y
        return task.cont

    def movePlayer(self, task):
        is_down = base.mouseWatcherNode.is_button_down
        playerXSpeed = 0
        playerYSpeed = 0
        if is_down(self.forward_button):
            playerYSpeed = -0.30
        if is_down(self.backward_button):
            playerYSpeed = 0.30
        if is_down(self.right_button):
            playerXSpeed = 0.30
        if is_down(self.left_button):
            playerXSpeed = -0.3
        self.player.setX(self.player, playerXSpeed)
        self.player.setY(self.player, playerYSpeed)
        base.cam.setPos(self.player.getPos())
        playerXSpeed = 0
        playerYSpeed = 0

        return task.cont
