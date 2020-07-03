# -*- coding: utf-8 -*-

from pydicom import dcmread
import matplotlib.pyplot as plt

fpath = "./ds/lumbar_train51/train/study0/image1.dcm"

ds = dcmread(fpath)


# print(ds)


plt.imshow(ds.pixel_array, cmap=plt.cm.bone)
plt.show()