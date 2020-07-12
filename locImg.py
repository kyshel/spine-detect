from klib1 import *
import numpy as np
import cv2

WHITE = [255,255,255]
BLACK = [0,0,0]
RED =[0,0,255]
GREEN =[0,255,0]
BLUE =[255,0,0]
YELLOW =[0,243,255]
PINK =[189,0,255]
PURPLE =[255,0,205]

def draw_cross(img,loc,color=BLUE,line_length=10):
    (x,y) = loc
    cv2.line(img,(x,y-line_length),(x,y+line_length),color,1)
    cv2.line(img,(x-line_length,y),(x+line_length,y),color,1)

def locImg(pngPath):
    img = cv2.imread(pngPath)

    cv2.imshow('img', img)







    #cv2.imshow('img2', imgScaled2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




    return img







def main():

    locImg('png/t/study0/image37.dcm.png')






if __name__ == '__main__':
    main()


