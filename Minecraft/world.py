from block import Block
from panda3d.core import*
import random


class world():

    def setupLights(self):
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
        linfog = Fog("worldFog")
        linfog.setColor(0, 0, 1)
        linfog.setLinearRange(0, 32)
        linfog.setLinearFallback(0, 16, 32)
        render.attachNewNode(linfog)
        render.setFog(linfog)
        base.camLens.setFar(32)
