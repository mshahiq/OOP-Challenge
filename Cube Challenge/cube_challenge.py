class CubeIntersection:

    def __init__(self,cubeA_size,cubeA_x,cubeA_y,cubeA_z,cubeB_size,cubeB_x,cubeB_y,cubeB_z) -> None:
        self.cubeA_size = cubeA_size
        self.cubeA_x = cubeA_x
        self.cubeA_y = cubeA_y
        self.cubeA_z = cubeA_z
        self.cubeB_size = cubeB_size
        self.cubeB_x = cubeB_x
        self.cubeB_y = cubeB_y
        self.cubeB_z = cubeB_z

    def intersection_of_cubeA_and_cubeB(self):
            Ax1 = self.cubeA_y - (self.cubeA_size/2)                                                         
            Ax3 = self.cubeA_y - (self.cubeA_size/2)
            Ax5 = self.cubeA_y - (self.cubeA_size/2)
            Ax7 = self.cubeA_y - (self.cubeA_size/2)

            Ay1 = self.cubeA_x - (self.cubeA_size/2)
            Ay2 = self.cubeA_x - (self.cubeA_size/2)
            Ay5 = self.cubeA_x - (self.cubeA_size/2)
            Ay6 = self.cubeA_x - (self.cubeA_size/2)

            Ax2 = self.cubeA_y + (self.cubeA_size/2)
            Ax4 = self.cubeA_y + (self.cubeA_size/2)
            Ax6 = self.cubeA_y + (self.cubeA_size/2)
            Ax8 = self.cubeA_y + (self.cubeA_size/2)

            Ay3 = self.cubeA_x + (self.cubeA_size/2)
            Ay4 = self.cubeA_x + (self.cubeA_size/2)
            Ay7 = self.cubeA_x + (self.cubeA_size/2)
            Ay8 = self.cubeA_x + (self.cubeA_size/2)
            
            Az1 = (self.cubeA_z/2) - (self.cubeA_size/2)
            Az2 = (self.cubeA_z/2) - (self.cubeA_size/2)
            Az3 = (self.cubeA_z/2) - (self.cubeA_size/2)
            Az4 = (self.cubeA_z/2) - (self.cubeA_size/2)

            Az5 = (self.cubeA_z/2) + (self.cubeA_size/2)
            Az6 = (self.cubeA_z/2) + (self.cubeA_size/2)
            Az7 = (self.cubeA_z/2) + (self.cubeA_size/2)
            Az8 = (self.cubeA_z/2) + (self.cubeA_size/2)            

            Bx1 = self.cubeB_y - (self.cubeB_size/2)
            Bx3 = self.cubeB_y - (self.cubeB_size/2)
            Bx5 = self.cubeB_y - (self.cubeB_size/2)
            Bx7 = self.cubeB_y - (self.cubeB_size/2)

            By1 = self.cubeB_x - (self.cubeB_size/2)
            By2 = self.cubeB_x - (self.cubeB_size/2)
            By5 = self.cubeB_x - (self.cubeB_size/2)
            By6 = self.cubeB_x - (self.cubeB_size/2)

            Bx2 = self.cubeB_y + (self.cubeB_size/2)
            Bx4 = self.cubeB_y + (self.cubeB_size/2)
            Bx6 = self.cubeB_y + (self.cubeB_size/2)
            Bx8 = self.cubeB_y + (self.cubeB_size/2)

            By3 = self.cubeB_x + (self.cubeB_size/2)
            By4 = self.cubeB_x + (self.cubeB_size/2)
            By7 = self.cubeB_x + (self.cubeB_size/2)
            By8 = self.cubeB_x + (self.cubeB_size/2)

            Bz1 = (self.cubeB_z/2) - (self.cubeB_size/2)
            Bz2 = (self.cubeB_z/2) - (self.cubeB_size/2)
            Bz3 = (self.cubeB_z/2) - (self.cubeB_size/2)
            Bz4 = (self.cubeB_z/2) - (self.cubeB_size/2)

            Bz5 = (self.cubeB_z/2) + (self.cubeB_size/2)
            Bz6 = (self.cubeB_z/2) + (self.cubeB_size/2)
            Bz7 = (self.cubeB_z/2) + (self.cubeB_size/2)
            Bz8 = (self.cubeB_z/2) + (self.cubeB_size/2)

            if (Ax4>Bx1 and Ay4>By1 and Az4>Bz1):
                volume = ((Bx1-Ax4)*(By1-Ay4)*(Bz1-Az4))
                volume_round = (round(volume))
                volume_final = abs(volume_round) 

                return True, volume_final

            elif (Bx4>Ax1 and By4>Ay1 and Bz4>Az1):
                volume = ((Ax1-Bx4)*(Ay1-By4)*(Az1-Bz4))
                volume_round = (round(volume))
                volume_final = volume_round * (-1)

                return True, volume_final

            else:
                volume = 0
                return False, volume

intersection = CubeIntersection(5,10,10,0,12,10,4,4)

print(intersection.intersection_of_cubeA_and_cubeB())