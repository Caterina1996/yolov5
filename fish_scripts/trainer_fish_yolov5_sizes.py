# from ultralytics import YOLO
import numpy as np
import matplotlib.pyplot as plt
import os
import glob
import shutil
from clearml import Task
from natsort import natsorted
import random
import time


path_to_calls="/mnt/c/Users/haddo/DL_stack/yolov5/projects/fish/"
path_to_project = "/mnt/c/Users/haddo/DL_stack/yolov5/projects/fish/test_sizes"
path_to_dataset = "/mnt/c/Users/haddo/DL_stack/yolov5/datasets/fish/PLOME_IS/"

tmp_suffixes = ["images/temp_train/", "labels/temp_train", "images/temp_val", "labels/temp_val"]

dataset_yaml = "/mnt/c/Users/haddo/DL_stack/yolov5/data/fish.yaml"

def create_empty_temp_dirs(base_path):
    print("Base path is:", base_path)
    for tmp_suffix in tmp_suffixes:
        tmp_dir = os.path.join(base_path, tmp_suffix)
        if not os.path.exists(tmp_dir):
            os.makedirs(tmp_dir)
        else:
            shutil.rmtree(tmp_dir)
            os.makedirs(tmp_dir)


ds_versions = [16]
do_train = True
folds_created = True
k = 5
seed=42
check_imgs_array,check_lbls_array=[],[]
random.seed(seed)

for v in ds_versions:

    if not folds_created:
        # PART 1: Create k-folds
        # 1.1 Create data_dict
        folders = ["train", "valid"]
        images, labels = [], []
        for folder in folders:
            images.extend(glob.glob(path_to_dataset + "/images/" + folder + "/**"))
            labels.extend(glob.glob(path_to_dataset +  "/labels/" + folder + "/**"))
            if len(images) != len(labels):
                print("WARNING!!!: THE NUMBER OF IMAGES AND LABELS DOES NOT MATCH")
                
        images = natsorted(images)
        labels = natsorted(labels)
        train_val_data = dict(zip(images, labels))

        # 1.2 Create folds
        
        for i in range(1, k+1):
            os.makedirs(path_to_dataset+ "/images/folds/" + str(i) , exist_ok=True)
            os.makedirs(path_to_dataset+ "/labels/folds/" + str(i) , exist_ok=True)

        # 1.3 Copy images and labels into folds
        init_idx = 0
        random.shuffle(images)
        final_idx = int(len(images) / k) + 1  # the last elem (b) is not included in [a:b] function
        print("\n num of train images is: ", len(images), "\n")
        print("idx is: ", final_idx, "\n")

        for i in range(1, k+1):
            print("Copying images to the ", i, "th fold")
            print(" init idx is: ", init_idx, "\n", "final idx is: ", final_idx, "\n")

            for sample in images[init_idx:final_idx]:
                shutil.copyfile(sample, path_to_dataset+ "/images/folds/" + str(i) +"/"+ sample.split("/")[-1])
                shutil.copyfile(train_val_data[sample], path_to_dataset+ "/labels/folds/" + str(i)+"/"+ train_val_data[sample].split("/")[-1])
                check_imgs_array.append(sample)
                check_lbls_array.append(train_val_data[sample],)

            init_idx = final_idx
            final_idx = final_idx + int(len(images) / k) + 1
            if i == k - 1:
                final_idx = len(images)

if len(set(list(check_imgs_array)))!=len(check_imgs_array) or len(set(list(check_lbls_array)))!=len(check_lbls_array):
    print(set(list(check_imgs_array)))
    print(set(list(check_lbls_array)))
    print("WARNING: SOMETHING HAS BEEN COPIED MORE THAN ONE TIMEEEE!!!!!!!!!!!!!!")

    print("condition1: ",len(set(list(check_imgs_array)))!=len(check_imgs_array))
    print("condition2: ",len(set(list(check_lbls_array)))!=len(check_lbls_array))

    

# FOLDS CREATED

if do_train:
    # 2 Instructions
    # train_instruction = "yolo segment train cfg={} data={} model={} epochs=200 imgsz=640 seed={}  lr0={} project={} name={}"
    # train_instruction = "yolo segment train data={} model={} epochs=200 imgsz=640 seed={}  lr0={} project={} name={} seed=42"
    # val_instruction = "yolo segment val data={} model={}  project={} name={} split=val"
    # test_instruction = "yolo segment val data={} model={} project={} name={} split=test"

    # lrs = [0.03, 0.01, 0.0033, 0.00011, 0.00037]
    lrs = [0]

    model_sizes = {
        "n": "nano",
        "s": "small",
        "m": "medium",
        "l": "large",
        "x": "extra_large"
    }


    # configs=["/mnt/c/Users/haddo/yolov8/ultralytics/yolo/cfg/da.yaml","/mnt/c/Users/haddo/yolov8/ultralytics/yolo/cfg/no_da.yaml"]
    batch_sizes=[8]

    k = 5  # num folds
    for batch in batch_sizes:
        # Tidy train-val splits from k-fold
                
        # create temp train and val (or empty them)
        create_empty_temp_dirs(path_to_dataset)

        folds_images_path=path_to_dataset+"/images/folds/"
        folds_labels_path=path_to_dataset+"/labels/folds/"
        # create the k fold iteration (here to avoid doing it every time)
        # # k fold 
        for i in range(5, k+1):
            create_empty_temp_dirs(path_to_dataset)
            for f in range(1, k+1):
                if f == i:
                    print("copying val images from: ", folds_images_path + "/" + str(f) + "/ to /temp_val/")
                    print("copying val labels from: ", folds_labels_path + "/" + str(f) + "/ to /temp_val/")
                    for img, lbl in zip(glob.glob(folds_images_path + "/" + str(f) + "/*"), glob.glob(folds_labels_path + "/" + str(f) + "/*")):
                        shutil.copyfile(img, path_to_dataset + "/images/temp_val/" + img.split("/")[-1])
                        shutil.copyfile(lbl, path_to_dataset + "/labels/temp_val/" + lbl.split("/")[-1])
                else:
                    print("copying val images from: ", folds_images_path + "/" + str(f) + "to /train/")
                    print("copying val labels from: ", folds_labels_path + "/" + str(f) + "to /train/")

                    for img, lbl in zip(glob.glob(folds_images_path + "/" + str(f) + "/*"), glob.glob(folds_labels_path + "/" + str(f) + "/*")):
                        shutil.copyfile(img, path_to_dataset + "/images/temp_train/" + img.split("/")[-1])
                        shutil.copyfile(lbl, path_to_dataset + "/labels/temp_train/" + lbl.split("/")[-1])

            
           
            for model_size in model_sizes.keys():
                project_name=path_to_project+"/"+model_sizes[model_size] +"/"  
                for lr in lrs:
                                        
                    run_name=os.path.join(project_name,"fold_"+str(i))
                    # run_name=os.path.join(project_name,"lr_"+str(lr))
                    
                    # instruction = f"python clearml_log_yolov5.py --project_name 'Pecesv5' --task_name {run_name} \
                    #     --model_size {model_size} --dataset {dataset_yaml} \
                    #         --epochs 300 --batch {batch} --patience 20 --yolo_proj {project_name} --yolo_name {run_name} \
                    #             --seed {seed}"
                    task = Task.init(
                        project_name='Pecesv5',
                        task_name=run_name,
                        output_uri=True # To upload the model and weights to ClearML.
                    )
                 
                    instruction=f"python ../segment/train.py --img 640 --batch 8 --epochs 300 --data {dataset_yaml} --weights yolov5{model_size}-seg.pt --patience 20 \
                    --project {project_name} --name {run_name} --seed 42 --device 0"

                    # instruction="python ../segment/train.py --img 1024 --batch 8 --epochs 200 --data fish.yaml \
                    #     --weights yolov5n-seg.pt --patience 20  --project /mnt/c/Users/haddo/yolov5/projects/fish/test_sizes --name nano --seed=42"
                    
                   
                    model_variant = f'YOLOv5{model_size}-seg'

                    # task.set_parameter('model_variant', model_variant)
                    # train_args =  dict(
                    #     data=dataset_yaml,
                    #     optimizer="SGD",
                    #     epochs=200,
                    #     patience=20,
                    #     batch=8,
                    #     project=project_name,
                    #     name=run_name,
                    #     seed=42
                    # )
                    # task.connect(train_args)
                    # task.connect_configuration(train_args['data'], 'Dataset yaml')     
                    # task = Task.init(project_name='Peces', task_name=run_name)
                    # task.set_parameter('model_variant', model_sizes[model_size])

                    os.system(instruction)

                    with open(path_to_calls+'/calls_peces_paper.txt', 'a+') as f:
                        f.write(instruction)
                        # f.write(test_instruction_formatted)
                        f.write("\n")
                        f.write("------------------------------------------------------------- \n")
                        f.write("\n")

                    print(instruction)
                    # Use the formatted instructions
                    
                    task.close()
                    time.sleep(300)

