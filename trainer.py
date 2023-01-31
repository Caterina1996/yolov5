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


k=10 #num folds
input_imgs_path="/mnt/c/Users/haddo/yolov5/datasets/halimeda/kfold/images/"
input_labels_path="/mnt/c/Users/haddo/yolov5/datasets/halimeda/kfold/labels/"
folds_dir=""

temp_imgs_train=input_imgs_path+"temp_train"
temp_imgs_val=input_imgs_path+"temp_val"

temp_labels_train=input_labels_path+"temp_train"
temp_labels_val=input_labels_path+"temp_val"


training_instruction="python train.py --img 1200 --batch 8 --epochs 200 --data halimeda_temp.yaml --weights yolov5x.pt  \
                    --project /mnt/c/Users/haddo/yolov5/projects/halimeda/k-fold_training_2 --name {}  \
                    --single-cls --hyp data/hyps/hyp.scratch-low.yaml --save-period 10 "

inference_instruction="python detect.py --weights /mnt/c/Users/haddo/yolov5/projects/halimeda/k-fold_training/{}/weights/best.pt \
                    --project /mnt/c/Users/haddo/yolov5/projects/halimeda/k-fold_training/{}/  --name inference_test_3/ --data data/halimeda_temp.yaml \
                    --source  /mnt/c/Users/haddo/yolov5/datasets/halimeda/kfold/images/test/  --save-txt --save-conf --conf-thres 0.03"

inference_instruction_SS="python detect.py --weights /mnt/c/Users/haddo/yolov5/projects/halimeda/k-fold_training/{}/weights/best.pt \
                    --project /mnt/c/Users/haddo/yolov5/projects/halimeda/k-fold_training/{}/  --name inference_SS_3/ --data data/halimeda_temp.yaml \
                    --source  /mnt/c/Users/haddo/yolov5/datasets/halimeda/segmentation/  --save-txt --save-conf --conf-thres 0.03"

pascalvoc_instruction="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py \
                    -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh \
                    -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/kfold/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/k-fold_training_2/{}/inference_test/labels/ \
                    -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/k-fold_training_2/{}/pascalvoc/"

coverage_instruction="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 \
                    --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/k-fold_training_2/{}/inference_test/labels/ \
                    --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/k-fold_training_2/{}/inference_test/coverage/ --grid 10 "

eval_ss_instruction="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py \
         --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/k-fold_training_2/{}/inference_test/coverage/ \
         --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/kfold/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/kfold/labels/test/ \
         --run_name {} --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/k-fold_training_2/{}/inference_test/ --shape 1024"

#check get_im path



# temporary_dirs=[temp_imgs_train,temp_imgs_val,temp_labels_train,temp_labels_val]

# def create_empty_temp_dirs():
#     for temp_dir in temporary_dirs:
#         if not os.path.exists(temp_dir):
#             os.mkdir(temp_dir)
#         else:
#             shutil.rmtree(temp_dir)
#             os.mkdir(temp_dir)


# def create_empty_permanent_dirs():
#     for i in range(1,k+1):
#         for temp_dir in temporary_dirs:
#             if not os.path.exists(temp_dir+"_"+str(i)):
#                 os.mkdir(temp_dir+"_"+str(i))
#             else:
#                 print("THIS FOLDER ALREADY EXISTS!!")

# create_empty_temp_dirs()

# val_files_list=[]
# train_files_list=[]

# for i in range(1,k+1):
#     #1) K folds:
     
#     #Copy all files to tmp train and tmp val
#     for f in range(1,k+1): 
#         if f==i:
#             #copy val_files
#             #copy images
#             print("PATH: ",input_imgs_path+folds_dir+"/"+str(f)+"/*")
#             for img in glob.glob(input_imgs_path+folds_dir+"/"+str(f)+"/*"):
#                 shutil.copyfile(img, temp_imgs_val+"/"+img.split("/")[-1])
                
#                 val_files_list.append(img)
#             #copy labels
#             for img in glob.glob(input_labels_path+folds_dir+"/"+str(f)+"/*"):
#                 shutil.copyfile(img, temp_labels_val+"/"+img.split("/")[-1])
               
#         else:
#             #copy files to train partition        
#             for img in glob.glob(input_imgs_path+folds_dir+"/"+str(f)+"/*"):
#                 shutil.copyfile(img, temp_imgs_train+"/"+img.split("/")[-1])
#                 train_files_list.append(img)
#             #copy labels
#             for img in glob.glob(input_labels_path+folds_dir+"/"+str(f)+"/*"):
#                 shutil.copyfile(img, temp_labels_train+"/"+img.split("/")[-1])

#     print("train Files list len",len(train_files_list))
#     print("val Files list len",len(val_files_list))
#     train_files_list.extend(val_files_list)
#     print("Files list set len",len(set(train_files_list)))

#     val_files_list=[]
#     train_files_list=[]

#     # 2) Train and eval (eval comming with train):
#     T=training_instruction.format(str(i)) 
#     os.system(T)

#     #3) Inference:
#     I=inference_instruction.format(str(i),str(i)) 
#     os.system(I)

#     #3.1) Inference SS:
#     I=inference_instruction_SS.format(str(i),str(i)) 
#     os.system(I)

#     #4) Pascalvoc:
#     P=pascalvoc_instruction.format(str(i),str(i)) 
#     os.system(P)

#     #5) Coverage:
#     C=coverage_instruction.format(str(i),str(i)) 
#     os.system(C)

#     #6) Eval SS:
#     SS=eval_ss_instruction.format(str(i),str(i),str(i)) 
#     os.system(SS)

#     #7) Remove temporary directories and create new ones:
#     create_empty_temp_dirs()


# ---------------------------------END----------------------------------------------

# The following code is just a temporary fix:

# Missing evalss2 -> threshold sweep -> went wrong because of nans

missing_evals=["base_2","base_5","base_4","base_da_1","high3_da_2","high3_da_4","low27_1","low27_2","low27_3","low27_da_1","low3_4","low3_da_1","low3_da_2","low9_1","low9_3","low9_4"]

#Instruction:
command="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss2.py \
    --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/{}/inference_test_2/coverage2 \
    --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ \
    --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/hp/labels/test/ --run_name {} \
    --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/{}/inference_test_2 --shape 1024"

try:
    for folder in missing_evals:
        instr=command.format(folder,folder,folder)
        os.system(instr)

    # unify csv:
    unify_csv="python unify_xlsx.py --path_in projects/halimeda/final_trainings/yolo_XL/ --path_out projects/halimeda/final_trainings/yolo_XL/  --lookfor metrics.xlsx"
    os.system(unify_csv)

except Exception as e:
    print("you are fucked!", e)
