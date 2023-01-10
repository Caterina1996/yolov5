import os 
import argparse
import shutil
import glob

from comet_ml import Experiment

# Create an experiment with your api key
experiment = Experiment(
    api_key="g1hZLRyJgRN8tIfc25oDC3ACG",
    project_name="halimeda",
    workspace="caterina1996",
)

training_instruction="python train.py --img 1280 --batch 8 --epochs 200 --data halimeda.yaml --weights yolov5x6.pt  \
                    --project /mnt/c/Users/haddo/yolov5/projects/halimeda/yolo_X6/k-fold_training --name hyp_high_2  \
                    --single-cls --hyp data/hyps/hyp.scratch-high_2.yaml --save-period 10 "


# T=training_instruction.format(str(i)) 
os.system(T)