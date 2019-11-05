from panda3d.core import*
import math


class player():
    def __init__(self, x, y, z, taskMgr, accept, MainNode, blocksNode):
        #posicao do player
        self.x = x * 2
        self.y = y * 2
        self.z = z
        #movimentacao da camera (tanto para cima quanto para os lados)
        self.xoff = 0
        self.yoff = 0
        self.zoff = 0
        self.px, self.py = 0, 0
        #atributo de pulo
        self.jumping = False
        #atributos usados durante a interacao do jogador com o mundo
        self.accept = accept
        self.taskMgr = taskMgr
        self.MainNode = MainNode
        self.playerNode = self.MainNode.attachNewNode('playerNode')
        self.blocksNode = blocksNode
        #modelo do jogador carregado na tela
        self.player = loader.loadModel("assets/box.egg")
        self.player.setScale(0.5, 0.5, 0.5)
        #funcao de andar do player em alguns botoes do teclado
        self.forward_button = KeyboardButton.ascii_key('w')
        self.backward_button = KeyboardButton.ascii_key('s')
        self.right_button = KeyboardButton.ascii_key('d')
        self.left_button = KeyboardButton.ascii_key('a')
        self.jump_button = KeyboardButton.ascii_key(' ')
        #cosntantes que afetam o jogador(Gravidade e a sua velocidade de moviemnto)
        self.gravityAcc = 0.15
        self.playerSpeed = 0.2

        #Barreira de colissao criada no player
        self.cTrav = CollisionTraverser()
        
        self.setupCollisions()
        self.createPlayer()
        #Criacao da camera em terceira pessoa que se move baseada na movimentacao do jogador
        self.taskMgr.add(self.thirdPersonCameraTask, 'thirdPersonCameraTask')
        self.taskMgr.add(self.movePlayer, 'movePlayer')

    #criacao do player dentro do mmundo
    def createPlayer(self):
        #Spawnando o jogador em coordenadas especificas+fixando o mause ao centro(efetivaemnte desabilitando o mesmo para sair do jogo sem um ALT+TAB)
        self.player.reparentTo(self.playerNode)
        self.player.setPos(self.x, self.y, self.z)
        base.cam.setPos(0, 0, 10)
        self.player.setP(180)
        #disabilitar a movimentacao padrao do Panda 3d
        base.disableMouse()

    #Funcionamente da camera baseada na movimentacao do mause
    def thirdPersonCameraTask(self, task):
        #calcuo do movimento feito peloo jogador quando usa o mause
        md = base.win.getPointer(0)
        x = md.getX()
        y = md.getY()
        #garantindo que a camera se mantenha parada se o jogador deixar de mexer no mause
        if (x - self.px != 0 and y - self.py != 0):
            self.xoffset = x - float(base.win.getXSize() / 2)
            self.yoffset = y - float(base.win.getYSize() / 2)
            base.cam.setHpr(base.cam.getH() - self.xoffset, base.cam.getP() - self.yoffset, 0)
            self.player.setH(self.player.getH() - self.xoffset)
        #caso contrario, movendo a camera baseando-se nos iputs de movimento    
        else:
            base.win.movePointer(0, int(base.win.getXSize() / 2), int(base.win.getYSize() / 2))
        self.px, self.py = x, y
        return task.cont

    #   Como que o jogador se movimenta pelo mundo
    def movePlayer(self, task):
        self.cTrav.traverse(self.MainNode)
        #Se nem um botando estiver sendo apertado, a velocidade do player tanto no eixo X quanto Y eh 0
        is_down = base.mouseWatcherNode.is_button_down
        playerXSpeed = 0
        playerYSpeed = 0

        #Movimentando o player em certas direcoes de acordo com o botao apertado
        if is_down(self.forward_button):
            playerYSpeed = -self.playerSpeed
        if is_down(self.backward_button):
            playerYSpeed = self.playerSpeed
        if is_down(self.right_button):
            playerXSpeed = self.playerSpeed
        if is_down(self.left_button):
            playerXSpeed = -self.playerSpeed
        if is_down(self.jump_button):
            if not self.jumping:
                self.jumping = True
                self.player.setZ(self.player, -1.75)
        #atualizacao das coordenadas do jogador
        self.player.setX(self.player, playerXSpeed)
        self.player.setY(self.player, playerYSpeed)
        #intereacao do movimento do jogador com a forca de gravidade e o topo dos blocos
        entries = list(self.playerGroundHandler.entries)
        entries.sort(key=lambda x: x.getSurfacePoint(self.MainNode).getZ())
        if len(entries) > 0:
            if entries[len(entries) - 1].getSurfacePoint(self.MainNode).getZ() + 1.5 < int(self.z):
                self.player.setZ(self.player, self.gravityAcc)
            else:
                self.jumping = False
        #Fixando a camera do centro da tela, se movendo tambem com o player
        base.cam.setPos(self.player.getPos())
        self.x = self.player.getX()
        self.y = self.player.getY()
        self.z = self.player.getZ()
        playerXSpeed = 0
        playerYSpeed = 0
        return task.cont
    #funcao que retorna as coordenadas x e y do jogador a cada frame
    def returnPos(self):
        return [self.x, self.y]

    #processo de verificacao e ultilizacao da colisao com blocos
    def setupCollisions(self):
        self.playerCol = CollisionNode('player')
        #criacao da barreira de colissao que tem a sua origem no potno central do jogador
        self.playerCol.addSolid(CollisionBox(0, 1.25, 1.25, 2))
        self.playerCol.setFromCollideMask(CollideMask.bit(0))
        self.playerCol.setIntoCollideMask(CollideMask.allOff())
        self.playerColNp = self.player.attachNewNode(self.playerCol)
        self.playerPusher = CollisionHandlerPusher()
        self.playerPusher.horizontal = False

        self.playerPusher.addCollider(self.playerColNp, self.player)
        self.cTrav.addCollider(self.playerColNp, self.playerPusher)

        self.playerGroundRay = CollisionRay()
        self.playerGroundRay.setOrigin(0, 0, 0)
        self.playerGroundRay.setDirection(0, 0, 1)
        self.playerGroundCol = CollisionNode('playerRay')
        self.playerGroundCol.addSolid(self.playerGroundRay)
        self.playerGroundCol.setFromCollideMask(CollideMask.bit(0))
        self.playerGroundCol.setIntoCollideMask(CollideMask.allOff())
        self.playerGroundColNp = self.player.attachNewNode(self.playerGroundCol)
        self.playerGroundHandler = CollisionHandlerQueue()
        self.cTrav.addCollider(self.playerGroundColNp, self.playerGroundHandler)

        self.playerGroundColNp.show()
        self.playerColNp.show()