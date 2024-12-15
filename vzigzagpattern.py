import svg

class vzigzagpattern ():
    def __init__(self, width, height):
        #super().__init__(self)
        self.page_width = width
        self.page_height = height
        

    def build (self, step):
        print ("zigzag pattern step=", step)
        elements: list[svg.Element] = []
        path = []
        x = 0
        while x < self.page_width:
            path.append (svg.M(x, 0))
            y = 0
            dx = step / 2
            while y < self.page_height:
                path.append (svg.L(x + dx,y))
                y += step
                dx = -dx
            x += step

        elements.append(svg.Path(
                stroke="#000000",
                stroke_width=0.5,
                stroke_linecap="round",
                fill="none",
                d=path,
            ))
        return elements

