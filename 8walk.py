import os
for root, dirs, files in os.walk("t"):
    for file in files:
        if file.endswith(".dcm"):
             print(os.path.join(root, file))