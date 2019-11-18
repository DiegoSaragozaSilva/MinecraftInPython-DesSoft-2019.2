from world import world
from block import Block
import random

class chunck():
    def __init__(self, n, MainNode, i, j, blockModel, blocksNode):
        #atributos de uma chunk(profundidade,tamanho e largura )
        self.maxDepth = 5
        self.width = 16
        self.height = 16
        self.world = n
        self.MainNode = MainNode
        self.blocksNode = blocksNode
        #lsita de blocos dentro da chunl
        self.blocks = []
        #coordenadas das chunks(por exemplo: se criamos um mundo 3 por 3 chunks, "i" e "j" representam a posicao dessa chunk no mundo )
        self.n1 = i
        self.n2 = j
        #no inicio, nem uma chunk eh renderizada
        self.rendered = False
        self.blockModel = blockModel
        self.createChunck()

    # colocando todos os blocos dentro de uma chink se baseando no valor da cor do Perling Noise Criado   
    def createChunck(self):
        for i in range(self.n1 * self.width, self.n1 * self.width + self.width):
            for j in range(self.n2 * self.height, self.n2 * self.height + self.height):
                z = float('{0:.1f}'.format(self.returnZ(self.world.noise(i, j))))
                treeRandomizer = random.randint(0, 100)
                #atribuindo o nome de cada bloco na chunk sabendo a sua posicao Z na mesma
                if z >= 1:
                    self.blocks.append(Block(
                        i, j, z, 'grass', self.MainNode, self.blockModel, self.blocksNode))
                    if (treeRandomizer <= 1):
                       self.createTree(i, j, z)
                    self.fill(i, j, z - 1)
                elif z == 0:
                    self.blocks.append(Block(
                        i, j, z, 'sand', self.MainNode, self.blockModel, self.blocksNode))

                    self.fill(i, j, z - 1)
                elif z <= -1:
                    self.blocks.append(Block(
                        i, j, -1, 'water', self.MainNode, self.blockModel, self.blocksNode))

                    self.blocks.append(Block(
                        i, j, -2, 'gravel', self.MainNode, self.blockModel, self.blocksNode))

                    self.fill(i, j, -2)
            
    #Fazendo com que abaixo de qualquer bloco criado pelo processo incial, seja um bloco de terra(execao para gravel sendo gerada abaixo da agua)
    def fill(self, i, j, z):
            for w in range(int(z) - (-self.maxDepth)):
                self.blocks.append(Block(
                    i, j, z - w, 'dirt', self.MainNode, self.blockModel, self.blocksNode))
                 
    #Criando arvores baseado em uma probabilidade que qualquer bloco de grama tem
    def createTree(self, x, y, z):
        leafRandomizer = random.randint(0, 2)
        for i in range(4):
            self.blocks.append(Block(
                x, y, z + i + 1, 'oak', self.MainNode, self.blockModel, self.blocksNode))
        #criaca das multiplas distribuicoes de folhas   
        if leafRandomizer == 1:
            self.blocks.append(Block(
                x + 1, y, z + 4, 'leaf', self.MainNode, self.blockModel, self.blocksNode))
             
            self.blocks.append(Block(
                x - 1, y, z + 4, 'leaf', self.MainNode, self.blockModel, self.blocksNode))
             
            self.blocks.append(Block(
                x + 1, y + 1, z + 4, 'leaf', self.MainNode, self.blockModel, self.blocksNode))
             
            self.blocks.append(Block(
                x - 1, y - 1, z + 4, 'leaf', self.MainNode, self.blockModel, self.blocksNode))
             
            self.blocks.append(Block(
                x - 1, y + 1, z + 4, 'leaf', self.MainNode, self.blockModel, self.blocksNode))
             
            self.blocks.append(Block(
                x + 1, y - 1, z + 4, 'leaf', self.MainNode, self.blockModel, self.blocksNode))
             
            self.blocks.append(Block(
                x, y + 1, z + 4, 'leaf', self.MainNode, self.blockModel, self.blocksNode))
             
            self.blocks.append(Block(
                x, y - 1, z + 4, 'leaf', self.MainNode, self.blockModel, self.blocksNode))
             
            self.blocks.append(Block(
                x, y, z + 5, 'leaf', self.MainNode, self.blockModel, self.blocksNode))
             
    #Funcao que retorna o valor Z de um bloco dentro de uma chunk, sendo usada em cima para determianr qual bloco sera esse
    def returnZ(self, z):
        if z >= 0 and z <= 0.1:
            return 0
        elif z >= 0.1 and z <= 0.2:
            return 1
        elif z >= 0.2 and z <= 0.3:
            return 2
        elif z >= 0.3 and z <= 0.4:
            return 3
        elif z >= 0.4 and z <= 0.5:
            return 4
        elif z >= 0.5 and z <= 0.6:
            return 5
        elif z >= 0.6 and z <= 0.7:
            return 6
        elif z >= 0.7 and z <= 0.8:
            return 7
        elif z >= 0.8 and z <= 0.9:
            return 8
        elif z >= 0.9 and z <= 1:
            return 9
        elif z >= 1:
            return 10

        elif z <= -0.1 and z >= -0.2:
            return -1
        elif z <= -0.2 and z >= -0.3:
            return -2
        elif z <= -0.3 and z >= -0.4:
            return -3
        elif z <= -0.4 and z >= -0.5:
            return -4
        elif z <= -0.5 and z >= -0.6:
            return -5
        elif z <= -0.6 and z >= -0.7:
            return -6
        elif z <= -0.7 and z >= -0.8:
            return -7
        elif z <= -0.8 and z >= -0.9:
            return -8
        elif z <= -0.9 and z >= -1:
            return -9
        elif z <= -1:
            return -10
        elif z < -0.0:
            return 0
        return None
    #funcao que renderinza os blocos de uma nova chunk quando o jogador sai da chunk anterior
    def renderChunck(self):
        self.rendered = True
        for i in range(len(self.blocks) - 1):
            self.blocks[i].updateBlock()
    #funcao que des-renderinza os blocos de uma antiga chunk quando o jogador entra em uma chunk nova
    def deleteChunck(self):
        self.rendered = False
        for i in range(len(self.blocks) - 1):
            self.blocks[i].destroyBlock()

    def createBlock(self, x, y, z):
        self.blocks.append(Block(x, y, z, 'dirt', self.MainNode, self.blockModel, self.blocksNode))
        self.blocks[len(self.blocks) - 1].updateBlock()
