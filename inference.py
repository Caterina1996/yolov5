

import torch
import torch.nn as nn
import torch.optim as optim
import os
import glob
from skimage.io import imread
# path_to_images="/home/uib/yolov5/datasets/halimeda/images/val/*"

path_to_images="/mnt/c/Users/haddo/INVHALI/dataset/OD/test/*"

path_to_model="/mnt/c/Users/haddo/yolov5/projects/halimeda/yolo_nano/fold3_data/weights"

images=glob.glob(path_to_images)


# Load model
def load_model(path):
    # model = torch.load(path_to_model)
    #Alternativa:
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=path+'/best.pt')

    #Això s'ha de fer abans de l'inferència per posar el model en mode inferencia(és pel dropout i batchnorm)
    model.eval()
    return model()


OD_model=load_model(path_to_model)

for img in images:
    im=imread(img)
    results = OD_model(im)  # inference
    print(results)
    # results.save("/home/uib/yolov5/projects/halimeda/runs/exp4/results/")
    results.show()
