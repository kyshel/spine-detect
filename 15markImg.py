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

def markImg(pngPath,instanceInfo):

    # print(pngPath)
    # print(instanceInfo)

    img = cv2.imread(pngPath )
    # cv2.circle(img, (125,50), 5, RED, thickness=5, lineType=8, shift=0)
    cx = 125
    cy = 125
    loc_text = (int(cx)+30,int(cy))




    cv2.circle(img, (cx, cy), 3, RED, thickness=2, lineType=8, shift=0)
    # cv2.circle(img, (50, 50), 5, GREEN, thickness=5, lineType=6, shift=0)




    TEXT = '0aA'
    TEXT_FACE = cv2.FONT_HERSHEY_DUPLEX
    TEXT_SCALE = 1
    TEXT_THICKNESS = 1


    text_size, _ = cv2.getTextSize(TEXT, TEXT_FACE, TEXT_SCALE, TEXT_THICKNESS)
    text_loc_fix = (loc_text[0] , int(loc_text[1] + text_size[1] / 2))

    cv2.putText(img, text=TEXT,
                org=text_loc_fix,
                fontFace=TEXT_FACE,
                fontScale=TEXT_SCALE, color=YELLOW, thickness=TEXT_THICKNESS, lineType=cv2.LINE_AA)

    cv2.line(img, (cx, cy), loc_text, YELLOW, thickness=1)










    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



    pass




with open('lumbar_train51_annotation.json') as f:
    json_origin = json.load(f)

json_indexed = indexListAccordKey(json_origin,'studyUid')
instanceInfo = json_indexed['1.2.430.2608.1.285.6961.2270.33760357']['data'][0]
markImg('png/t/study0/image37.dcm.png',instanceInfo)

