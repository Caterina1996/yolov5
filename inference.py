

import argparse
import math
import os
import random
import sys
import time
from copy import deepcopy
from datetime import datetime
from pathlib import Path

import numpy as np
import torch
import torch.distributed as dist
import torch.nn as nn
import yaml
from torch.optim import lr_scheduler
from tqdm import tqdm
import torch
from PIL import ImageGrab
import glob

path_to_images="/home/uib/yolov5/datasets/halimeda/images/train/*"

path_to_model="/home/uib/yolov5/projects/halimeda/runs/exp4/weights"

images=glob.glob(path_to_images)

model = torch.hub.load('ultralytics/yolov5', 'custom', path=path_to_model+'/best.pt')


# crops = results.crop(save=True)  # cropped detections dictionary
for img in images:
    results = model(img)  # inference

    results.save("/home/uib/yolov5/projects/halimeda/runs/exp4/results/")

# im1 = Image.open('zidane.jpg')  # PIL image
# im2 = cv2.imread('bus.jpg')[..., ::-1]  # OpenCV image (BGR to RGB)

# # Inference
# results = model([im1, im2], size=640) # batch of images

# # Results
# results.print()
# results.save()  # or .show()

# results.xyxy[0]  # im1 predictions (tensor)
# results.pandas().xyxy[0]  # im1 predictions (pandas)