# authors : Guillaume Lemaitre <g.lemaitre58@gmail.com>
# license : MIT

import matplotlib.pyplot as plt
import pydicom
from pydicom.data import get_testdata_files
from pprint import pprint

print(__doc__)


dataset = pydicom.dcmread('t/study0/image1.dcm')


# plot the image using matplotlib

pprint(dataset)

plt.imshow(dataset.pixel_array, cmap=plt.cm.bone)
plt.show()