from panda3d.core import*
import math


class player():
    def __init__(self, x, y, z, taskMgr, accept, MainNode, blocksNode):
        self.x = x * 2
        self.y = y * 2
        self.z = z
        self.xoff = 0
        self.yoff = 0
        self.zoff = 0
        self.px, self.py = 0, 0
        self.accept = accept
        self.taskMgr = taskMgr
        self.MainNode = MainNode
        self.playerNode = self.MainNode.attachNewNode('playerNode')
        self.blocksNode = blocksNode
        self.player = loader.loadModel("box.egg")
        self.player.setScale(0.5, 0.5, 0.5)
        self.forward_button = KeyboardButton.ascii_key('w')
        self.backward_button = KeyboardButton.ascii_key('s')
        self.right_button = KeyboardButton.ascii_key('d')
        self.left_button = KeyboardButton.ascii_key('a')
        self.fly_button = KeyboardButton.ascii_key(' ')
        self.gravityAcc = 0.1
        self.cTrav = CollisionTraverser()
        
        self.setupCollisions()
        self.createPlayer()

        self.taskMgr.add(self.thirdPersonCameraTask, 'thirdPersonCameraTask')
        self.taskMgr.add(self.movePlayer, 'movePlayer')

    def createPlayer(self):
        self.player.reparentTo(self.playerNode)
        self.player.setPos(self.x, self.y, self.z)
        base.cam.setPos(0, 0, 10)
        self.player.setP(180)
        base.disableMouse()

    def thirdPersonCameraTask(self, task):
        md = base.win.getPointer(0)
        x = md.getX()
        y = md.getY()
        if (x - self.px != 0 and y - self.py != 0):
            self.xoffset = x - float(base.win.getXSize() / 2)
            self.yoffset = y - float(base.win.getYSize() / 2)
            base.cam.setHpr(base.cam.getH() - self.xoffset, base.cam.getP() - self.yoffset, 0)
            self.player.setH(self.player.getH() - self.xoffset)
            
        else:
            base.win.movePointer(0, int(base.win.getXSize() / 2), int(base.win.getYSize() / 2))
        self.px, self.py = x, y
        return task.cont

    def movePlayer(self, task):
        self.cTrav.traverse(self.MainNode)
        is_down = base.mouseWatcherNode.is_button_down
        playerXSpeed = 0
        playerYSpeed = 0
        if is_down(self.forward_button):
            playerYSpeed = -0.1
        if is_down(self.backward_button):
            playerYSpeed = 0.1
        if is_down(self.right_button):
            playerXSpeed = 0.1
        if is_down(self.left_button):
            playerXSpeed = -0.1
        self.player.setX(self.player, playerXSpeed)
        self.player.setY(self.player, playerYSpeed)
        
        entries = list(self.playerGroundHandler.entries)
        entries.sort(key=lambda x: x.getSurfacePoint(self.MainNode).getZ())
        if len(entries) > 0:
            if entries[len(entries) - 1].getSurfacePoint(self.MainNode).getZ() + 0.5  + 1 < self.z:
                self.player.setZ(self.player, self.gravityAcc)
        
        base.cam.setPos(self.player.getPos())
        self.x = self.player.getX()
        self.y = self.player.getY()
        self.z = self.player.getZ()
        playerXSpeed = 0
        playerYSpeed = 0
        return task.cont

    def returnPos(self):
        return [self.x, self.y]

    def setupCollisions(self):
        self.playerCol = CollisionNode('player')
        self.playerCol.addSolid(CollisionBox(0, 1.1, 1.1, 1.1))
        self.playerCol.setFromCollideMask(CollideMask.bit(0))
        self.playerCol.setIntoCollideMask(CollideMask.allOff())
        self.playerColNp = self.player.attachNewNode(self.playerCol)
        self.playerPusher = CollisionHandlerPusher()
        self.playerPusher.horizontal = False

        self.playerPusher.addCollider(self.playerColNp, self.player)
        self.cTrav.addCollider(self.playerColNp, self.playerPusher)

        self.playerGroundRay = CollisionRay()
        self.playerGroundRay.setOrigin(0, 0, 9)
        self.playerGroundRay.setDirection(0, 0, -1)
        self.playerGroundCol = CollisionNode('playerRay')
        self.playerGroundCol.addSolid(self.playerGroundRay)
        self.playerGroundCol.setFromCollideMask(CollideMask.bit(0))
        self.playerGroundCol.setIntoCollideMask(CollideMask.allOff())
        self.playerGroundColNp = self.player.attachNewNode(self.playerGroundCol)
        self.playerGroundHandler = CollisionHandlerQueue()
        self.cTrav.addCollider(self.playerGroundColNp, self.playerGroundHandler)

        self.playerColNp.show()