
import os 
import argparse
import shutil
import glob
# from clearml import Task
import time



k=2 #num folds
input_imgs_path="/mnt/c/Users/haddo/yolov5/datasets/halimeda/NEW_DATASET/images/"
input_labels_path="/mnt/c/Users/haddo/yolov5/datasets/halimeda/NEW_DATASET/labels/"
folds_dir=""

temp_imgs_train=input_imgs_path+"temp_train"
temp_imgs_val=input_imgs_path+"temp_val"

temp_labels_train=input_labels_path+"temp_train"
temp_labels_val=input_labels_path+"temp_val"



inference_instruction_test="python detect.py --weights /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_sizes/{}/weights/best.pt \
                    --project /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_sizes/{}/  --name inference_all_test/ --data data/halimeda_temp.yaml \
                    --source  /mnt/c/Users/haddo/DL_stack/Halimeda/dataset/NEW_DATASET/all_test/images/  --save-txt --save-conf --conf-thres 0.0 --line-thickness 1"


coverage_instruction_test="python /mnt/c/Users/haddo/DL_stack/object_detection_utils/metrics/coverage.py --shape 1024 \
                    --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_sizes/{}/inference_all_test/labels/ \
                    --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_sizes/{}/inference_all_test/coverage/ --grid 500 "
    

eval_instruction_test="python /mnt/c/Users/haddo/DL_stack/Halimeda/scripts/eval_one_thr.py --run_name {}  \
                    --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_sizes/{}/inference_all_test/coverage/ \
                    --out_path /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_sizes/{}/inference_all_test/ --thr 81  \
                    --gt_path  /mnt/c/Users/haddo/DL_stack/Halimeda/dataset/NEW_DATASET/all_test/gt/ --shape 1024"




#check get_im path
temporary_dirs=[temp_imgs_train,temp_imgs_val,temp_labels_train,temp_labels_val]

model_sizes={"yolo_small":"yolov5s.pt","yolo_medium":"yolov5m.pt","yolo_large":"yolov5l.pt","yolo_nano":"yolov5n.pt",}

# model_sizes={"yolo_XL":"yolov5x.pt"}


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

# create_empty_temp_dirs()

val_files_list=[]
train_files_list=[]
create_dirs=True
for model in model_sizes.keys():
    
    
    I=inference_instruction_test.format(model,model) 
    os.system(I)  


    C=coverage_instruction_test.format(model,model) 
    os.system(C)  


    C=eval_instruction_test.format(model,model) 
    os.system(C)  





