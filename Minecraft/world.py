from block import Block
from panda3d.core import*
from direct.gui.OnscreenText import OnscreenText

class world():
    def __init__(self, screenWidth, screenHeight):
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.chuncksToRenderText = OnscreenText(pos = (-1.08, 0.95), scale = 0.05, mayChange=True, bg = (214, 214, 194, 0.5), fg = (255, 255, 255, 255))
        self.chuncksToDeleteText = OnscreenText(pos = (-1.02, 0.85), scale = 0.05, mayChange=True, bg = (214, 214, 194, 0.5), fg = (255, 255, 255, 255))
        self.worldChuncksText = OnscreenText(pos = (-0.955, 0.75), scale = 0.05, mayChange=True, bg = (214, 214, 194, 0.5), fg = (255, 255, 255, 255))
        self.ost = base.loader.loadSfx("assets/Sweden.mp3")

    def setupWorld(self):
        alight1 = DirectionalLight('dlight1')
        alight1.setColorTemperature(4500)
        alight2 = DirectionalLight('dlight2')
        alight2.setColorTemperature(4500)
        alnp1 = render.attachNewNode(alight1)
        alnp2 = render.attachNewNode(alight2)
        alnp1.setHpr(0, -45, 0)
        alnp2.setHpr(0, -135, 0)
        render.setLight(alnp1)
        render.setLight(alnp2)
        self.ost.play()

    def debugMode(self, state, worldChuncks):
        if state:
            render = 'Chuncks rendered: {0}'.format(str(len(worldChuncks[0])))
            delete = 'Chuncks not rendered: {0}'.format(str(len(worldChuncks[1])))
            world = 'Total chuncks in this world: {0}'.format(str(len(worldChuncks[2])))
            self.chuncksToRenderText.setText(render)
            self.chuncksToDeleteText.setText(delete)
            self.worldChuncksText.setText(world)