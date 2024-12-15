import svg


STROKE_LEN = 10
GAP = 10
WIDTH = 210
HEIGHT = 290

SHIFT = int(STROKE_LEN / 2)
STEP = 10

class squarepattern ():
    def __init__(self, width, height):
        super().__init__()
        self.page_width = width
        self.page_height = height
        print ("square pattern Width=", width, " Height=", height)

    def build (self, step):
        print ("square pattern step=", step)
        elements: list[svg.Element] = []
        for y in range(0, self.page_height, int(step)):
        
            dy = (step*2)//3
            for x in range(0,self.page_width, int(step)):
                path = []
                path.append (svg.M(x, y))
                path.append (svg.L(x, y+dy))
                path.append (svg.L(x +dy, y+dy))
                path.append (svg.L(x +dy, y))
                path.append (svg.L(x , y))
                path.append (svg.M(x+dy//2, y))
                path.append (svg.L(x+dy//2, y+dy))
                path.append (svg.M(x, y+dy//2))
                path.append (svg.L(x+dy, y+dy//2))

                elements.append(svg.Path(
                            stroke="#000000",
                            stroke_width=0.5,
                            stroke_linecap="round",
                            fill="none",
                            d=path,
                        ))

        
        return elements




