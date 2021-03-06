# authors : Guillaume Lemaitre <g.lemaitre58@gmail.com>
# license : MIT

import difflib

import pydicom
from pydicom.data import get_testdata_files

print(__doc__)

filename_mr = get_testdata_files('MR_small.dcm')[0]
filename_ct = get_testdata_files('CT_small.dcm')[0]

datasets = tuple([pydicom.dcmread(filename, force=True)
                  for filename in (filename_mr, filename_ct)])

# difflib compare functions require a list of lines, each terminated with
# newline character massage the string representation of each dicom dataset
# into this form:
rep = []
for dataset in datasets:
    lines = str(dataset).split("\n")
    lines = [line + "\n" for line in lines]  # add the newline to end
    rep.append(lines)


diff = difflib.Differ()
for line in diff.compare(rep[0], rep[1]):
    if line[0] != "?":
        print(line)