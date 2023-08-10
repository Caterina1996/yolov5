
import os 
import argparse
import shutil
import glob
# from clearml import Task
import time



k=5 #num folds
input_imgs_path="/mnt/c/Users/haddo/yolov5/datasets/halimeda/NEW_DATASET/images/"
input_labels_path="/mnt/c/Users/haddo/yolov5/datasets/halimeda/NEW_DATASET/labels/"
folds_dir=""

temp_imgs_train=input_imgs_path+"temp_train"
temp_imgs_val=input_imgs_path+"temp_val"

temp_labels_train=input_labels_path+"temp_train"
temp_labels_val=input_labels_path+"temp_val"


training_instruction="python train.py --img 1024 --batch 8 --epochs 200 --data halimeda_temp.yaml --weights {} --patience 60 \
                    --project /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_sizes/ --name {}  \
                    --single-cls --hyp data/hyps/final/hyp.low9_da.yaml"


inference_instruction_val="python detect.py --weights /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_sizes/{}/weights/best.pt \
                    --project /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_sizes/{}/  --name inference_val/ --data data/halimeda_temp.yaml \
                    --source  /mnt/c/Users/haddo/yolov5/datasets/halimeda/NEW_DATASET/images/temp_val/  --save-txt --save-conf --conf-thres 0.0 --line-thickness 1"

inference_instruction_test="python detect.py --weights /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_sizes/{}/weights/best.pt \
                    --project /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_sizes/{}/  --name inference_test/ --data data/halimeda_temp.yaml \
                    --source  /mnt/c/Users/haddo/yolov5/datasets/halimeda/NEW_DATASET/images/test/  --save-txt --save-conf --conf-thres 0.0 --line-thickness 1"


coverage_instruction_val="python /mnt/c/Users/haddo/DL_stack/object_detection_utils/metrics/coverage.py --shape 1024 \
                    --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_sizes/{}/inference_val/labels/ \
                    --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_sizes/{}/inference_val/coverage/ --grid 500 "

coverage_instruction_test="python /mnt/c/Users/haddo/DL_stack/object_detection_utils/metrics/coverage.py --shape 1024 \
                    --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_sizes/{}/inference_test/labels/ \
                    --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_sizes/{}/inference_test/coverage/ --grid 500 "


eval_instruction_val="python /mnt/c/Users/haddo/DL_stack/Halimeda/scripts/eval_one_thr.py --run_name {}  \
                    --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_sizes/{}/inference_val/coverage/ \
                    --out_path /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_sizes/{}/inference_val/ --thr 81  \
                    --gt_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/NEW_DATASET/labels/coverage/{}/ --shape 1024"

eval_instruction_test="python /mnt/c/Users/haddo/DL_stack/Halimeda/scripts/eval_one_thr.py --run_name {}  \
                    --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_sizes/{}/inference_test/coverage/ \
                    --out_path /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_sizes/{}/inference_test/ --thr 81  \
                    --gt_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/NEW_DATASET/labels/test_coverage/ --shape 1024"




#check get_im path
temporary_dirs=[temp_imgs_train,temp_imgs_val,temp_labels_train,temp_labels_val]

model_sizes={"yolo_nano":"yolov5n.pt","yolo_small":"yolov5s.pt","yolo_medium":"yolov5m.pt","yolo_large":"yolov5l.pt"}


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
for model in model_sizes.keys():
    
    for i in range(3,k+1):
        
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

        # python train.py --img 1024 --batch 8 --epochs 200 --data halimeda_temp.yaml --weights {} --patience 60 \
        #             --project /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_sizes/ --name {}  \
        #             --single-cls --hyp data/hyps/final/hyp.low9_da.yaml     
        #    
        training_folder=model+"/"+str(i)
        T=training_instruction.format(model_sizes[model],training_folder) 
        os.system(T)

        # python detect.py --weights /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_sizes/{}/weights/best.pt \
        #             --project /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_sizes/{}/  --name inference_val/ --data data/halimeda_temp.yaml \
        #             --source  /mnt/c/Users/haddo/yolov5/datasets/halimeda/NEW_DATASET/images/temp_val/  --save-txt --save-conf --conf-thres 0.0 --line-thickness 1"

        I=inference_instruction_val.format(training_folder,training_folder) 
        os.system(I)  
        I=inference_instruction_test.format(training_folder,training_folder) 
        os.system(I)  

        # python /mnt/c/Users/haddo/DL_stack/object_detection_utils/metrics/coverage.py --shape 1024 \
        #             --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_sizes/{}/inference_val/labels/ \
        #             --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_sizes/{}/inference_val/coverage/ --grid 500

        C=coverage_instruction_val.format(training_folder,training_folder) 
        os.system(C)  
        C=coverage_instruction_test.format(training_folder,training_folder) 
        os.system(C)  

        # python /mnt/c/Users/haddo/DL_stack/Halimeda/scripts/eval_one_thr.py --run_name {}  \
        #             --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_sizes/{}/inference_test/coverage/ \
        #             --out_path /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_sizes/{}/inference_test/ --thr 81  \
        #             --gt_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/NEW_DATASET/labels/coverage/{}/ --shape 1024

        C=eval_instruction_val.format(training_folder,training_folder,training_folder,str(i)) 
        os.system(C)  
        C=eval_instruction_test.format(training_folder,training_folder,training_folder) 
        os.system(C)  
        create_empty_temp_dirs()






# training_instruction="python train.py --img 1024 --batch 8 --epochs 200 --data halimeda_temp.yaml --weights yolov5n.pt --patience 60 \
#                     --project /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET --name yolo_nano  \
#                     --single-cls --hyp data/hyps/final/hyp.low9_da.yaml"

# inference_instruction="python detect.py --weights /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_nano/weights/best.pt \
#                     --project /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_nano/  --name inference_test/ --data data/halimeda_temp.yaml \
#                     --source  /mnt/c/Users/haddo/yolov5/datasets/halimeda/NEW_DATASET/images/test/  --save-txt --save-conf --conf-thres 0.0 --line-thickness 1"


# coverage_instruction="python /mnt/c/Users/haddo/DL_stack/object_detection_utils/metrics/coverage.py --shape 1024 \
#                     --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_nano/inference_test/labels/ \
#                     --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_nano/inference_test/coverage/ --grid 500 "


# eval_instruction="python /mnt/c/Users/haddo/DL_stack/Halimeda/scripts/eval_one_thr.py --run_name yolo_nano_inf_test  \
#                     --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_nano/inference_test/coverage/ \
#                     --out_path /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_nano/inference_test/ --thr 81  \
#                     --gt_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/NEW_DATASET/labels/test_coverage/ --shape 1024"

# os.system(training_instruction)
# os.system(inference_instruction)
# os.system(coverage_instruction)
# os.system(eval_instruction)


# #----------------

# training_instruction="python train.py --img 1024 --batch 8 --epochs 200 --data halimeda_temp.yaml --weights yolov5s.pt --patience 60 \
#                     --project /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET --name yolo_small  \
#                     --single-cls --hyp data/hyps/final/hyp.low9_da.yaml"

# inference_instruction="python detect.py --weights /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_small/weights/best.pt \
#                     --project /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_small/  --name inference_test/ --data data/halimeda_temp.yaml \
#                     --source  /mnt/c/Users/haddo/yolov5/datasets/halimeda/NEW_DATASET/images/test/  --save-txt --save-conf --conf-thres 0.0 --line-thickness 1"


# coverage_instruction="python /mnt/c/Users/haddo/DL_stack/object_detection_utils/metrics/coverage.py --shape 1024 \
#                     --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_small/inference_test/labels/ \
#                     --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_small/inference_test/coverage/ --grid 500 "


# eval_instruction="python /mnt/c/Users/haddo/DL_stack/Halimeda/scripts/eval_one_thr.py --run_name yolo_small_inf_test  \
#                     --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_small/inference_test/coverage/ \
#                     --out_path /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_small/inference_test/ --thr 81  \
#                     --gt_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/NEW_DATASET/labels/test_coverage/ --shape 1024"

# os.system(training_instruction)
# os.system(inference_instruction)
# os.system(coverage_instruction)
# os.system(eval_instruction)

# #----------------


# training_instruction="python train.py --img 1024 --batch 8 --epochs 200 --data halimeda_temp.yaml --weights yolov5m.pt --patience 60 \
#                     --project /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET --name yolo_medium  \
#                     --single-cls --hyp data/hyps/final/hyp.low9_da.yaml"

# inference_instruction="python detect.py --weights /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_medium/weights/best.pt \
#                     --project /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_medium/  --name inference_test/ --data data/halimeda_temp.yaml \
#                     --source  /mnt/c/Users/haddo/yolov5/datasets/halimeda/NEW_DATASET/images/test/  --save-txt --save-conf --conf-thres 0.0 --line-thickness 1"


# coverage_instruction="python /mnt/c/Users/haddo/DL_stack/object_detection_utils/metrics/coverage.py --shape 1024 \
#                     --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_medium/inference_test/labels/ \
#                     --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_medium/inference_test/coverage/ --grid 500 "


# eval_instruction="python /mnt/c/Users/haddo/DL_stack/Halimeda/scripts/eval_one_thr.py --run_name yolo_medium_inf_test  \
#                     --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_medium/inference_test/coverage/ \
#                     --out_path /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_medium/inference_test/ --thr 81  \
#                     --gt_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/NEW_DATASET/labels/test_coverage/ --shape 1024"

# os.system(training_instruction)
# os.system(inference_instruction)
# os.system(coverage_instruction)
# os.system(eval_instruction)

# #----------------

# training_instruction="python train.py --img 1024 --batch 8 --epochs 200 --data halimeda_temp.yaml --weights yolov5l.pt --patience 60 \
#                     --project /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET --name yolo_large  \
#                     --single-cls --hyp data/hyps/final/hyp.low9_da.yaml"

# inference_instruction="python detect.py --weights /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_large/weights/best.pt \
#                     --project /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_large/  --name inference_test/ --data data/halimeda_temp.yaml \
#                     --source  /mnt/c/Users/haddo/yolov5/datasets/halimeda/NEW_DATASET/images/test/  --save-txt --save-conf --conf-thres 0.0 --line-thickness 1"


# coverage_instruction="python /mnt/c/Users/haddo/DL_stack/object_detection_utils/metrics/coverage.py --shape 1024 \
#                     --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_large/inference_test/labels/ \
#                     --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_large/inference_test/coverage/ --grid 500 "


# eval_instruction="python /mnt/c/Users/haddo/DL_stack/Halimeda/scripts/eval_one_thr.py --run_name yolo_large_inf_test  \
#                     --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_large/inference_test/coverage/ \
#                     --out_path /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_large/inference_test/ --thr 81  \
#                     --gt_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/NEW_DATASET/labels/test_coverage/ --shape 1024"

# os.system(training_instruction)
# os.system(inference_instruction)
# os.system(coverage_instruction)
# os.system(eval_instruction)


# eval_instruction="python /mnt/c/Users/haddo/DL_stack/Halimeda/scripts/eval_one_thr.py --run_name yolo_XL_inf_test  \
#                     --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/low9_da/1/inference_test/coverage/ \
#                     --out_path /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/yolo_sizes/ --thr 81  \
#                     --gt_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/NEW_DATASET/labels/test_coverage/ --shape 1024"
