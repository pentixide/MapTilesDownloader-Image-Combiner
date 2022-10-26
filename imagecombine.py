from PIL import Image
from pathlib import Path
import os

#example path
#'~/MapTilesDownloader-master/MapTilesDownloader-master/src/output/1666706237350/15'
path=''

def findImages(path):
    imDict={}
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".png"):
                tP=Path(root).as_posix()
                if Path(root).as_posix() not in imDict:
                    imDict.update({tP:[file]})
                else:
                    imDict[tP].append(file)
    return imDict

def combineImages(imDict):
    imDim = Image.open(list(imDict.keys())[0]+'/'+imDict[list(imDict.keys())[0]][0]).size[0]
    W=(imDim*len(imDict))
    H=(imDim*len(imDict[list(imDict.keys())[0]]))

    imRtn = Image.new('RGB',(W,H))    
    curX = 0
    
    for y in tD:
        curY = 0
        key = list(tD.keys())
        keyIndex = key.index(y)
        root = key[keyIndex]
        for x in tD[root]:
            image = Image.open(root+'/'+x)
            imRtn.paste(image, (curX,curY))
            curY = curY + image.size[1]
            if(x == tD[y][-1]):
                curX = curX + image.size[0]
    return imRtn

#tD = findImages(path)
image = combineImages(findImages(path))
image.save(path[:path.rfind('/')+1]+str(image)[-12:-1]+'.png')
image.show()
    
