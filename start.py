from wand.image import Image as wn
from pathlib import Path
import os
import shutil
from importlib import import_module

def conv(name):
    pdf = wn(filename="allFiles/{}".format(name), resolution=300)
    pdfImages = pdf.convert("jpeg")
    i = 0
    for img in pdfImages.sequence:
        pageImg = wn(image=img)
        if len(pdfImages.sequence)>1:
            pageImg.save(filename='allFiles/{}{}.jpg'.format(name[:-4],i+1))
            i=i+1

        else:
            pageImg.save(filename='allFiles/{}.jpg'.format(name[:-4]))

    return i


fold = Path('allFiles')
files = fold.iterdir()

for file in files:
    c = 0
    if file.name[-3:]!='pdf':
        shutil.move('allFiles/{}'.format(file.name), 'image/{}'.format(file.name))

    else:
        c = conv(file.name)
        if c>0:
            for i in range(1,c+1):
                newName = '{}{}.jpg'.format(file.name[:-4],i)
                shutil.move('allFiles/{}'.format(newName), 'image/{}'.format(newName))
        else:
            newName = '{}.jpg'.format(file.name[:-4])
            shutil.move('allFiles/{}'.format(newName), 'image/{}'.format(newName))

import_module('req')
import_module('extractor')


