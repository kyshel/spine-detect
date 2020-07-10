import glob, os
os.chdir("../glob")
for file in glob.glob("*.txt"):
    print(file)