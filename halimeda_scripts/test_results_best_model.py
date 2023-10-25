import os 
import argparse
import shutil
import glob
# from clearml import Task
import time
"""
This code applies k-fold cross validation 

Input: Dataset splitted in k folders(partitions)
For each fold the code trains with all folders data except one and uses the remaining one as validation
It also does inference and calculates test metrics (pascalvoc and coverage) for best thr

"""

#k-fold cross validation 
# Before using call datasetSplitter

k=5 #num folds
input_imgs_path="/mnt/c/Users/haddo/yolov5/datasets/halimeda/NEW_DATASET/images/"
input_labels_path="/mnt/c/Users/haddo/yolov5/datasets/halimeda/NEW_DATASET/labels/"
folds_dir=""

temp_imgs_train=input_imgs_path+"temp_train"
temp_imgs_val=input_imgs_path+"temp_val"

temp_labels_train=input_labels_path+"temp_train"
temp_labels_val=input_labels_path+"temp_val"

inference_instruction="python detect.py --weights /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/{}/weights/best.pt \
                    --project /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/{}/  --name inference_test/ --data data/halimeda_temp.yaml \
                    --source  /mnt/c/Users/haddo/yolov5/datasets/halimeda/NEW_DATASET/images/test/  --save-txt --save-conf --conf-thres 0.0 --line-thickness 1"


coverage_instruction="python /mnt/c/Users/haddo/DL_stack/object_detection_utils/metrics/coverage.py --shape 1024 \
                    --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/{}/inference_test/labels/ \
                    --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/{}/inference_test/coverage/ --grid 500 "

eval_ss2_instruction="python /mnt/c/Users/haddo/DL_stack/object_detection_utils/metrics/eval_ss2.py \
                    --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/{}/inference_test/coverage/ \
                    --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/NEW_DATASET/labels/test_coverage/  \
                    --run_name {} --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/{}/ --shape 1024"



#check get_im path
temporary_dirs=[temp_imgs_train,temp_imgs_val,temp_labels_train,temp_labels_val]

# config_files=["hyp.base.yaml", "hyp.base_da.yaml", "hyp.high3.yaml", "hyp.high3_da.yaml", "hyp.low27.yaml", "hyp.low27_da.yaml", "hyp.low3.yaml", "hyp.low3_da.yaml", "hyp.low9.yaml", "hyp.low9_da.yaml"]
config_files=[ "hyp.low9_da.yaml"]

def create_empty_temp_dirs():
    for temp_dir in temporary_dirs:
        if not os.path.exists(temp_dir):
            os.mkdir(temp_dir)
        else:
            shutil.rmtree(temp_dir)
            os.mkdir(temp_dir)


def create_empty_permanent_dirs():
    for i in range(1,k+1):
        for temp_dir in temporary_dirs:
            if not os.path.exists(temp_dir+"_"+str(i)):
                os.mkdir(temp_dir+"_"+str(i))
            else:
                print("THIS FOLDER ALREADY EXISTS!!")

create_empty_temp_dirs()

val_files_list=[]
train_files_list=[]
create_dirs=True
for config in config_files:
    config_name=config.split(".")[1]
     
    for i in range(1,6):
        training_name=config_name+"/"+str(i)

        I=inference_instruction.format(str(training_name),str(training_name)) 
        print("hola!!")
        os.system(I)    

        C=coverage_instruction.format(str(training_name),str(training_name)) 
        os.system(C)

        SS=eval_ss2_instruction.format(str(training_name),str(training_name),str(training_name)) 
        os.system(SS)

       


