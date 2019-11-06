from block import Block
from panda3d.core import*
from direct.gui.OnscreenText import OnscreenText
from direct.gui.OnscreenImage import OnscreenImage

class world():
    def __init__(self, screenWidth, screenHeight, MainNode):
        #Tamanho do mundo
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        #Texto no jogo mostrando a quantidade de chunks que estao renderizados e chunks que ainda nao estao sendo renderizados
        self.chuncksToRenderText = OnscreenText(pos = (-1.08, 0.95), scale = 0.05, mayChange=True, bg = (214, 214, 194, 0.5), fg = (255, 255, 255, 255))
        self.chuncksToDeleteText = OnscreenText(pos = (-1.02, 0.85), scale = 0.05, mayChange=True, bg = (214, 214, 194, 0.5), fg = (255, 255, 255, 255))
        self.worldChuncksText = OnscreenText(pos = (-0.955, 0.75), scale = 0.05, mayChange=True, bg = (214, 214, 194, 0.5), fg = (255, 255, 255, 255))
        self.ost = base.loader.loadSfx("assets/Sweden.mp3")
        self.MainNode = MainNode
        #Criando a Crosshair
        print(DisplayRegion.getPixelHeight)
        print(DisplayRegion.getPixelWidth)
        self.Crosshair=OnscreenImage(image="textures/crosshair.png",pos=(0,0,0),scale=0.05)
        self.Crosshair.setTransparency(TransparencyAttrib.MAlpha)

    def setupWorld(self):
        #criacao de atributos esteticos do mundo, como iluminacao natural
        alight = AmbientLight('alight')
        alight.setColor(VBase4(255 / 255, 87 / 255, 3 / 255, 1))
        alnp = self.MainNode.attachNewNode(alight)
        self.MainNode.setLight(alnp)
        #inicio da musica no jogo
        self.ost.play()

    def debugMode(self, state, worldChuncks):
        #Funcao que efetivamente mostra o valor dos chunks carregadoes e nao na tela
        if state:
            render = 'Chuncks rendered: {0}'.format(str(len(worldChuncks[0])))
            delete = 'Chuncks not rendered: {0}'.format(str(len(worldChuncks[1])))
            world = 'Total chuncks in this world: {0}'.format(str(len(worldChuncks[2])))
            self.chuncksToRenderText.setText(render)
            self.chuncksToDeleteText.setText(delete)
            self.worldChuncksText.setText(world)