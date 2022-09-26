
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

class Stream:
    def __init__(self):
        self.begin = []
        
    def close(self):
        self.begin = []
        
    def liveFeed(self,x,y,color="black",time=0.2):
        if self.begin == []:
            self.begin = [x,y]
        else :
            x1,y1 = self.begin
            x2,y2 = x,y
            plt.plot((x1,x2),(y1,y2),color=color)
            plt.pause(time)
            self.begin = [x,y]
            
    def makeFeed_XY(self,x_data,y_data,color="black",time=0.2):
        new_x = []
        new_y = []
        for x in range(1,len(x_data)):
            i = [x_data[x-1],x_data[x]]
            new_x.append(i)
        for y in range(1,len(y_data)):
            i = [y_data[y-1],y_data[y]]
            new_y.append(i)
        for iteration in range(len(new_x)):
            plt.plot(new_x[iteration],new_y[iteration],color=color)
            plt.pause(time)
            
    def makeFeed_DFC(self,data,color="black",time=0.2):
        x_data = np.arange(data.index.stop)
        y_data = data
        self.makeFeed_XY(x_data,y_data,color=color,time=time)
        
    def makeMultiFeed_XY(self,x_data,func_data,color=[],time=0.2):
        if len(color) == 0 :
            color = ["black" for i in range(len(x_data))]
        for i in range(1,len(x_data)):
            n = 0
            for func in func_data:
                plt.plot((x_data[i-1],x_data[i]),(func[i-1],func[i]),color=color[n])
                n += 1
            plt.pause(time)



