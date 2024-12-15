import svg
import math

class dotpatternvsin ():
    def __init__(self, width, height):
        super().__init__()
        self.page_width = width
        self.page_height = height
        print ("dots pattern vertical sin Width=", width, " Height=", height)

    def build (self, step):
        print ("dots pattern vertical sin step=", step)
        elements: list[svg.Element] = []
        path = []
        stepy = 2
        f =  3.1415927 / (self.page_width / 16) 
        x = 0
        
        
        while x < self.page_width:            
            y = 0
            path = []
            path.append (svg.M(x, 0))
            while y < self.page_height:    
                path.append (svg.L(x + math.sin(y * f) * (step * 0.75), y ))
                y += stepy

            elements.append(svg.Path(
                stroke="#000000",
                stroke_width=0.5,
                stroke_linecap="round",
                fill="none",
                d=path,
            ))
            x += step
            
       
        
        return elements

