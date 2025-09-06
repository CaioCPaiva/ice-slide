import pyxel
import copy
import ast
import time
base_array = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

world_array = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

#gelo = 1
#gelo grosso = 2
#água = -1
#neve = 5
#bloco inquebrável = 9

world_list = []
class maker:
    def __init__(self):
        pyxel.init(500, 300, title="Ice Slide - Level Maker",fps = 60)
        pyxel.load("assets_ice_slide.pyxres")
        self.mouse_x=0
        self.mouse_y = 0
        self.selection  = 0
        self.initial_x = -10
        self.initial_y = -10
        self.difficulty = 1
        self.level = -1
        pyxel.run(self.update, self.draw)
    
    def remake_world(self):
        global world_array
        world_array = []
        if self.difficulty==1:
            with open("map_lists.txt", "r") as f:
                lines = f.readlines()
                content = ast.literal_eval(lines[self.level-1])
                
            for y in range(16):
                temp_array = []            
                for x in range(16):
                    valor = 1 
                    for i in range(len(content[1])):
                        if content[1][i][0] == x and content[1][i][1] == y:
                            valor = content[1][i][2]
                            break  
                    temp_array.append(valor)
                world_array.append(temp_array)

            self.initial_x = (content[0][0]-2)
            self.initial_y = content[0][1]
        elif self.difficulty == 2:
            with open("hard_map_lists.txt", "r") as f:
                lines = f.readlines()
                content = ast.literal_eval(lines[self.level-1])
                
            for y in range(16):
                temp_array = []            
                for x in range(16):
                    valor = 1 
                    for i in range(len(content[1])):
                        if content[1][i][0] == x and content[1][i][1] == y:
                            valor = content[1][i][2]
                            break  
                    temp_array.append(valor)
                world_array.append(temp_array)

            self.initial_x = (content[0][0])
            self.initial_y = content[0][1]

    def update(self):
        global world_array, base_array, world_list
        self.mouse_x = pyxel.mouse_x
        self.mouse_y = pyxel.mouse_y

        if  (self.mouse_x>=300 and self.mouse_x<=360) and (self.mouse_y>=250 and self.mouse_y<=270) and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)==True:
            world_array = copy.deepcopy(base_array)
            self.initial_x = -10
            self.initial_y = -10

        if (self.mouse_x>=300 and self.mouse_x<=320) and (self.mouse_y>=60 and self.mouse_y<=80) and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)==True:
            self.selection = 1
        if (self.mouse_x>=325 and self.mouse_x<=345) and (self.mouse_y>=60 and self.mouse_y<=80) and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)==True:
            self.selection = 2
        if (self.mouse_x>=350 and self.mouse_x<=370) and (self.mouse_y>=60 and self.mouse_y<=80) and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)==True:
            self.selection = 3
        if (self.mouse_x>=375 and self.mouse_x<=395) and (self.mouse_y>=60 and self.mouse_y<=80) and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)==True:
            self.selection = 4
        if (self.mouse_x>=400 and self.mouse_x<=420) and (self.mouse_y>=60 and self.mouse_y<=80) and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)==True:
            self.selection = 5
        if (self.mouse_x>=300 and self.mouse_x<=360) and (self.mouse_y>=110 and self.mouse_y<=130) and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)==True:
            self.selection = 6
        if (self.mouse_x>=300 and self.mouse_x<=320) and (self.mouse_y>=85 and self.mouse_y<=105) and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)==True:
            self.selection = 7
        
        if (self.mouse_x>=20 and self.mouse_x<=275) and (self.mouse_y>=20 and self.mouse_y<=275) and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT)==True:
            match self.selection:
                case 1:
                    world_array[(self.mouse_y-20)//16][(self.mouse_x-20)//16] = 1
                case 2:
                    world_array[(self.mouse_y-20)//16][(self.mouse_x-20)//16] = 2
                case 3:
                    world_array[(self.mouse_y-20)//16][(self.mouse_x-20)//16] = -1
                case 4:
                    world_array[(self.mouse_y-20)//16][(self.mouse_x-20)//16] = 5
                case 5:
                    world_array[(self.mouse_y-20)//16][(self.mouse_x-20)//16] = -10
                case 7:
                    world_array[(self.mouse_y-20)//16][(self.mouse_x-20)//16] = 9

        if self.selection == 6 and (self.mouse_x>=20 and self.mouse_x<=275) and (self.mouse_y>=20 and self.mouse_y<=275) and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)==True:
            self.initial_x = (self.mouse_x-20)//16
            self.initial_y = (self.mouse_y-20)//16
            self.selection = 0
        
        if (self.mouse_x>=440 and self.mouse_x<=480) and (self.mouse_y>=60 and self.mouse_y<=80) and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)==True:
            self.level = -1
            world_array = copy.deepcopy(base_array)
            self.initial_x = -10
            self.initial_y = -10
            if self.difficulty ==1:
                self.difficulty = 2
            else:
                self.difficulty = 1
            
        if (self.mouse_x>=300 and self.mouse_x<=320) and (self.mouse_y>=20 and self.mouse_y<=40) and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT)==True:
            if self.level >0:
                self.level -=1
                self.remake_world()
            if self.level == 0:
                self.level = -1
                world_array = copy.deepcopy(base_array)
                self.initial_x = -10
                self.initial_y = -10
            time.sleep(0.2)
        if (self.mouse_x>=460 and self.mouse_x<=480) and (self.mouse_y>=20 and self.mouse_y <=40) and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT)==True:
            if self.difficulty == 1:
                with open("map_lists.txt", "r") as file:
                    count = len(file.readlines())
            elif self.difficulty == 2:
                with open("hard_map_lists.txt", "r") as file:
                    count = len(file.readlines())
            if (self.level) < count and self.level >=0:
                self.level +=1
                self.remake_world()
            elif self.level == -1:
                self.level = 1
                self.remake_world()
            time.sleep(0.2)


        if (self.mouse_x>=420 and self.mouse_x<=480) and (self.mouse_y>=250 and self.mouse_y<=270) and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)==True:
            if self.initial_x>0 and self.initial_y>0:
                if self.level == -1:    
                    if self.difficulty==1:
                        x = 0
                        for j in range(16):
                            for i in range(16):
                                if world_array[j][i]==-10:
                                    x+=1
                        if x!=1:
                            print("por favor defina um e apenas um ponto final")
                        else:

                            temp_list=[]
                            world_list.append([self.initial_x,self.initial_y])

                            for y in range(16):
                                for x in range(16):
                                    if world_array[y][x] != 1:
                                        temp_list.append([x, y, world_array[y][x]])

                            world_list.append(temp_list)
                            world_list.append(1)

                            with open("map_lists.txt", "r") as f:
                                lines = f.readlines()
                                previous_level = ast.literal_eval(lines[-1])
                            previous_level.pop(-1)
                            previous_level.append(0)
                            lines = lines[:-1] 

                            with open("map_lists.txt", "w") as f:
                                f.writelines(lines)

                            end_world = str(world_list)

                            with open("map_lists.txt", "a") as f:
                                f.write(str(previous_level)+"\n")
                                f.write(end_world)

                            print("level exportado!")
                            world_array = copy.deepcopy(base_array)
                            self.initial_x = -10
                            self.initial_y = -10
                    elif self.difficulty==2:
                        temp_list=[]
                        world_list.append([self.initial_x,self.initial_y])

                        for y in range(16):
                            for x in range(16):
                                if world_array[y][x] != 1:
                                    temp_list.append([x, y, world_array[y][x]])

                        world_list.append(temp_list)
                        world_list.append(1)

                        with open("hard_map_lists.txt", "r") as f:
                            lines = f.readlines()
                            previous_level = ast.literal_eval(lines[-1])
                        previous_level.pop(-1)
                        previous_level.append(0)
                        lines = lines[:-1] 

                        with open("hard_map_lists.txt", "w") as f:
                            f.writelines(lines)

                        end_world = str(world_list)

                        with open("hard_map_lists.txt", "a") as f:
                            f.write(str(previous_level)+"\n")
                            f.write(end_world)
                        print("level exportado!")
                        world_array = copy.deepcopy(base_array)
                        self.initial_x = -10
                        self.initial_y = -10
                else:
                    if self.difficulty == 1:
                        with open("map_lists.txt", "r") as f:
                            linhas = f.readlines()
                        remade_world = []
                        temp_list = []
                        remade_world.append([self.initial_x, self.initial_y])
                        for y in range(16):
                                for x in range(16):
                                    if world_array[y][x] != 1:
                                        temp_list.append([x, y, world_array[y][x]])
                        remade_world.append(temp_list)
                        remade_world.append(0)
                        linhas[(self.level-1)] = str(remade_world)
                        linhas = [linha.rstrip("\n") for linha in linhas]
                        with open("map_lists.txt", "w") as f:
                            f.write("\n".join(linhas))

                    elif self.difficulty == 2:
                        with open("hard_map_lists.txt", "r") as f:
                            linhas = f.readlines()
                        remade_world = []
                        temp_list = []
                        remade_world.append([self.initial_x, self.initial_y])
                        for y in range(16):
                                for x in range(16):
                                    if world_array[y][x] != 1:
                                        temp_list.append([x, y, world_array[y][x]])
                        remade_world.append(temp_list)
                        remade_world.append(0)
                        linhas[(self.level-1)] = str(remade_world)
                        linhas = [linha.rstrip("\n") for linha in linhas]
                        with open("hard_map_lists.txt", "w") as f:
                            f.write("\n".join(linhas))

            else:
                print("Defina um ponto inicial")
        
    def draw(self):
        pyxel.cls(7)
        for j in range(16):
            for i in range(16):
                match world_array[j][i]:
                    case 1:
                        pyxel.blt(20+(i*16),20+(j*16),0,16,0,16,16)
                    case 2:
                        pyxel.blt(20+(i*16),20+(j*16),0,0,0,16,16)
                    case -1:
                        pyxel.blt(20+(i*16),20+(j*16),0,32,0,16,16)
                    case 5:
                        pyxel.blt(20+(i*16),20+(j*16),0,0,64,16,16)
                    case -10:
                        pyxel.blt(20+(i*16),20+(j*16),0,16,0,16,16)
                        pyxel.blt(20+(i*16),20+(j*16),0,48,32,16,16, 8)
                    case 9:
                        pyxel.blt(20+(i*16),20+(j*16),0,144,16,16,16)
        if self.difficulty == 1:
            pyxel.rect(442,62,16,16,3)
            pyxel.text(448,67, "F", 7)
        elif self.difficulty == 2:
            pyxel.rect(462,62,16,16,8)
            pyxel.text(468,67, "D", 7)
            pyxel.blt(((self.initial_x)*16)+20,(self.initial_y*16)+20,0,16,32,16,16)
        for i in range(17):
            pyxel.rect(20+(i*16),20,1,256,1)
            pyxel.rect(20,20+(i*16),256,1,1)
        pyxel.rect(((self.initial_x)*16)+23, (self.initial_y*16)+23,11,11,3)

        pyxel.rectb(300,60,20,20,1) #gelo
        pyxel.blt(302,62,0,16,0,16,16)
        pyxel.rectb(325,60,20,20,1) #gelo grosso
        pyxel.blt(327,62,0,0,0,16,16)
        pyxel.rectb(350,60,20,20,1) #agua
        pyxel.blt(352,62,0,32,0,16,16)
        pyxel.rectb(375,60,20,20,1) #neve
        pyxel.blt(377,62,0,0,64,16,16)
        pyxel.rectb(400,60,20,20,1) #final point
        pyxel.blt(402,62,0,48,32,16,16, 8)
        pyxel.rectb(300,85,20,20,1) #bloco inquebrável
        pyxel.blt(302,87,0,144,16,16,16)
        pyxel.rect(300, 110, 60, 20,3) #setar posição inicial
        pyxel.text(305, 118, "Set init pos", 7)
        pyxel.rect(300, 250, 60, 20,9) #Resetar level
        pyxel.text(305, 258, "Reset Level", 7)
        pyxel.rect(420, 250, 60, 20,2) #Exportar level
        pyxel.text(430, 258, "Save Level", 7)

        pyxel.text(440,53,"Difficulty",1)
        pyxel.rectb(440,60,40,20,1)
        
        pyxel.rectb(300, 20, 20,20,1) #seleção de levels
        pyxel.rectb(460, 20, 20,20,1)
        pyxel.rect(325, 20, 130,20,1)
        pyxel.tri(303, 30, 315,24,315,36,1)
        pyxel.tri(476, 30, 464,24,464,36,1)
        
        if self.level == -1:
            pyxel.text(343, 28, "New level", 7)
        else:
            pyxel.text(343, 28, f"Level {self.level}", 7)

        match self.selection:
            case 1:
                pyxel.rectb(300,60,20,20,8)
            case 2:
                pyxel.rectb(325,60,20,20,8)
            case 3:
                pyxel.rectb(350,60,20,20,8)
            case 4:
                pyxel.rectb(375, 60, 20,20,8)
            case 5:
                pyxel.rectb(400,60,20,20,8)
            case 6:
                pyxel.rectb(299,109,62,22,8)
                pyxel.rectb(300,110,60,20,8)
            case 7:
                pyxel.rectb(300,85,20,20,8)
        
        


        
        pyxel.blt(self.mouse_x, self.mouse_y,0,128,16,8,8,3)
maker()