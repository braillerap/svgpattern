import svg
import math

class dotpatternsin2 ():
    def __init__(self, width, height):
        super().__init__()
        self.page_width = width
        self.page_height = height
        print ("dots pattern sin Width=", width, " Height=", height)

    def build (self, step):
        print ("dots pattern sin step=", step)
        elements: list[svg.Element] = []
        path = []
        stepx = 2
        f =  3.1415927 / (self.page_width / 16) 
        y = 0
        
        while y < self.page_height:
            x = 0
            path = []
            path.append (svg.M(0, y))
            while x < self.page_width:
                path.append (svg.L(x, y + math.sin(x * f) * (step * 0.75)))
                x += stepx

            elements.append(svg.Path(
                stroke="#000000",
                stroke_width=0.5,
                stroke_linecap="round",
                fill="none",
                d=path,
            ))
            y += step
            
       
        
        return elements

