# from ultralytics import YOLO
import numpy as np
import matplotlib.pyplot as plt
import os
import glob
import shutil
from clearml import Task
from natsort import natsorted
import random
import time


# path_to_calls="/mnt/c/Users/haddo/DL_stack/yolov5/projects/fish/"
# path_to_project = "/mnt/c/Users/haddo/DL_stack/yolov5/projects/fish/test_sizes"
# path_to_dataset = "/mnt/c/Users/haddo/DL_stack/yolov5/datasets/fish/PLOME_IS/"
# tmp_suffixes = ["images/temp_train/", "labels/temp_train", "images/temp_val", "labels/temp_val"]
# dataset_yaml = "/mnt/c/Users/haddo/DL_stack/yolov5/data/fish.yaml"

path_to_calls = r"C:\Users\Uib\yolov5\projects\halimeda\halimeda_xesc"
path_to_project = r"C:\Users\Uib\yolov5\projects\halimeda\halimeda_xesc"
path_to_dataset = r"C:\Users\Uib\yolov5\datasets\halimeda_xesc"
dataset_yaml = r"C:\Users\Uib\yolov5\data\halimeda_xesc_y_test_git.yaml"

model_size = 'x'
name = 'xesc_y_test_git_desde_best'

txt_path = os.path.join(path_to_calls, f'call_{name}.txt')

run_name=os.path.join(path_to_project, name)

task = Task.init(
    project_name='Halimeda_xesc',
    task_name=run_name,
    output_uri=True # To upload the model and weights to ClearML.
)

# instruction=f"python ../train.py --img 1200 --batch 8 --epochs 200 --data {dataset_yaml} --weights yolov5{model_size}.pt --patience 20 \
# --project {path_to_project} --name {run_name} --seed 42 --device 0"

instruction=f"python ../train.py --img 1200 --batch 8 --epochs 200 --data {dataset_yaml} --weights C:\\Users\\Uib\\yolov5\\projects\\halimeda\\halimeda_xesc\\github_model.pt --patience 20 \
--project {path_to_project} --name {run_name} --seed 42 --device 0"



# instruction="python ../segment/train.py --img 1024 --batch 8 --epochs 200 --data fish.yaml \
#     --weights yolov5n-seg.pt --patience 20  --project /mnt/c/Users/haddo/yolov5/projects/fish/test_sizes --name nano --seed=42"


os.system(instruction)

with open(txt_path, 'a+') as f:
    f.write(instruction)
    # f.write(test_instruction_formatted)
    f.write("\n")
    f.write("------------------------------------------------------------- \n")
    f.write("\n")

print(instruction)
# Use the formatted instructions

task.close()
time.sleep(300)
