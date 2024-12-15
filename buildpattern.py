import svg
import cairosvg
from PIL import Image
import os

import vlinepattern
import vzigzagpattern
import hlinepattern
import squarepattern
import dotpattern
import dotpatternalt
import dotpatternsin2
import dotpatternvsin

WIDTH = 210
HEIGHT = 297
WIDTH_A3 = 297
HEIGHT_A3 = 420

if __name__ == '__main__':
    generators = [
        {'name':'_vlinepattern_',   'description':'full',   'builder':vlinepattern.vlinepattern(WIDTH_A3, HEIGHT_A3),       'steps':[2.6]},
        {'name':'_vlinepattern',    'description':'vertical',   'builder':vlinepattern.vlinepattern(WIDTH_A3, HEIGHT_A3),       'steps':[5,6,7]},
        {'name':'_hlinepattern',    'description':'horizontal',   'builder':hlinepattern.hlinepattern(WIDTH_A3, HEIGHT_A3),       'steps':[5,6,7]},
        {'name':'_zigzagpattern',   'description':'zigzag',   'builder':vzigzagpattern.vzigzagpattern(WIDTH_A3, HEIGHT_A3),   'steps':[5,6,7]},
        {'name':'_squarepattern',   'description':'square',   'builder':squarepattern.squarepattern(WIDTH_A3, HEIGHT_A3),     'steps':[5,6,7]},
        #{'name':'_dotpattern',      'builder':dotpattern.dotpattern(WIDTH_A3, HEIGHT_A3),           'steps':[3,5,6,8]},
        {'name':'_dotpatternalt',   'description':'alt dot',   'builder':dotpatternalt.dotpatternalt(WIDTH_A3, HEIGHT_A3),     'steps':[5,6,8]},
        {'name':'_dotpatternsin',   'description':'sin',   'builder':dotpatternsin2.dotpatternsin2(WIDTH_A3, HEIGHT_A3),   'steps':[5,6,8]},
        {'name':'_dotpatternvsin',  'description':'v sin',   'builder':dotpatternvsin.dotpatternvsin(WIDTH_A3, HEIGHT_A3),   'steps':[5,6,8]}
    
    ]

    for generator in generators:
        patgen = generator['builder']
        steps = generator['steps']
        for step in steps:
            elm = patgen.build (step)
            pattern = svg.SVG(
                viewBox=svg.ViewBoxSpec(0, 0, WIDTH_A3, HEIGHT_A3),
                width=svg.mm(WIDTH_A3),
                height=svg.mm(HEIGHT_A3),
                elements=elm
                )
            pathto = generator['name'] + "_A3_" + str(step) + ".svg"
            with open (pathto, "w") as fout:
                fout.write(str(pattern))
            
            pathto_tmp_png = generator['name'] + "_tmp_" + str(step) + ".png"

            cairosvg.svg2png(url=pathto, write_to=pathto_tmp_png, parent_width=WIDTH_A3 *5, parent_height=HEIGHT_A3*5, output_width=WIDTH_A3*5, output_height=HEIGHT_A3*5)

            im = Image.open(pathto_tmp_png)
            im = im.crop( (16,16,128+16,128+16) )

            pathtopng = generator['name'] + "_A3_" + str(step) + ".png"

            im.save (pathtopng)

            os.remove(pathto_tmp_png)