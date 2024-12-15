import svg

class hlinepattern ():
    def __init__(self, width, height):
        super().__init__()
        self.page_width = width
        self.page_height = height
        print ("horizontal line pattern Width=", width, " Height=", height)

    def build (self, step):
        print ("horizontal line pattern step=", step)
        elements: list[svg.Element] = []
        path = []
        y = 0
        while y < self.page_height:
            path.append (svg.M(0, y))
            path.append (svg.L(self.page_width, y))
            y += step

        elements.append(svg.Path(
                stroke="#000000",
                stroke_width=0.5,
                stroke_linecap="round",
                fill="none",
                d=path,
            ))
        return elements

