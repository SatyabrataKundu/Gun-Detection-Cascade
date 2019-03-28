import os
path = 'D:/Gun-Detection-Cascade/negetiveImageSource'
files = os.listdir(path)
i = 10001

for file in files:
    os.rename(os.path.join(path, file), os.path.join(path, str(i)+'.jpg'))
    i = i+1