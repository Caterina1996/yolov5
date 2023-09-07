import os 
import argparse
import shutil
import glob

"""
This code applies k-fold cross validation 

Input: Dataset splitted in k folders(partitions)
For each fold the code trains with all folders data except one and uses the remaining one as validation
It also does inference and calculates test metrics (pascalvoc and coverage) for best thr

"""


#k-fold cross validation 
# Before using call datasetSplitter


training_instruction="python train.py --img 1024 --batch 8 --epochs 200 --data valves2d.yaml --weights yolov5x.pt  \
                    --project /mnt/c/Users/haddo/yolov5/projects/valves2d/ --name default_params_adam_2 --single-cls --patience 10"


inference_instruction="python detect.py --weights /mnt/c/Users/haddo/yolov5/projects/valves2d/default_params_adam_2/weights/best.pt \
                    --project /mnt/c/Users/haddo/yolov5/projects/valves2d/default_params_adam_2  --name inference_test/ --data data/valves2d.yaml \
                    --source  /mnt/c/Users/haddo/yolov5/datasets/valves_2d/images/test/  --save-txt --save-conf --conf-thres 0 --line-thickness 1"

inference_instruction="python detect.py --weights /mnt/c/Users/haddo/yolov5/projects/valves2d/default_params_adam_2/weights/best.pt \
                    --project /mnt/c/Users/haddo/yolov5/projects/valves2d/default_params_adam_2  --name inference_test_thr/ --data data/valves2d.yaml \
                    --source  /mnt/c/Users/haddo/yolov5/datasets/valves_2d/images/test/  --save-txt --save-conf --conf-thres 0.27 --line-thickness 5"


inference_instruction="python detect.py --weights /mnt/c/Users/haddo/yolov5/projects/valves2d/default_params_adam_2/weights/best.pt \
                    --project /mnt/c/Users/haddo/yolov5/projects/valves2d/default_params_adam_2  --name inference_train/ --data data/valves2d.yaml \
                    --source  /mnt/c/Users/haddo/yolov5/datasets/valves_2d/images/train/  --save-txt --save-conf --conf-thres 0 --line-thickness 1"


pascalvoc_instruction="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py \
                    -tiou 0.5 -tconf 0.01 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh \
                    -gt /mnt/c/Users/haddo/yolov5/datasets/valves_2d/labels/test -det /mnt/c/Users/haddo/yolov5/projects/valves2d/default_params_adam_2/inference_test/labels/ \
                    -np -sp /mnt/c/Users/haddo/yolov5/projects/valves2d/default_params_adam_2/pascalvoc/"


pascalvoc_instruction="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py \
                    -tiou 0.5 -tconf 0.01 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh \
                    -gt /mnt/c/Users/haddo/yolov5/datasets/valves_2d/labels/test -det /mnt/c/Users/haddo/yolov5/projects/valves2d/default_params_adam_2/inference_test/labels/ \
                    -np -sp /mnt/c/Users/haddo/yolov5/projects/valves2d/default_params_adam_2/pascalvoc/"


pascalvoc_instruction="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py \
                    -tiou 0.5 -tconf 0.01 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh \
                    -gt /mnt/c/Users/haddo/yolov5/datasets/valves_2d/labels/train -det /mnt/c/Users/haddo/yolov5/projects/valves2d/default_params_adam_2/inference_train/labels/ \
                    -np -sp /mnt/c/Users/haddo/yolov5/projects/valves2d/default_params_adam_2/pascalvoc/"


# 2) Train and eval (eval comming with train):
T=training_instruction
os.system(T)

# 3) Inference:
I=inference_instruction
os.system(I)

# 4) Pascalvoc:
P=pascalvoc_instruction
os.system(P)



