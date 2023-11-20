import os 
import argparse
import shutil
import glob

# from comet_ml import Experiment

# Create an experiment with your api key
# experiment = Experiment(
#     api_key="g1hZLRyJgRN8tIfc25oDC3ACG",
#     project_name="halimeda",
#     workspace="caterina1996",
# )

training_instruction_1="python train.py --img 1024 --batch 8 --epochs 200 --data halimeda.yaml --weights yolov8l.pt  \
                    --project /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_8 --name hyp_low_2  \
                    --single-cls --hyp data/hyps/hyp.scratch-low_2.yaml "

training_instruction_1="python train.py --img 1024 --batch 8 --epochs 200 --data halimeda.yaml --weights yolov5x6.pt  \
                    --project /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_X6/ --name hyp_low_2  \
                    --single-cls --hyp data/hyps/hyp.scratch-low_2.yaml --save-period 10 "

inference_instruction_1="python detect.py --weights /mnt/c/Users/haddo/yolov5/projects/halimeda/yolo_X6/hyp_med_2/weights/best.pt \
                    --project /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_X6/hyp_low_2/  --name inference_test/ --data data/halimeda.yaml \
                    --source  /mnt/c/Users/haddo/yolov5/datasets/halimeda/images/test --save-txt" 

# ---------------------------------------------------------------------------------------------------------------------
training_instruction_2="python train.py --img 1024 --batch 8 --epochs 200 --data halimeda.yaml --weights yolov5x6.pt  \
                    --project /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_X6/hyp_low_2/ --name hyp_low_2  \
                    --single-cls --hyp data/hyps/hyp.scratch-low_2_lr2.yaml --save-period 10 "

inference_instruction_2="python detect.py --weights /mnt/c/Users/haddo/yolov5/projects/halimeda/yolo_X6/hyp_med_2/weights/best.pt \
                    --project /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_X6/  --name inference_test/ --data data/halimeda.yaml \
                    --source  /mnt/c/Users/haddo/yolov5/datasets/halimeda/images/test --save-txt" 


training_instruction_3="python train.py --img 1024 --batch 8 --epochs 200 --data halimeda.yaml --weights yolov5x6.pt  \
                    --project /mnt/c/Users/haddo/yolov5/projects/halimeda/yolo_X6/ --name hyp_high_2 \
                    --single-cls --hyp data/hyps/hyp.scratch-med_2.yaml --save-period 10 "

inference_instruction_3="python detect.py --weights /mnt/c/Users/haddo/yolov5/projects/halimeda/yolo_X6/hyp_high_2/weights/best.pt \
                    --project /mnt/c/Users/haddo/yolov5/projects/halimeda/yolo_X6/hyp_high_2/  --name inference_test/ --data data/halimeda.yaml \
                    --source  /mnt/c/Users/haddo/yolov5/datasets/halimeda/images/test"

inference_instruction_33="python detect.py --weights /mnt/c/Users/haddo/yolov5/projects/halimeda/yolo_X6/hyp_high_2/weights/best.pt \
                    --project /mnt/c/Users/haddo/yolov5/projects/halimeda/yolo_X6/hyp_high_2/  --name inference_web/ --data data/halimeda.yaml \
                    --source  /mnt/c/Users/haddo/yolov5/datasets/halimeda/images/from_web"



training_instruction_4="python train.py --img 1024 --batch 8 --epochs 200 --data halimeda.yaml --weights yolov5x6.pt  \
                    --project /mnt/c/Users/haddo/yolov5/projects/halimeda/yolo_X6/ --name hyp_high_2_lr2  \
                    --single-cls --hyp data/hyps/hyp.scratch-high_2_lr2.yaml --save-period 10 "

inference_instruction_4="python detect.py --weights /mnt/c/Users/haddo/yolov5/projects/halimeda/yolo_X6/hyp_high_2_lr2/weights/best.pt \
                    --project /mnt/c/Users/haddo/yolov5/projects/halimeda/yolo_X6/hyp_high_2_lr2/  --name inference_test/ --data data/halimeda.yaml \
                    --source  /mnt/c/Users/haddo/yolov5/datasets/halimeda/images/test"

inference_instruction_44="python detect.py --weights /mnt/c/Users/haddo/yolov5/projects/halimeda/yolo_X6/hyp_high_2_lr2/weights/best.pt \
                    --project /mnt/c/Users/haddo/yolov5/projects/halimeda/yolo_X6/hyp_high_2_lr2/  --name inference_web/ --data data/halimeda.yaml \
                    --source  /mnt/c/Users/haddo/yolov5/datasets/halimeda/images/from_web"




# T=training_instruction.format(str(i)) 
# os.system(training_instruction_1)
# os.system(inference_instruction_1)
# os.system(inference_instruction_11)

os.system(training_instruction_2)
os.system(inference_instruction_2)


os.system(training_instruction_3)
os.system(inference_instruction_3)


os.system(training_instruction_4)
os.system(inference_instruction_4)
