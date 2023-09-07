import os



coverage_instruction="python /mnt/c/Users/haddo/DL_stack/object_detection_utils/metrics/coverage.py --shape 1024 \
                    --path_txt /mnt/c/Users/haddo/yolov5/datasets/halimeda/NEW_DATASET/labels/train_val_splits/{}/ \
                    --path_out /mnt/c/Users/haddo/yolov5/datasets/halimeda/NEW_DATASET/labels/coverage/{}/ --grid 500 "

for i in range(1,6):
    I=coverage_instruction.format(str(i),str(i)) 
    os.system(I)



