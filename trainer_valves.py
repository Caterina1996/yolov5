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


training_instruction="python train.py --img 1024 --batch 8 --epochs 200 --data valves2d.yaml --weights yolov5n.pt  \
                    --project /mnt/c/Users/haddo/yolov5/projects/valves2d/ --name default_params_adam --single-cls --patience 10 --optimizer Adam"


inference_instruction="python detect.py --weights /mnt/c/Users/haddo/yolov5/projects/valves2d/default_params/weights/best.pt \
                    --project /mnt/c/Users/haddo/yolov5/projects/valves2d/default_params_adam  --name inference_test/ --data data/valves2d.yaml \
                    --source  /mnt/c/Users/haddo/yolov5/datasets/valves_2d/images/test/  --save-txt --save-conf --conf-thres 0 --line-thickness 1"


pascalvoc_instruction="python /mnt/c/Users/haddo/DL_stack/object_detection_utils/metrics/pascalvoc.py \
                    -tiou 0.5 -tconf 0.01 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh \
                    -gt /mnt/c/Users/haddo/yolov5/datasets/valves_2d/labels/test -det /mnt/c/Users/haddo/yolov5/projects/valves2d/default_params_adam/inference_test/labels/ \
                    -np -sp /mnt/c/Users/haddo/yolov5/projects/valves2d/default_params_adam/pascalvoc/"


# pascalvoc_instruction="python /mnt/c/Users/haddo/DL_stack/object_detection_utils/metrics/pascalvoc.py \
#                     -tiou 0.5 -tconf 0.01 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh \
#                     -gt /mnt/c/Users/haddo/yolov5/datasets/valves_2d/labels/val -det /mnt/c/Users/haddo/yolov5/projects/valves2d/default_params_ES/inference_val/labels/ \
#                     -np -sp /mnt/c/Users/haddo/yolov5/projects/valves2d/default_params_ES/pascalvoc_val/"


# 2) Train and eval (eval comming with train):
T=training_instruction
os.system(T)

# 3) Inference:
I=inference_instruction
os.system(I)

# 4) Pascalvoc:
P=pascalvoc_instruction
os.system(P)



# inference_instruction_OD="python detect.py --weights /mnt/c/Users/haddo/yolov5/projects/halimeda/k-fold_training_2/3/weights/best.pt \
#                     --project /mnt/c/Users/haddo/DL_stack/yolov5/projects/halimeda  --name inference_gopro/ --data data/halimeda_temp.yaml \
#                     --source  /mnt/c/Users/haddo/DL_stack/Halimeda/dataset/survey_gopro/  --save-txt --save-conf --conf-thres 0.1 --line-thickness 1"

# inference_SS="python inference.py --run_path ../model/ --data_path /mnt/c/Users/haddo/DL_stack/Halimeda/dataset/survey_gopro/ --shape 1024"



# merge="python merge_blobs.py --path_od ../merge/video_gopro/inference_OD/labels/ --path_ss ../merge/video_gopro/inference_SS/ --path_merge ../merge/video_gopro/merged  \
#                              --iter 1  --ns 12 3 1 2 1 1 1 1 1 1"