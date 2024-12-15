import svg
import math

class dotpattern ():
    def __init__(self, width, height):
        super().__init__()
        self.page_width = width
        self.page_height = height
        print ("dots pattern Width=", width, " Height=", height)

    def build (self, step):
        print ("dots pattern step=", step)
        elements: list[svg.Element] = []
        
        y = 0
        
        while y < self.page_height:
            x = 0
            while x < self.page_width:
                elements.append(svg.Circle(
                    cx=x,cy=y,r=0.1,
                    stroke="#000000",
                    stroke_width=0.5,
                    fill="none"
                    
                ))
                x += step
            y += step

        
        return elements

