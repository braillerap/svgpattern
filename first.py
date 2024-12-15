import svg


STROKE_LEN = 10
GAP = 10
WIDTH = 210
HEIGHT = 290

SHIFT = int(STROKE_LEN / 2)
STEP = 10


def draw() -> svg.SVG:
    elements: list[svg.Element] = []
    path = []
    for y in range(0, HEIGHT, STEP):
        path.append (svg.M(0, y))
        dy = 8
        for x in range(0,WIDTH, STEP):
            path.append (svg.L(x, y+dy))
            dy = - dy

    elements.append(svg.Path(
                stroke="#ff0000",
                stroke_width=0.5,
                stroke_linecap="round",
                fill="none",
                d=path,
            ))
    return svg.SVG(
        viewBox=svg.ViewBoxSpec(0, 0, WIDTH, HEIGHT),
        width=svg.mm(WIDTH),
        height=svg.mm(HEIGHT),
        elements=elements,
    )


if __name__ == '__main__':
    print(draw())