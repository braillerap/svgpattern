import svg

class dotpatternalt ():
    def __init__(self, width, height):
        super().__init__()
        self.page_width = width
        self.page_height = height
        print ("alternate dot pattern width=", width, " Height=", height)

    def build (self, step):
        print ("alternate dot pattern step=", step)
        elements: list[svg.Element] = []
        i = 0
        y = 0
        while y < self.page_height:
            if i % 2 == 1:
                x = 0
            else:
                x = step / 2
            while x < self.page_width:
                elements.append(svg.Circle(
                    cx=x,cy=y,r=0.1,
                    stroke="#000000",
                    stroke_width=0.5,
                    fill="none"
                    
                ))
                x += step
            y += step
            i += 1

        
        return elements

