import svg

class vlinepattern ():
    def __init__(self, width, height):
        super().__init__()
        self.page_width = width
        self.page_height = height
        print ("vertical line pattern Width=", width, " Height=", height)

    def build (self, step):
        print ("vertical line pattern step=", step)
        elements: list[svg.Element] = []
        path = []
        x = 0
        while x < self.page_width:
            path.append (svg.M(x, 0))
            path.append (svg.L(x,self.page_height))
            x += step

        elements.append(svg.Path(
                stroke="#000000",
                stroke_width=0.5,
                stroke_linecap="round",
                fill="none",
                d=path,
            ))
        return elements

