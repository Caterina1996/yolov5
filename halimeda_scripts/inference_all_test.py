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

eval_instruction="python /mnt/c/Users/haddo/DL_stack/Halimeda/scripts/eval_one_thr.py --run_name low_9_da_1_inf_OD_test_thr_81  \
                    --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/low9_da/1/inference_test/coverage/ \
                    --out_path /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/low9_da/1/inference_test/ --thr 81  \
                    --gt_path nt/c/Users/haddo/yolov5/datasets/halimeda/NEW_DATASET/labels/test_coverage --shape 1024" 



inference_instruction="python detect.py --weights /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/low9_da/1/weights/best.pt \
                    --project /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/low9_da/1/  --name inference_all_test/  \
                    --source  /mnt/c/Users/haddo/DL_stack/Halimeda/dataset/NEW_DATASET/all_test/images/  --save-txt --save-conf --conf-thres 0.0 --line-thickness 1"


coverage_instruction="python /mnt/c/Users/haddo/DL_stack/object_detection_utils/metrics/coverage.py --shape 1024 \
                    --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/low9_da/1/inference_all_test/labels/ \
                    --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/low9_da/1/inference_all_test/coverage/ --grid 500 "


eval_instruction="python /mnt/c/Users/haddo/DL_stack/Halimeda/scripts/eval_one_thr.py --run_name low_9_da_1_inf_all_test_thr_81  \
                    --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/low9_da/1/inference_all_test/coverage/ \
                    --out_path /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/low9_da/1/inference_all_test/ --thr 81  \
                    --gt_path /mnt/c/Users/haddo/DL_stack/Halimeda/dataset/NEW_DATASET/all_test/gt/ --shape 1024"  


""" 


python detect.py --weights /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/low9_da/1/weights/best.pt \
                    --project /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/low9_da/1/  --name inference_SS_val/  \
                    --source  /mnt/c/Users/haddo/DL_stack/Halimeda/dataset/NEW_DATASET/all_test/images/  --save-txt --save-conf --conf-thres 0.0 --line-thickness 1"



"""



os.system(inference_instruction)    

os.system(coverage_instruction)

os.system(eval_instruction)



inference_instruction="python detect.py --weights /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/low9_da/1/weights/best.pt \
                    --project /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/low9_da/1/  --name inference_SS_val/  \
                    --source  /mnt/c/Users/haddo/DL_stack/Halimeda/dataset/NEW_DATASET/SS/sets/val_best_model/images/  --save-txt --save-conf --conf-thres 0.0 --line-thickness 1"




#INFERENCE SS MIKI


eval_ss2_instruction="python /mnt/c/Users/haddo/DL_stack/object_detection_utils/metrics/eval_ss2.py \
                    --pred_path /mnt/c/Users/haddo/SS_Halimeda/cat/000033/inference_val/ \
                    --gt_im_path  /mnt/c/Users/haddo/SS_Halimeda/cat/5/val/mask/  \
                    --run_name best_SS_over_val5_cat --save_path /mnt/c/Users/haddo/SS_Halimeda/cat/metrics_cat/ --shape 1024"


I="python eval_one_thr.py --run_name best_SS_over_OD_cat  --pred_path /mnt/c/Users/haddo/SS_Halimeda/cat/000033/inference_od/ \
                                                    --out_path /mnt/c/Users/haddo/SS_Halimeda/cat/metrics_cat/ --thr 123  \
                                                    --gt_path  /mnt/c/Users/haddo/SS_Halimeda/cat/test_od/mask/ --shape 1024  "


I="python eval_one_thr.py --run_name best_SS_over_SS_test_cat  --pred_path /mnt/c/Users/haddo/SS_Halimeda/cat/000033/inference_test/ \
                                                    --out_path /mnt/c/Users/haddo/SS_Halimeda/cat/metrics_cat/ --thr 123  \
                                                    --gt_path /mnt/c/Users/haddo/SS_Halimeda/cat/test_ss/mask/ --shape 1024  "


I="python eval_one_thr.py --run_name best_SS_over_all_cat  --pred_path /mnt/c/Users/haddo/SS_Halimeda/cat/000033/inference_all/ \
                                                    --out_path /mnt/c/Users/haddo/SS_Halimeda/cat/metrics_cat/ --thr 123  \
                                                    --gt_path /mnt/c/Users/haddo/SS_Halimeda/cat/test_all/mask/ --shape 1024  "


I="python eval_one_thr.py --run_name best_SS_over_OD_cat  --pred_path /mnt/c/Users/haddo/SS_Halimeda/cat/000033/inference_od/ \
                                                    --out_path /mnt/c/Users/haddo/SS_Halimeda/cat/metrics_cat/ --thr 123  \
                                                    --gt_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/NEW_DATASET/labels/test_coverage/ --shape 1024  "


#-----------------------------

"""

python detect.py --weights /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/low9_da/1/weights/best.pt \
                    --project /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/low9_da/1/  --name inference_SS_val5/  \
                    --source  /mnt/c/Users/haddo/SS_Halimeda/cat/5/val/img/  --save-txt --save-conf --conf-thres 0.0 --line-thickness 1

python od_in_ss.py --path_od /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/low9_da/1/inference_SS_val5/labels \
                    --path_ss_gt /mnt/c/Users/haddo/SS_Halimeda/cat/5/val/mask/ \
                    --path_out /mnt/c/Users/haddo/DL_stack/Halimeda/dataset/NEW_DATASET


python /mnt/c/Users/haddo/DL_stack/object_detection_utils/metrics/coverage.py --shape 1024 \
                    --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/low9_da/1/inference_SS_val5/labels \
                    --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/NEW_DATASET/low9_da/1/inference_SS_val5/coverage/ --grid 500 


python merge_outs.py --path_od /mnt/c/Users/haddo/DL_stack/Halimeda/dataset/NEW_DATASET/INFERENCE_best_models/OD_over_all_val \
                    --path_ss /mnt/c/Users/haddo/DL_stack/Halimeda/dataset/NEW_DATASET/INFERENCE_best_models/SS_over_all_val \
                    --path_merge /mnt/c/Users/haddo/DL_stack/Halimeda/combined_model/inference_test/combined_weights_swp/


"""
