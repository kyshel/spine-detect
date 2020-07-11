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


    return img



def markImg(pngPath,instanceInfo):

    # print(pngPath)
    # print(instanceInfo['annotation']['data'])

    img = cv2.imread(pngPath)

    for anno in instanceInfo['annotation'] :
        for point in anno['data']['point']:
            cx,cy = point['coord'][0],point['coord'][1]
            loc_text = (int(cx) + 40, int(cy))

            draw_cross(img, (cx,cy), color=BLUE, line_length=3)
            # cv2.circle(img, (cx, cy), 2, RED, thickness=1, lineType=8, shift=0)

            if 'disc' in point['tag']:
                level = point['tag']['disc']
            elif 'vertebra' in point['tag']:
                level = point['tag']['vertebra']
            else:
                level = 'WRONG LEVEL!'


            TEXT = point['tag']['identification'] + ':' + level
            TEXT_FACE = cv2.FONT_HERSHEY_DUPLEX
            TEXT_SCALE = 0.4
            TEXT_THICKNESS = 1

            text_size, _ = cv2.getTextSize(TEXT, TEXT_FACE, TEXT_SCALE, TEXT_THICKNESS)
            text_loc_fix = (loc_text[0], int(loc_text[1] + text_size[1] / 2))

            cv2.putText(img, text=TEXT,
                        org=text_loc_fix,
                        fontFace=TEXT_FACE,
                        fontScale=TEXT_SCALE, color=YELLOW, thickness=TEXT_THICKNESS, lineType=cv2.LINE_AA)

            cv2.line(img, (cx+5, cy), loc_text, YELLOW, thickness=1)


            # print(point)


    return img








def main():
    with open('lumbar_train51_annotation.json') as f:
        json_origin = json.load(f)

    json_indexed = indexListAccordKey(json_origin, 'studyUid')
    instanceInfo = json_indexed['1.2.430.2608.1.285.6961.2270.33760357']['data'][0]
    img = markImg('png/t/study0/image37.dcm.png', instanceInfo)
    img2 = locImg('png/t/study0/image37.dcm.png')

    scaleMulti = 3
    imgScaled1 = cv2.resize(img, (scaleMulti * img.shape[0], scaleMulti * img.shape[1]))
    imgScaled2 = cv2.resize(img2, (scaleMulti * img2.shape[0], scaleMulti * img2.shape[1]))
    img_concate_Verti = np.concatenate((imgScaled1, imgScaled2), axis=1)

    cv2.imshow('img_concate_Verti', img_concate_Verti)
    #cv2.imshow('img2', imgScaled2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



if __name__ == '__main__':
    main()


