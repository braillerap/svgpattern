import fnmatch
import sys
import os
import base64 
import json

def main ():
    patlist =[]
    if len(sys.argv) < 2:
        print ("jsonpackage <filter>")
        print ("jsonpackage *.svg")
    
    filter = sys.argv[1]
    print (filter)
    files = fnmatch.filter(os.listdir(), filter)
    print (files)

    for file in files:
        print (file)
        fpng = os.path.splitext(file)
        print (fpng)
        pngpath = fpng[0] + ".png"
        print (pngpath)
        patlist.append( (file, pngpath,fpng[0] ) )
        print (patlist)

    package = []
    for file in patlist:
        
        print (file)
        with open(file[0], 'r') as f:
            data = f.read()
        with open(file[1], 'rb') as f:
            png = base64.b64encode(f.read()).decode('ascii')


            package.append ({"fname":file[2], "data":data, "image":png})    
    print(len(package))
    json.dump (package, open("packagesvg.json", "w"))

if __name__ == '__main__':
    main ()
