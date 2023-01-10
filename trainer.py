import os 
import argparse
import shutil
import glob
#k-fold cross validation 

# Before using call datasetSplitter


# Import comet_ml at the top of your file
# from comet_ml import Experiment

# # Create an experiment with your api key
# experiment = Experiment(
#     api_key="g1hZLRyJgRN8tIfc25oDC3ACG",
#     project_name="halimeda",
#     workspace="caterina1996",
# )


k=5 #num folds
input_imgs_path="/mnt/c/Users/haddo/yolov5/datasets/halimeda/images/"
input_labels_path="/mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/"
folds_dir="train_val_splits"

temp_imgs_train=input_imgs_path+"temp_train"
temp_imgs_val=input_imgs_path+"temp_val"

temp_labels_train=input_labels_path+"temp_train"
temp_labels_val=input_labels_path+"temp_val"


training_instruction="python train.py --img 1200 --batch 8 --epochs 200 --data halimeda.yaml --weights yolov5x.pt  \
                    --project /mnt/c/Users/haddo/yolov5/projects/halimeda/yolo_XL/k-fold_training --name {}  \
                    --single-cls --hyp data/hyps/hyp.scratch-low.yaml --save-period 10 "

inference_instruction="python detect.py --weights /mnt/c/Users/haddo/yolov5/projects/halimeda/yolo_XL/k-fold_training/{}/weights/best.pt \
                    --project /mnt/c/Users/haddo/yolov5/projects/halimeda/yolo_XL/k-fold_training/{}/  --name inference_web/ --data data/halimeda.yaml \
                    --source  /mnt/c/Users/haddo/yolov5/datasets/halimeda/images/from_web"

temporary_dirs=[temp_imgs_train,temp_imgs_val,temp_labels_train,temp_labels_val]

def create_empty_temp_dirs():
    for temp_dir in temporary_dirs:
        if not os.path.exists(temp_dir):
            os.mkdir(temp_dir)
        else:
            shutil.rmtree(temp_dir)
            os.mkdir(temp_dir)

create_empty_temp_dirs()

val_files_list=[]
train_files_list=[]

for i in range(1,k+1):
    #K folds 
    
    # Create folders:-> Això no fa falta perquè es crea tot sol?
    # if not os.path.exists("/mnt/c/Users/haddo/yolov5/projects/halimeda/yolo_XL/k-fold_training/"+str(i)):
    #     os.mkdir("/mnt/c/Users/haddo/yolov5/projects/halimeda/yolo_XL/k-fold_training/"+str(i))
    # else:
    #     os.mkdir("/mnt/c/Users/haddo/yolov5/projects/halimeda/yolo_XL/k-fold_training/"+str(i))
    #     shutil.rmtree("/mnt/c/Users/haddo/yolov5/projects/halimeda/yolo_XL/k-fold_training/"+str(i))

    #copy all files to tmp train and tmp val
    for f in range(1,k+1): 
        if f==i:
            #copy val_files
            #copy images
            for img in glob.glob(input_imgs_path+folds_dir+"/"+str(f)+"/*"):
                shutil.copyfile(img, temp_imgs_val+"/"+img.split("/")[-1])
                # val_files_list.append(img)
            #copy labels
            for img in glob.glob(input_labels_path+folds_dir+"/"+str(f)+"/*"):
                shutil.copyfile(img, temp_labels_val+"/"+img.split("/")[-1])
               
        else:
            #copy files to train partition        
            for img in glob.glob(input_imgs_path+folds_dir+"/"+str(f)+"/*"):
                shutil.copyfile(img, temp_imgs_train+"/"+img.split("/")[-1])
                # train_files_list.append(img)
            #copy labels
            for img in glob.glob(input_labels_path+folds_dir+"/"+str(f)+"/*"):
                shutil.copyfile(img, temp_labels_train+"/"+img.split("/")[-1])

    # print("train Files list len",len(train_files_list))
    # print("val Files list len",len(val_files_list))
    # train_files_list.extend(val_files_list)
    # print("Files list set len",len(set(train_files_list)))
    # val_files_list=[]
    # train_files_list=[]

    
    # 2 Train and eval (eval comming with train):
    T=training_instruction.format(str(i)) 
    os.system(T)

    #3 Inference:
    I=inference_instruction.format(str(i),str(i)) 
    os.system(I)

    #4 Remove temporary directories and create new ones
    create_empty_temp_dirs()



