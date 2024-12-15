import svg
import math

class dotpatternsin ():
    def __init__(self, width, height):
        super().__init__()
        self.page_width = width
        self.page_height = height
        print ("dots pattern sinWidth=", width, " Height=", height)

    def build (self, step):
        elements: list[svg.Element] = []
        stepx = 2.6
        f =  3.1415927 / (self.page_width / 16) 
        y = 0
        
        while y < self.page_height:
            x = 0
            
            while x < self.page_width:
                elements.append(svg.Circle(
                    
                    cx=x,cy=y + math.sin(x * f) * (step * 0.75) ,r=0.1,
                    stroke="#000000",
                    stroke_width=0.5,
                    fill="none"
                    
                ))
                x += stepx
            y += step

        
        return elements

