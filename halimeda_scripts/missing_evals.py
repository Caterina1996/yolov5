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


training_instruction="python train.py --img 1024 --batch 8 --epochs 200 --data halimeda_temp.yaml --weights yolov5x.pt --patience 60 \
                    --project /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET --name {}  \
                    --single-cls --hyp data/hyps/final/{}"


# training_instruction="python train.py --img 1024 --batch 8 --epochs 200 --data halimeda_temp.yaml --weights yolov5x.pt --patience 60 \
#                     --project /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET --name low_27_da/2/  \
#                     --single-cls --hyp data/hyps/final/hyp.low27_da.yaml"


inference_instruction="python detect.py --weights /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/{}/weights/best.pt \
                    --project /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/{}/  --name inference_val/ --data data/halimeda_temp.yaml \
                    --source  /mnt/c/Users/haddo/yolov5/datasets/halimeda/NEW_DATASET/images/temp_val/  --save-txt --save-conf --conf-thres 0.0 --line-thickness 1"


pascalvoc_instruction="python /mnt/c/Users/haddo/DL_stack/object_detection_utils/metrics/pascalvoc.py \
                    -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh \
                    -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/NEW_DATASET/labels/temp_val -det /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/{}inference_val/labels/ \
                    -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/{}/pascalvoc/"


coverage_instruction="python /mnt/c/Users/haddo/DL_stack/object_detection_utils/metrics/coverage.py --shape 1024 \
                    --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/{}/inference_val/labels/ \
                    --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/{}/inference_val/coverage/ --grid 500 "

eval_ss2_instruction="python /mnt/c/Users/haddo/DL_stack/object_detection_utils/metrics/eval_ss2.py \
                    --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/{}/inference_val/coverage/ \
                    --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/NEW_DATASET/labels/coverage/{}/  \
                    --run_name {} --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/{}/ --shape 1024"



#check get_im path
temporary_dirs=[temp_imgs_train,temp_imgs_val,temp_labels_train,temp_labels_val]

# config_files=["hyp.base.yaml", "hyp.base_da.yaml", "hyp.high3.yaml", "hyp.high3_da.yaml", "hyp.low27.yaml", "hyp.low27_da.yaml", "hyp.low3.yaml", "hyp.low3_da.yaml", "hyp.low9.yaml", "hyp.low9_da.yaml"]
config_files=[ "hyp.low27_da.yaml"]

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
     
    i=2
    training_name=config_name+"/"+str(i)
    # task = Task.init(project_name='HALIMEDA_HYPS', task_name=training_name)
    #1) K folds:
    #Copy all files to tmp train and tmp val
    if create_dirs:
        for f in range(1,k+1): 
            if f==i:
                print("copying val files")
                #copy val_files
                #copy images
                print("PATH: ",input_imgs_path+folds_dir+"/"+str(f)+"/*")
                for img in glob.glob(input_imgs_path+folds_dir+"/"+str(f)+"/*"):
                    shutil.copyfile(img, temp_imgs_val+"/"+img.split("/")[-1])
                    
                    val_files_list.append(img)
                #copy labels
                for img in glob.glob(input_labels_path+folds_dir+"/"+str(f)+"/*"):
                    shutil.copyfile(img, temp_labels_val+"/"+img.split("/")[-1])
                
            else:
                #copy files to train partition        
                print("copying train files")

                for img in glob.glob(input_imgs_path+folds_dir+"/"+str(f)+"/*"):
                    shutil.copyfile(img, temp_imgs_train+"/"+img.split("/")[-1])
                    train_files_list.append(img)
                #copy labels
                for img in glob.glob(input_labels_path+folds_dir+"/"+str(f)+"/*"):
                    shutil.copyfile(img, temp_labels_train+"/"+img.split("/")[-1])

            print("train Files list len",len(train_files_list))
            print("val Files list len",len(val_files_list))
            train_files_list.extend(val_files_list)
            print("Files list set len",len(set(train_files_list)))

            val_files_list=[]
            train_files_list=[]

        # 2) Train and eval (eval comming with train):
        # python train.py --img 1024 --batch 8 --epochs 200 --data halimeda_temp.yaml --weights yolov5x.pt --patience 60 \
        #             --project /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET --name {}  \
        #             --single-cls --hyp {}"


        T=training_instruction.format(str(training_name),str(config)) 
        os.system(T)

        # 3) Inference:
        """
        inference_instruction="python detect.py --weights /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/{}/weights/best.pt \
                    --project /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/{}/  --name inference_val/ --data data/halimeda_temp.yaml \
                    --source  /mnt/c/Users/haddo/yolov5/datasets/halimeda/NEW_DATASET/images/temp_val/  --save-txt --save-conf --conf-thres 0.0 --line-thickness 1"

        """
        I=inference_instruction.format(str(training_name),str(training_name)) 
        print("hola!!")
        os.system(I)    

        """
        pascalvoc_instruction="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py \
            -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh \
            -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/NEW_DATASET/labels/temp_val -det /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/{}inference_val/labels/ \
            -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/{}/pascalvoc/"
        """

        # 4) Pascalvoc:
        # P=pascalvoc_instruction.format(str(training_name),str(training_name)) 
        # os.system(P)

        # 5) Coverage:
        """
        
        coverage_instruction="python /mnt/c/Users/haddo/DL_stack/object_detection_utils/metrics/coverage.py --shape 1024 \
                    --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/{}/inference_val/labels/ \
                    --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/{}/inference_val/coverage/ --grid 500 "
        """
        C=coverage_instruction.format(str(training_name),str(training_name)) 
        os.system(C)

        # 6) Eval SS_2:
        """
        
        eval_ss2_instruction="python /mnt/c/Users/haddo/DL_stack/object_detection_utils/metrics/eval_ss2.py \
                    --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/{}/inference_val/coverage/ \
                    --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/NEW_DATASET/labels/coverage/{}/  \
                    --run_name {} --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/{}/ --shape 1024"
        """
        SS=eval_ss2_instruction.format(str(training_name),str(i),str(training_name),str(training_name)) 
        os.system(SS)

        # 7) Remove temporary directories and create new ones:
        create_empty_temp_dirs()
        # task.close()
       


