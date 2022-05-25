import math

class simulationCal:
    def __init__(self,x_axis,springConst,springAmount,g,mass):
        self.x_axis = x_axis
        # self.y_axis = y_axis
        self.springConst = springConst
        self.springAmount = springAmount
        self.initialVelo = 0
        self.g = g
        self.mass = mass
        self.length_x = 0
    #calculation: projectile part
    def projectileCal(self):
        #if self.y_axis/self.x_axis > math.cos(60 * (math.pi/180))
        self.initialVelo = math.sqrt((self.g * (self.x_axis ** 2)) / (2 * (math.cos(60 * (math.pi/180)) ** 2) * (self.x_axis * math.tan(60 * (math.pi/180)) - 0.2)))
        # self.initialVelo = math.sqrt(self.initialVelo)
        #print(initialVelo)
        
        return '%.3f'%float(self.initialVelo)

    def timeCal(self):
        self.time = self.x_axis / (self.initialVelo * math.cos(60 * (math.pi/180)))
        return '%.3f'%float(self.time)

    #calculation: spring part
    def springCal(self):
        # length_x=((2 * self.mass * self.g * (math.sin(60 * (math.pi/180)))) + ((4 * (self.mass ** 2)*(self.g ** 2)*((math.sin(60*(math.pi/180))) ** 2))+(4 * self.springAmount * self.springConst * self.mass * (self.initialVelo ** 2))) ** 0.5) / (2 * self.springAmount * self.springConst)
        self.length_x=((2 * (self.mass/1000) * self.g * (math.sin(60 * (math.pi/180)))) + ((4 * ((self.mass/1000) ** 2) * (self.g ** 2) * ((math.sin(60 * (math.pi/180))) ** 2))+(4 * self.springAmount * self.springConst * (self.mass/1000) * (self.initialVelo ** 2))) ** 0.5)/(2 * self.springAmount * self.springConst)

        return '%.3f'%float(self.length_x)
    
    # length_x=((2*self.mass*self.g*(math.sin(60*(math.pi/180))))+((4*(self.mass**2)*(self.g**2)*((math.sin(60*(math.pi/180)))**2))+(4*self.springAmount*self.springConst*self.mass*(self.initialVelo**2)))**0.5)/(2*self.springAmount*self.springConst)

    
# #input from inputBox  
# x_axis = 2.585
# y_axis = 0.2
# springConst = 803.6
# springAmount = 2
# #constant
# g = 9.81
# mass = 0.187

# x = simulationCal(x_axis, y_axis, springConst, springAmount, g, mass)
# c = x.projectileCal()
# v = x.springCal()
# print('%.3f'%c,'%.3f'%v)


# #find u

# initialVelo = (9.81 * (x_axis ** 2)) / (2 * (math.cos(60 * (math.pi/180)) ** 2) * (x_axis * math.tan(60 * (math.pi/180)) - y_axis))
# initialVelo = math.sqrt(initialVelo)

# #find t

# time = abs(x_axis / (initialVelo * math.cos(60* (math.pi/180))))

# print(initialVelo)
# print(time)
#print(time)
#decimal format "{0:.2f}".format(time)

#calculation: spring part
