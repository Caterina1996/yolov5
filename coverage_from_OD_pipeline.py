

import os

# from od model calculate coverage inference and evaluate:

inference_instruction="python detect.py --weights /mnt/c/Users/haddo/yolov5/projects/halimeda/k-fold_training_2/3/weights/best.pt \
                    --project /mnt/c/Users/haddo/yolov5/projects/halimeda/k-fold_training_2/3/  --name inference_val/ --data data/halimeda_temp.yaml \
                    --source  /mnt/c/Users/haddo/yolov5/datasets/halimeda/kfold/images/temp_val/  --save-txt --save-conf --conf-thres 0.03 --line-thickness 1"


coverage_instruction="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 \
                    --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/k-fold_training_2/3/inference_val/labels/ \
                    --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/k-fold_training_2/3/inference_val/coverage/ --grid 10 "


eval_ss2_instruction="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss2.py \
                    --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/k-fold_training_2/3/inference_val/coverage/ \
                    --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/val/ --run_name fold_3_ss2_eval \
                    --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/k-fold_training_2/3/inference_val --shape 1024"

# os.system(inference_instruction)

os.system(coverage_instruction)

os.system(eval_ss2_instruction)