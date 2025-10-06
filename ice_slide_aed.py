import pyxel
import ast
import random
import time
import math

world = []
initial_x = 0
initial_y = 0
master = -999
master_memory = 1
break_thick = True
fps = 13
wave_speed = 13
counter = 0
wave = False
last = 0
difficulty = 1
clouds = []
cloud_marker = -100

class Cloud:
    def __init__(self, type, pos_x, pos_y, back):
        self.type = type
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.back = back
    def move(self):
        pyxel.blt(self.pos_x, self.pos_y, 1,208,((self.type-1)*32)+16,48,32,8,2)
        self.pos_x += 0.5

for i in range(random.randint(3,5)):
    cloud = Cloud(random.randint(1,5),random.randint(20, 232), random.randint(20, 80), random.randint(1,3))
    for i in clouds:
        if cloud.pos_x > i.pos_x - 50 and cloud.pos_x < i.pos_x + 50 and cloud.pos_y > i.pos_y - 20 and cloud.pos_y < i.pos_y + 20:
            cloud.pos_x += 60

    clouds.append(cloud)

def definir_mundo(master):
    global world, initial_x, initial_y, last, difficulty
    world = []
    if difficulty ==1:
        with open("map_lists.txt", "r") as f:
            lines = f.readlines()
            content = ast.literal_eval(lines[master-1])
            
        if content[2]==1:
            last = 1
            
        for y in range(16):
            temp_array = []            
            for x in range(16):
                temp_row = [0]
                valor = 1 
                for i in range(len(content[1])):
                    if content[1][i][0] == x and content[1][i][1] == y:
                        valor = content[1][i][2]
                        break  
                if valor == 5 or valor == 1 or valor ==2:
                    temp_row.append(random.randint(-5,-1))
                else:
                    temp_row.append(0)
                temp_row.insert(0,valor)
                temp_array.append(temp_row)
            world.append(temp_array)

        initial_x = content[0][0]
        initial_y = content[0][1]
    elif difficulty == 2:
        with open("hard_map_lists.txt", "r") as f:
            lines = f.readlines()
            content = ast.literal_eval(lines[master-1])
            
        if content[2]==1:
            last = 1
            
        for y in range(16):
            temp_array = []            
            for x in range(16):
                temp_row = [0]
                valor = 1 
                for i in range(len(content[1])):
                    if content[1][i][0] == x and content[1][i][1] == y:
                        valor = content[1][i][2]
                        break  
                if valor == 5 or valor == 1 or valor ==2:
                    temp_row.append(random.randint(-5,-1))
                else:
                    temp_row.append(0)
                temp_row.insert(0,valor)
                temp_array.append(temp_row)
            world.append(temp_array)

        initial_x = content[0][0]+2
        initial_y = content[0][1]

        world[initial_y][initial_x-2][0]=7


##GUIA MASTER:
# master = -1 : derrota
# master = -2 : vitória
# master = -999: Menu inicial
# master = -998: pré retorno pro menu inicial
# master = -1000 : dificuldade ganha
# master = 0 : neutro
# master = inteiro positivo : level

##Dying
#se for 1, morre afogado, se for 4, morre por contusão
        

definir_mundo(1)

def trilha(x, y):
    global break_thick
    for j in range(16):
        for i in range(16):
            if ((world[j][i][0]) == 0):
                world[j][i][0] = -1

            if world[j][i][1] >0 and world[j][i][1]<3 and world[j][i][0]!= 2 and world[j][i][0]!=7 and world[j][i][0]!=9:
                world[j][i][0] = 0
                world[j][i][1] -= 1

            if world[j][i][1] == 3:
             world[j][i][1] -=1
            
            if world[j][i][0] == 2 and world[j][i][1]==1:
                world[j][i][0] = 1
                world[j][i][1] = 0

            if world[j][i][0] == 2 and world[j][i][1]==2:
                world[j][i][1] = 1

    if world[y][x][0] ==1:
        world[y][x][1] = 3
    if world[y][x][0] == 2 and break_thick == True:
        world[y][x][1] = 2

class Jogo:
    def __init__(self):
        self.x = 8
        self.y = 5
        self.move = True
        self.direction = None
        self.selection = 1      
        self.dying = 0  
        pyxel.init(320, 256, title="Ice Slide",fps = fps)
        pyxel.load("assets_ice_slide.pyxres") 
        pyxel.run(self.update, self.draw)

    def update(self):
        global world, master_memory, master, initial_x, initial_y, last, difficulty, break_thick, clouds, cloud_marker

        if master == -998:
            time.sleep(0.3)
            master = -999

        if pyxel.frame_count < 1:
                pyxel.playm(1, loop=True)

        if master == -1000:
            self.direction = None
            self.move = False
            if (pyxel.btnp(pyxel.KEY_A)==True or pyxel.btnp(pyxel.KEY_LEFT)==True):
                self.selection = -1
                pyxel.play(0,5)
            elif (pyxel.btnp(pyxel.KEY_D)==True or pyxel.btnp(pyxel.KEY_RIGHT)==True):
                self.selection = -2
                pyxel.play(0,5)

            if self.selection == -1 and (pyxel.btnp(pyxel.KEY_SPACE)==True or pyxel.btnp(pyxel.KEY_RETURN)==True):
                pyxel.quit()
            elif self.selection == -2 and (pyxel.btnp(pyxel.KEY_SPACE)==True or pyxel.btnp(pyxel.KEY_RETURN)==True):
                self.move = False
                self.direction = None
                self.selection = 1 
                master_memory = 1
                last=0
                master = -998
                pyxel.play(0,4)
                time.sleep(0.2)
                pyxel.playm(1, loop=True)     

        if master == -999:
            self.direction = None
            self.move = False
            if (self.selection ==1 or self.selection==2) and (pyxel.btnp(pyxel.KEY_D)==True or pyxel.btnp(pyxel.KEY_RIGHT)==True):
                self.selection = int(self.selection*10)
                pyxel.play(0,5)
            if (self.selection ==10 or self.selection==20) and (pyxel.btnp(pyxel.KEY_A)==True or pyxel.btnp(pyxel.KEY_LEFT)==True):
                self.selection = int(self.selection/10)
                pyxel.play(0,5)
            if (self.selection ==2 or self.selection==20) and (pyxel.btnp(pyxel.KEY_W)==True or pyxel.btnp(pyxel.KEY_UP)==True):
                self.selection = int(self.selection/2)
                pyxel.play(0,5)
            if (self.selection ==1 or self.selection==10) and (pyxel.btnp(pyxel.KEY_S)==True or pyxel.btnp(pyxel.KEY_DOWN)==True):
                self.selection = int(self.selection*2)
                pyxel.play(0,5)
            #modo facil
            if self.selection == 1 and (pyxel.btnp(pyxel.KEY_SPACE)==True or pyxel.btnp(pyxel.KEY_RETURN)==True):
                self.move=True
                difficulty = 1
                master = master_memory
                definir_mundo(master)
                self.x = initial_x
                self.y = initial_y
                pyxel.stop()
                pyxel.play(0,4)
                time.sleep(0.2)
                pyxel.play(1,28,0, loop=True)
            #sair do jogo
            elif self.selection == 2 and (pyxel.btnp(pyxel.KEY_SPACE)==True or pyxel.btnp(pyxel.KEY_RETURN)==True):
                pyxel.quit()
            #modo dificil    
            elif self.selection == 10 and (pyxel.btnp(pyxel.KEY_SPACE)==True or pyxel.btnp(pyxel.KEY_RETURN)==True):
                self.move=True
                difficulty = 2
                master = master_memory
                definir_mundo(master)
                self.x = initial_x
                self.y = initial_y
                pyxel.stop()
                pyxel.play(0,4)
                time.sleep(0.2)
                pyxel.play(1,28,0, loop=True)
            #como jogar    
            elif self.selection == 20 and (pyxel.btnp(pyxel.KEY_SPACE)==True or pyxel.btnp(pyxel.KEY_RETURN)==True):
                master = -997
                self.selection = -1
                pyxel.stop()
                pyxel.play(0,4)
                time.sleep(0.2)
                return                                  
        if master == -997:
        # Voltar para o menu principal
            if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_RETURN):
                master = -999
                self.selection = 1
                pyxel.play(0,4)
                pyxel.playm(1, loop=True)               
            # Ir para a página da DIREITA 
            if (pyxel.btnp(pyxel.KEY_D) or pyxel.btnp(pyxel.KEY_RIGHT)) and self.selection == -1:
                self.selection = -2
                pyxel.play(0,5)

            # Ir para a página da ESQUERDA
            if (pyxel.btnp(pyxel.KEY_A) or pyxel.btnp(pyxel.KEY_LEFT)) and self.selection == -2:
                self.selection = -1
                pyxel.play(0,5)

        if pyxel.btnp(pyxel.KEY_R)==True and self.move==True and master > 0:
            master = master_memory
            definir_mundo(master) 
            self.x=initial_x
            self.y=initial_y

        if master == -1:
            if (pyxel.btnp(pyxel.KEY_A)==True or pyxel.btnp(pyxel.KEY_LEFT)==True):
                self.selection = -1
                pyxel.play(0,5)
            elif (pyxel.btnp(pyxel.KEY_D)==True or pyxel.btnp(pyxel.KEY_RIGHT)==True):
                self.selection = -2
                pyxel.play(0,5)

            if self.selection == -1 and (pyxel.btnp(pyxel.KEY_SPACE)==True or pyxel.btnp(pyxel.KEY_RETURN)==True):
                self.move = False
                self.direction = None
                self.selection = 1 
                master_memory = 1
                self.dying = 0
                master = -998
                pyxel.play(0,4)
                time.sleep(0.2)
                pyxel.playm(1, loop=True)
            elif self.selection == -2 and (pyxel.btnp(pyxel.KEY_SPACE)==True or pyxel.btnp(pyxel.KEY_RETURN)==True):
                master = master_memory
                definir_mundo(master)
                self.selection = -2
                self.x=initial_x
                self.y=initial_y
                self.direction = None
                self.move = True
                self.dying = 0
                pyxel.play(0,4)
                time.sleep(0.2)
                pyxel.play(1,28,0, loop=True)

        if master == -2:
            if ((pyxel.btnp(pyxel.KEY_A)==True or pyxel.btnp(pyxel.KEY_LEFT)==True)) and (self.selection == -2 or self.selection == -3):
                self.selection += 1
                pyxel.play(0,5)
            elif (pyxel.btnp(pyxel.KEY_D)==True or pyxel.btnp(pyxel.KEY_RIGHT)==True) and (self.selection == -1 or self.selection == -2):
                self.selection -= 1
                pyxel.play(0,5)

            if self.selection == -1 and (pyxel.btnp(pyxel.KEY_SPACE)==True or pyxel.btnp(pyxel.KEY_RETURN)==True):
                self.move = False
                self.direction = None
                self.selection = 1 
                master_memory = 1
                self.dying = 0
                master = -998
                pyxel.play(0,4)
                time.sleep(0.2)
                pyxel.playm(1, loop=True)

            elif self.selection == -2 and (pyxel.btnp(pyxel.KEY_SPACE)==True or pyxel.btnp(pyxel.KEY_RETURN)==True):
                master = master_memory
                definir_mundo(master)
                self.selection = -2
                self.x=initial_x
                self.y=initial_y
                self.direction = None
                self.move = True
                self.dying = 0
                pyxel.play(0,4)
                time.sleep(0.2)
                pyxel.play(1,28,0, loop=True)

            elif self.selection == -3 and (pyxel.btnp(pyxel.KEY_SPACE)==True or pyxel.btnp(pyxel.KEY_RETURN)==True):
                master_memory += 1
                master = master_memory
                definir_mundo(master)
                self.x=initial_x
                self.y=initial_y
                self.selection = -2
                self.direction = None
                self.move = True
                pyxel.play(0,4)
                time.sleep(0.2)
                pyxel.play(1,28,0, loop=True)

        if self.dying ==4:
            time.sleep(0.7)
            master = -1
            self.dying = 5
        if self. dying ==3:
            master = -1
        if self.dying == 1 or self.dying ==2:
            time.sleep(0.5)
            self.dying+= 1

        if (pyxel.btn(pyxel.KEY_W)==True or pyxel.btnp(pyxel.KEY_UP)==True) and self.move == True and master > 0:
            self.direction = "north"
            self.move = False
            break_thick = True
            if world[self.y][self.x-2][0] == 2:
                world[self.y][self.x-2][1] = 2
        elif (pyxel.btn(pyxel.KEY_S)==True or pyxel.btnp(pyxel.KEY_DOWN)==True) and self.move == True and master > 0:
            self.direction = "south"
            self.move = False
            break_thick = True
            if world[self.y][self.x-2][0] == 2:
                world[self.y][self.x-2][1] = 2
        elif (pyxel.btn(pyxel.KEY_A)==True or pyxel.btnp(pyxel.KEY_LEFT)==True) and self.move == True and master > 0:
            self.direction = "west"
            self.move = False
            break_thick = True
            if world[self.y][self.x-2][0] == 2:
                world[self.y][self.x-2][1] = 2
        elif (pyxel.btn(pyxel.KEY_D)==True or pyxel.btnp(pyxel.KEY_RIGHT)==True) and self.move == True and master > 0:
            self.direction = "east"
            self.move = False
            break_thick = True
            if world[self.y][self.x-2][0] == 2:
                world[self.y][self.x-2][1] = 2

        if self.move == False and self.direction == "north" and master > 0 and self.dying ==0:
            if (world[self.y-1][self.x-2][0] == 5):
                self.move = True
                pyxel.play(0,6)
            else:
                if world[self.y-1][self.x-2][0] == -1:
                    self.selection = -2
                    self.dying = 1
                    pyxel.stop(1)
                self.y -= 1
                pyxel.play(0,3)
                if self.y ==0:
                    self.selection = -2
                    self.dying = 4
                    pyxel.stop(1)
                else:
                    if (world[self.y-1][self.x-2][0] == 5):
                        break_thick = False
                

        if self.move == False and self.direction == "south" and master > 0 and self.dying ==0:
            if (world[self.y+1][self.x-2][0] == 5):
                self.move = True
                pyxel.play(0,6)
            else:
                if world[self.y+1][self.x-2][0] == -1:
                    self.selection = -2
                    self.dying = 1
                    pyxel.stop(1)
                self.y += 1
                pyxel.play(0,3)
                if self.y ==15:
                    self.selection = -2
                    self.dying = 4
                    pyxel.stop(1)
                else:
                    if (world[self.y+1][self.x-2][0] == 5):
                        break_thick = False
                

        if self.move == False and self.direction == "west" and master > 0 and self.dying ==0:
            if (world[self.y][self.x-3][0] == 5):
                self.move = True
                pyxel.play(0,6)
            else:
                if world[self.y][self.x-3][0] == -1:
                    self.selection = -2
                    self.dying = 1
                    pyxel.stop(1)
                self.x -= 1
                pyxel.play(0,3)
                if self.x ==2:
                    self.selection = -2
                    self.dying = 4
                    pyxel.stop(1)
                else:
                    if (world[self.y][self.x-3][0] == 5):
                        break_thick = False
                

        if self.move == False and self.direction == "east" and master > 0 and self.dying ==0:
            if (world[self.y][self.x-1][0] == 5):
                self.move = True
                pyxel.play(0,6)
            else:
                if world[self.y][self.x-1][0] == -1:
                    self.selection = -2
                    self.dying = 1
                    pyxel.stop(1)
                self.x += 1
                pyxel.play(0,3)
                if self.x ==17:
                    self.selection = -2
                    self.dying = 4
                    pyxel.stop(1)
                else:
                    if (world[self.y][self.x-1][0] == 5):
                        break_thick = False
                

        trilha(self.x-2, self.y)

        if master == -3:
            time.sleep(0.7)
            master = -2
            self.selection = -3 
            self.x = initial_x
            self.y = initial_y

        if world[self.y][self.x-2][0] == 9:
            self.move = True
            self.direction = None

        if (world[self.y][self.x-2][0] == -10) and difficulty==1:
            master = -3
            pyxel.stop(1)
        if master == -2 and last ==1:    
            master = -1000
            pyxel.stop(1)
        
        if self.x==initial_x and self.y==initial_y and difficulty==2:
            self.direction = None
            self.move = True
            x = 0
            for j in range(16):
                for i in range(16):
                    if world[j][i][0]==1:
                        x+=1
            if x == 0:
                self.selection = -3 
                self.x = 0
                self.y = 0
                master = -2
                pyxel.stop(1)

    def draw(self):
        global world, master_memory, master, counter, wave, cloud_marker, clouds
        counter += 1
        if counter % wave_speed == 0:
            wave = not wave
            counter = 0
        if difficulty == 1:
            if wave == True:
                pyxel.bltm(0,0,0,0,0,32,256)
                pyxel.bltm(288,0,0,64,0,32,256)
            elif wave == False:
                pyxel.bltm(0,0,0,32,0,32,256)
                pyxel.bltm(288,0,0,96,0,32,256)
            pyxel.bltm(16,0,0,128,0,16,256, 8)
            pyxel.bltm(288,0,0,144,0,16,256, 8)
        elif difficulty == 2:
            if wave == True:
                pyxel.bltm(0,0,0,192,0,32,256)
                pyxel.bltm(288,0,0,256,0,32,256)
            elif wave == False:
                pyxel.bltm(0,0,0,224,0,32,256)
                pyxel.bltm(288,0,0,288,0,32,256)
        for j in range(16):
            for i in range(16):
                match world[j][i][0]:
                    case 1:
                        if world[j][i][2] == -1:
                            pyxel.blt((i+2)*16, j*16, 0, 0, 80, 16, 16)
                        elif world[j][i][2] == -2:
                            pyxel.blt((i+2)*16, j*16, 0, 16, 80, 16, 16)
                        elif world[j][i][2] == -3:
                            pyxel.blt((i+2)*16, j*16, 0, 32, 80, 16, 16)
                        elif world[j][i][2] == -4:
                            pyxel.blt((i+2)*16, j*16, 0, 48, 80, 16, 16)
                        elif world[j][i][2] == -5:
                            pyxel.blt((i+2)*16, j*16, 0, 64, 80, 16, 16)
                    case 0:
                        pyxel.blt((i+2)*16, j*16, 0, 96, 0, 16, 16)
                    case -1:
                        if wave == True:
                            pyxel.blt((i+2)*16, j*16, 0, 32, 0, 16, 16)
                        elif wave == False:
                            pyxel.blt((i+2)*16, j*16, 0, 0, 48, 16, 16)
                    case 2:
                        if world[j][i][1] != 0:
                            pyxel.blt((i+2)*16, j*16, 0 ,144, 0, 16, 16)
                        else:
                            pyxel.blt((i+2)*16, j*16, 0, 0, 0, 16, 16)
                    case 5:
                        if world[j][i][2] == -1:
                            pyxel.blt((i+2)*16, j*16, 0, 0, 64, 16, 16)
                        elif world[j][i][2] == -2:
                            pyxel.blt((i+2)*16, j*16, 0, 16, 64, 16, 16)
                        elif world[j][i][2] == -3:
                            pyxel.blt((i+2)*16, j*16, 0, 32, 64, 16, 16)
                        elif world[j][i][2] == -4:
                            pyxel.blt((i+2)*16, j*16, 0, 48, 64, 16, 16)
                        elif world[j][i][2] == -5:
                            pyxel.blt((i+2)*16, j*16, 0, 64, 64, 16, 16)
                    case 7:
                        pyxel.blt((initial_x)*16, initial_y*16,0,16,32,16,16)
                    case 9 :
                        pyxel.blt((i+2)*16,j*16,0,144,16,16,16)
                    case -10:
                        pyxel.blt((i+2)*16, j*16, 0, 16, 0, 16, 16)
                        pyxel.blt((i+2)*16, j*16, 0, 48, 32, 16, 16,8)

        if self.dying == 1:
            pyxel.blt((self.x)*16, self.y*16, 0, 112, 0,16, 16,8)
        elif self.dying == 2:
            pyxel.blt((self.x)*16, self.y*16, 0, 128, 0,16, 16,8)
        elif self.dying == 4:
            pyxel.blt((self.x)*16, self.y*16, 0, 112, 16,16, 16,3)
        elif self.direction == None:
            pyxel.blt((self.x)*16, self.y*16, 0, 0, 16, 16, 16,8)
        elif self.direction == "south":
            pyxel.blt((self.x)*16, self.y*16, 0, 0, 16, 16, 16,8)
        elif self.direction == "north":
            pyxel.blt((self.x)*16, self.y*16, 0, 16, 16, 16, 16,8)
        elif self.direction == "east":
            pyxel.blt((self.x)*16, self.y*16, 0, 32, 16, 16, 16,8)
        elif self.direction == "west":
            pyxel.blt((self.x)*16, self.y*16, 0, 48, 16, 16, 16,8)

        match master:
            case 0:
                pass
            case -1: #tela de derrota
                for i in range(20):
                    pyxel.bltm(i*16,0,0,160,0,16,256)
                pyxel.rect(50, 200, 86, 25, 8)
                pyxel.blt(56, 205,1,192,32,16,16,3)
                pyxel.rect(186, 200, 86, 25, 3)
                pyxel.blt(189, 205,1,216,0,16,16,3)
                pyxel.text(76, 210, "Menu Inicial", 7)
                pyxel.text(207, 210, "Tentar Novamente", 7)
                if self.dying==3:
                    pyxel.blt(128, 82,1,0,64,64,52,5,0,1.3)
                    pyxel.text(122,160,"Voce morreu afogado!",7)
                elif self.dying == 5:
                    pyxel.blt(128,72,1,0,120,64,72,8,0,1.3)
                    pyxel.text(122,160,"Voce bateu a cabeca!",7)
                if self.selection == -1:
                    pyxel.rectb(49, 199, 88, 27, 7)
                    pyxel.rectb(50, 200, 86, 25, 1)
                elif self.selection == -2:
                    pyxel.rectb(185, 199, 88, 27, 7)
                    pyxel.rectb(186, 200, 86, 25, 1)
                pyxel.blt(132,40+int(math.cos(pyxel.frame_count/10)*7),1,64,0,56,16,3,0,2)
            case -2: #tela de vitória
                for i in range(20):
                    pyxel.bltm(i*16,0,0,176,0,16,256)
                pyxel.rect(16, 200, 86, 25, 8)
                pyxel.blt(22, 205,1,192,32,16,16,3)
                pyxel.rect(117, 200, 86, 25, 9)
                pyxel.blt(123, 205,1,216,0,16,16,3)
                pyxel.rect(218, 200, 86, 25, 3)
                pyxel.blt(224, 205,1,192,16,16,16,3)
                pyxel.text(42, 210, "Voltar ao Menu", 7)
                pyxel.text(143, 210, "Repetir Nivel", 7)
                pyxel.text(244, 210, "Proximo Nivel", 7)
                if self.selection == -1:
                    pyxel.rectb(15,199, 88, 27, 7)
                    pyxel.rectb(16, 200, 86, 25, 12)
                elif self.selection == -2:
                    pyxel.rectb(116, 199, 88, 27, 7)
                    pyxel.rectb(117, 200, 86, 25, 12) 
                elif self.selection == -3:
                    pyxel.rectb(217, 199, 88, 27, 7)
                    pyxel.rectb(218, 200, 86, 25, 12)
                pyxel.blt(123, 82,1,0,0,64,64,5,0,1.3)
                pyxel.blt(132,40,1,64,16,64,16,2,0,2+((math.cos(pyxel.frame_count/10))/6))
            case -3: #teela de transição de nivel
                pyxel.blt((self.x*16), (self.y*16),0,16,0,16,16)
                pyxel.blt((self.x*16), (self.y*16),0,64,32,16,16,8)
                pyxel.blt((self.x*16), (self.y*16)-11,0,80,32,16,16,8,-45)
            case -1000: #tela de vitória final
                pyxel.rect(0,0,320,256, 1)
                pyxel.text(145, 150, "Parabens!", 7)
                pyxel.text(125, 160, "Você terminou o modo!", 7)
                pyxel.rect(50, 200, 86, 25, 8)
                pyxel.blt(56, 205,1,232,0,16,16,3)
                pyxel.rect(186, 200, 86, 25, 3)
                pyxel.blt(189, 205,1,192,32,16,16,3)
                pyxel.text(76, 210, "Sair do jogo", 7)
                pyxel.text(207, 210, "Voltar ao menu", 7)
                if self.selection == -1:
                    pyxel.rectb(49, 199, 88, 27, 7)
                    pyxel.rectb(50, 200, 86, 25, 1)
                elif self.selection == -2:
                    pyxel.rectb(185, 199, 88, 27, 7)
                    pyxel.rectb(186, 200, 86, 25, 1) 
            case -998: #transição para o menu inicial
                pyxel.cls(0)
                
            case -999: #menu inicial
                pyxel.cls(6)

                #gera nuvens aleatóriamente e decide se vão passar pela frente ou atrás da montanha
                if pyxel.frame_count - cloud_marker > 55 and pyxel.frame_count%2==0: 
                    x = random.randint(1,50)
                    if x == 1:
                        clouds.append(Cloud(random.randint(1,5), -48, random.randint(20, 80), random.randint(1,3)))
                        cloud_marker = pyxel.frame_count
                for i in clouds:
                    if i.back!=1:    
                        i.move()
                    if i.pos_x > 320:
                        clouds.remove(i)
                pyxel.bltm(0,0,1,0,0,32,256,8)
                pyxel.bltm(288,0,1,32,0,32,256,8)
                pyxel.blt(32,0,2,0,0,256,256, 8)
                pyxel.rect(50, 200, 86, 25, 8)
                pyxel.blt(56, 205,1,232,0,16,16,3)
                pyxel.rect(186, 200, 86, 25, 3)
                pyxel.blt(192, 205,1,128,16,16,16,3)
                pyxel.rect(50, 160, 86, 25, 12)
                pyxel.blt(56, 165,1,176,16,16,16,3)
                pyxel.rect(186, 160, 86, 25, 5)
                pyxel.blt(192, 165,1,160,16,16,16,3)
                #printa as nuvens que passam pela frente da montanha
                for i in clouds:
                    if i.back==1:    
                        i.move()
                pyxel.blt(65,40+int(math.cos(pyxel.frame_count/10)*6),1,0,192,32,32,8,0,2.3)
                pyxel.blt(45,70+int(math.cos(pyxel.frame_count/10)*6),1,0,224,8,16,8,0,(math.cos(pyxel.frame_count/5)+2)*0.7+1)
                pyxel.blt(110,30+int(math.cos(pyxel.frame_count/10)*6),1,9,224,5,8,8,0,(math.sin(pyxel.frame_count/9)+2)*0.7+1)
                pyxel.text(78, 210, "Sair do Jogo", 7)
                pyxel.text(212, 210, "Instrucoes", 7)
                pyxel.text(78, 170, "Modo Facil", 7)
                pyxel.text(212, 170, "Modo Dificil", 7)
                if self.selection ==1:
                    pyxel.rectb(49, 159, 88, 27, 1)
                    pyxel.rectb(50, 160, 86, 25, 7)
                elif self.selection ==10:
                    pyxel.rectb(185, 159, 88, 27, 1)
                    pyxel.rectb(186, 160, 86, 25, 7)
                elif self.selection == 2:
                    pyxel.rectb(49, 199, 88, 27, 1)
                    pyxel.rectb(50, 200, 86, 25, 7)
                elif self.selection == 20:
                    pyxel.rectb(185, 199, 88, 27, 1)
                    pyxel.rectb(186, 200, 86, 25, 7) 
    
            case -997: #tela instrucoes
                #tela de como jogar
                if self.selection == -1: 
                    pyxel.cls(1)
                    pyxel.text(140, 20, "COMO JOGAR",7)
                    pyxel.text(40, 50, "CONTROLES:", 7)
                    pyxel.blt(152, 75, 0, 0, 16, 16, 16, 8)
                    pyxel.text(150, 65, "W / ^", 7) 
                    pyxel.text(150, 95, "S / v", 7)
                    pyxel.text(124, 80, "A / <", 7) 
                    pyxel.text(176, 80, "D / >", 7)
                    pyxel.text(40, 140, "OBJETIVO:", 7)
                    pyxel.text(40, 155, "- Modo Facil: Chegue ao peixe.", 7)
                    pyxel.text(40, 165, "- Modo Dificil: Pise em todo o gelo e volte para o inicio", 7)
                    pyxel.text(130, 230, "Pagina 1 de 2  >", 7)
                    pyxel.text(86, 240, "Pressione ESPACO ou RETURN para voltar", 7)
                #tela dos blocos
                elif self.selection == -2:
                    pyxel.cls(3)
                    pyxel.text(146, 20, "BLOCOS",7)  
                    pyxel.blt(50, 30, 0, 16, 0, 16, 16)
                    pyxel.text(74, 34, "- Gelo Normal: Deslize sobre ele,vira agua.", 7)
                    pyxel.blt(50, 60, 0, 0, 0, 16, 16)
                    pyxel.text(74, 64, "- Gelo grosso: Vira gelo normal ao pisar.", 7)
                    pyxel.blt(50, 90, 0, 160, 0, 16, 16)
                    pyxel.text(74, 94, "- gelo coberto: nao vira agua e para o penguim.", 7)
                    pyxel.blt(50, 120, 0, 0, 64, 16, 16)
                    pyxel.text(74, 124, "- Parede: Bloqueia seu movimento.", 7)
                    pyxel.blt(50, 150, 0, 32, 0, 16, 16)
                    pyxel.text(74, 154, "- Agua:afogamento!, fim de jogo.", 7)
                    pyxel.blt(50, 180, 0, 48, 32, 16, 16,8)
                    pyxel.text(74, 184, "- peixe: Objetivo do modo facil.", 7)
                    pyxel.blt(50, 210, 0, 16, 32, 16, 16)
                    pyxel.text(74, 214, "- Inicio (Dificil): Volte aqui para vencer.", 7)
                    pyxel.text(126, 230, "<  Pagina 2 de 2", 7)
                    pyxel.text(86, 240, "Pressione ESPACO ou RETURN para voltar", 7)
Jogo()