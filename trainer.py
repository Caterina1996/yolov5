import os 
import argparse
import shutil
import glob
#k-fold cross validation 

k=5 #num folds
input_imgs_path="/mnt/c/Users/haddo/yolov5/datasets/halimeda/images/"
input_labels_path="/mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/"
folds_dir="train_val_splits"

temp_imgs_train=input_imgs_path+"temp_train"
temp_imgs_val=input_imgs_path+"temp_val"

temp_labels_train=input_labels_path+"temp_train"
temp_labels_val=input_labels_path+"temp_val"

os.mkdir(temp_imgs_train)
os.mkdir(temp_imgs_val)

os.mkdir(temp_labels_train)
os.mkdir(temp_labels_val)


training_instruction="python train.py --img 1200 --batch 8 --epochs 2 --data halimeda.yaml --weights yolov5x.pt  \
                --project /mnt/c/Users/haddo/yolov5/projects/halimeda/yolo_XL/k-fold_training --name {}  \
                --single-cls --hyp data/hyps/hyp.scratch_none.yaml --patience 0"



for i in range(1,k+1):
    #K folds
    os.mkdir("/mnt/c/Users/haddo/yolov5/projects/halimeda/yolo_XL/k-fold_training/"+str(i))
    #copy all files to tmp train and tmp val
    for f in range(1,k+1): 
        if f==i:
            #copy val_files
            #copy images
            for img in glob.glob(input_imgs_path+folds_dir+"/"+i+"/*"):
                shutil.copyfile(img, temp_imgs_val+"/"+img.split("/")[-1])
            #copy labels
            for img in glob.glob(input_labels_path+folds_dir+"/"+i+"/*"):
                shutil.copyfile(img, temp_labels_val+"/"+img.split("/")[-1])
               
        else:
            #copy files to train partition        
            for img in glob.glob(input_imgs_path+folds_dir+"/"+i+"/*"):
                shutil.copyfile(img, temp_imgs_train+"/"+img.split("/")[-1])
            #copy labels
            for img in glob.glob(input_labels_path+folds_dir+"/"+i+"/*"):
                shutil.copyfile(img, temp_labels_train+"/"+img.split("/")[-1])
    
    # 2 Train:
    TI=training_instruction.format(str(i)) 
    os.system(TI)

    #3 Eval 


