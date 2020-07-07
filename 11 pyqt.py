#!/usr/bin/env python
import os
from pprint import pprint
import numpy as np
import png
import pydicom
import matplotlib.pyplot as plt
import time

from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
                             QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
                             QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
                             QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
                             QVBoxLayout, QWidget,QScrollArea, QMainWindow)
from PyQt5.QtGui import (QPixmap)

from PyQt5 import uic

import re


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



guiData = {}
guiData['dataset_dir'] = 't'
guiData['dir_names'] = sorted(get_immediate_subdirectories(guiData['dataset_dir']), key=natural_keys)




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



class WidgetGallery(QDialog):
    def __init__(self, guiData,parent = None):
        super(WidgetGallery, self).__init__(parent)

        # self.originalPalette = QApplication.palette()

        styleComboBox = QComboBox()
        # styleComboBox.addItems(QStyleFactory.keys())
        styleComboBox.addItems(guiData['dir_names'])

        self.studyComboBox = styleComboBox

        button1 = QPushButton()
        button1.setText("Button1")
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




        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0,1,1)
        mainLayout.addLayout(imageLayout, 1, 0,1,1)
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
        # print(dcm_list)
        labelList =[]
        for dcm in dcm_list:
            dcmPath = dcm_dir +  dcm
            pngPath = 'png/' + dcmPath + '.png'
            #print(dcmPath)
            #print(pngPath)
            lableNew = QLabel()
            pixmap = QPixmap(pngPath)
            lableNew.setPixmap(pixmap)
            labelList += [lableNew]

        #print(labelList)

        # for labelPng in labelList:
        #     self.imageLayout.addWidget(labelPng)

        labelPng = QLabel()
        pixmap = QPixmap('./png/t/study0/image1.dcm.png')
        labelPng.setPixmap(pixmap)

        #
        # scroll_area = self.scroll
        # draw_widget = self.widget
        #
        # for i in range(1, 50):
        #     object = QLabel("TextLabel")
        #     self.vbox.addWidget(object)
        #
        # draw_widget.setLayout(self.vbox)
        #
        #
        #
        # scroll_area.setWidget(draw_widget)
        # lay = QVBoxLayout(self)
        # lay.addWidget(scroll_area)
        # #lay.addWidget(scroll_area)
        #
        # self.scroll.setFixedHeight(200)
        # self.scroll.setFixedWidth(200)
        #
        # self.mainLayout.addLayout(lay, 2, 0, 1, 1)
        #
        #
        # return

        scroll = QScrollArea()
        widget = QWidget()
        vbox = QHBoxLayout(widget)


        for labelPng in labelList:
            vbox.addWidget(labelPng)

        widget.setLayout(vbox)

        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        #self.scroll.setWidgetResizable(True)

        scroll.setWidget(widget)
        scroll.setFixedHeight(300)
        scroll.setFixedWidth(300)

        #self.imageLayout.setFixedSize(640, 480)

        self.imageLayout.addWidget(scroll)

        # self.setGeometry(300, 300, 300, 200)

    # def initUI(self):
    #     self.scroll = QScrollArea()  # Scroll Area which contains the widgets, set as the centralWidget
    #     self.widget = QWidget()  # Widget that contains the collection of Vertical Box
    #     self.vbox = QVBoxLayout()  # The Vertical Box that contains the Horizontal Boxes of  labels and buttons
    #
    #     for i in range(1, 50):
    #         object = QLabel("TextLabel")
    #         self.vbox.addWidget(object)
    #
    #     self.widget.setLayout(self.vbox)
    #
    #     # Scroll Area Properties
    #     self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
    #     self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    #     self.scroll.setWidgetResizable(True)
    #     self.scroll.setWidget(self.widget)
    #
    #     self.setCentralWidget(self.scroll)
    #
    #     self.setGeometry(600, 100, 1000, 900)
    #
    #
    #     self.mainLayout .addLayout(self.vbox, 1, 0,1,1)
    #
    #     return



    def get_immediate_subfiles(self,a_dir):
        return [name for name in os.listdir(a_dir)]



if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    gallery = WidgetGallery(guiData)
    # gallery.resize(320, 240)
    gallery.show()
    sys.exit(app.exec_())
