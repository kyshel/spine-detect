#!/usr/bin/env python
import os
from pprint import pprint
import numpy as np
import png
import pydicom
import matplotlib.pyplot as plt
import time
from pydicom import dcmread

from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication,QComboBox,
                             QGridLayout, QHBoxLayout, QVBoxLayout,QLabel,
                             QPushButton, QWidget,QScrollArea)
from PyQt5.QtGui import (QPixmap,QImage)

#from PyQt5 import uic

import re

import json


def atoi(text):
    return int(text) if text.isdigit() else text


def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [atoi(c) for c in re.split(r'(\d+)', text)]


import os


def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

def cvImg2qImg(cvImg):
    height, width, channel = cvImg.shape
    bytesPerLine = 3 * width
    qImg = QImage(cvImg.data, width, height, bytesPerLine, QImage.Format_RGB888)
    return qImg

def getMarkedImg(pngPath,dcmInfo,json_whole_rebuild):

    studyUid = dcmInfo['(0020, 000d)']['value']
    instanceUid = dcmInfo['(0008, 0018)']['value']


    for instance_marked in json_whole_rebuild[studyUid]['data']:
        # print(instance_marked['instanceUid'])

        if instanceUid == instance_marked['instanceUid'] :
            print("cur  insID is :" + instance_marked['instanceUid'])
            print("mark insID is :" + instanceUid)
            print('matched')

            markImg(pngPath,instance_marked)


    pass

def markImg(pngPath,instanceInfo):

    print(pngPath)
    print(instanceInfo)



    pass






def indexListAccordKey(list,key):
    indexedList = {}
    for item in list:
        key_val = item[key]
        item.pop(key, None)
        indexedList[key_val] = item
    return indexedList


guiData = {}
guiData['dataset_dir'] = 't'
guiData['dir_names'] = sorted(get_immediate_subdirectories(guiData['dataset_dir']), key=natural_keys)

with open('lumbar_train51_annotation.json') as f:
    json_origin = json.load(f)


guiData['json_whole_indexed'] = indexListAccordKey(json_origin,'studyUid')



def dcm2png(file_src):
    ds = pydicom.dcmread(file_src)
    shape = ds.pixel_array.shape

    # Convert to float to avoid overflow or underflow losses.
    image_2d = ds.pixel_array.astype(float)

    # Rescaling grey scale between 0-255
    image_2d_scaled = (np.maximum(image_2d, 0) / image_2d.max()) * 255.0

    # Convert to uint
    image_2d_scaled = np.uint8(image_2d_scaled)

    plt.imshow(image_2d_scaled)
    plt.show()



class WidgetGallery(QScrollArea):
    def __init__(self,guiData):
        super(WidgetGallery, self).__init__()

        styleComboBox = QComboBox()
        styleComboBox.addItems(guiData['dir_names'])

        self.studyComboBox = styleComboBox

        button1 = QPushButton()
        button1.setText("Button1")
        #button1.setIcon(QIcon('png/t/study0/image1.dcm.png'))

        button1.clicked.connect(self.button1_clicked)

        # labelPng = QLabel()
        # pixmap = QPixmap('./png/t/study0/image1.dcm.png')
        # labelPng.setPixmap(pixmap)

        styleLabel = QLabel("&Style:")
        styleLabel.setBuddy(styleComboBox)

        topLayout = QHBoxLayout()
        topLayout.addWidget(styleLabel)
        topLayout.addWidget(styleComboBox)
        topLayout.addWidget(button1)
        # topLayout.addWidget(labelPng)

        imageLayout = QHBoxLayout()
        self.imageLayout = imageLayout
        self.label1=styleLabel

        jsonLayout = QHBoxLayout()





        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0,1,1)
        mainLayout.addLayout(imageLayout, 1, 0,1,1)
        mainLayout.addLayout(jsonLayout, 2, 0, 1, 1)
        self.mainLayout = mainLayout

        #self.initUI()


        self.setLayout(mainLayout)
        self.setWindowTitle("Styles")
        self.guiData = guiData

        #print(self.get_immediate_subfiles('./t/study0/'))
        button1.click()




    def button1_clicked(self):
        current_study = str(self.studyComboBox.currentText())
        self.label1.setText(current_study)
        dcm_dir =  self.guiData['dataset_dir'] + '/' + current_study + '/'
        dcm_list = self.get_immediate_subfiles(dcm_dir)

        eleList =[]

        for dcm in dcm_list:
            dcmPath = dcm_dir +  dcm
            pngPath = 'png/' + dcmPath + '.png'

            ds = dcmread(dcmPath)
            tag_list = [[0x0020, 0x000d],
                        [0x0020, 0x000e],
                        [0x0008, 0x0018],
                        [0x0020, 0x0052],
                        [0x0010, 0x1010],
                        [0x0010, 0x1030],
                        [0x0018, 0x0050],
                        [0x0018, 0x0088],
                        [0x0028, 0x0030]]

            newDcmInfo = {}
            for tag in tag_list:
                newLine = {}
                newLine['keyword']= ds[tag].keyword
                newLine['value'] = str(ds[tag].value)
                newDcmInfo[str(ds[tag].tag)] = newLine

            #print(newDcmInfo)

            stringInfo = json.dumps(newDcmInfo,indent=4, sort_keys=True)
            # print(stringInfo)



            labelNew = QLabel()
            finalImage = getMarkedImg(pngPath,newDcmInfo,guiData['json_whole_indexed'])

            pixmap = QPixmap(finalImage)
            labelNew.setPixmap(pixmap)

            newEle = {}
            newEle['filename'] = QLabel(dcm)
            newEle ['info'] = QLabel(stringInfo)
            newEle ['label'] = labelNew

            eleList += [newEle]

        #exit()

        # clean imageLayout
        for i in reversed(range(self.imageLayout.count())):
            self.imageLayout.itemAt(i).widget().setParent(None)




        scroll = QScrollArea()
        widget = QWidget()
        vbox = QHBoxLayout(widget)



        for ele in eleList:
            eleLayout = QVBoxLayout()
            eleLayout.addWidget(ele['label'])
            eleLayout.addWidget(ele['filename'])
            eleLayout.addWidget(ele['info'])

            vbox.addLayout(eleLayout)


        widget.setLayout(vbox)
        scroll.setWidget(widget)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        scroll.setFixedWidth(1280)
        scroll.setFixedHeight(600)

        self.imageLayout.addWidget(scroll)

    def imageClick(self):
        pass


    def get_immediate_subfiles(self,a_dir):
        return [name for name in os.listdir(a_dir)]


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    gallery = WidgetGallery(guiData)
    # gallery.resize(320, 240)
    gallery.show()
    sys.exit(app.exec_())
