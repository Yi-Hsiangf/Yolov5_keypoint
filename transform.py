from os import listdir
from os.path import isfile, join

def addkey(file_name):
    key = []
    lines = []
    with open(file_name, "r") as fn:
        lines = fn.read().splitlines()
        for line in lines:
            values = line.split(" ")
            key.append((values[1], values[2]))

    with open(file_name, "w") as fn:
        for idx, line in enumerate(lines):
            fn.write(line + " " + key[idx][0] + " " + key[idx][1])
            fn.write("\n")

if __name__ == '__main__':
    train_path = '/home/data/data/2022_yolov5_keypoint/labels/train/'
    files = [f for f in listdir(train_path) if isfile(join(train_path, f))]
    for file_name in files:
        addkey(train_path+file_name)
    
    val_path = '/home/data/data/2022_yolov5_keypoint/labels/val/'
    files = [f for f in listdir(val_path) if isfile(join(val_path, f))]
    for file_name in files:
        addkey(val_path+file_name)
