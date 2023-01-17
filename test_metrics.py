

import os
import glob


#folders=['/mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_X6/hyp_high_a', '/mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_X6/hyp_high_lr2_a', '/mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_X6/hyp_low_2_a', '/mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_X6/hyp_low_2_b', '/mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_X6/hyp_low_2_lr2_a', '/mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/hyp_high_a', '/mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/hyp_high_lr2_a', '/mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/hyp_low_2_a', '/mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/hyp_low_2_lr2_a']

gt_folder="/mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test"

dest_dir="/mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings"

inference_folder="/inference_test/labels/"

results_folder="/results/"

inference_instr="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 \
                -gtformat=xywh -detformat=xywh -gt " + gt_folder+ " -det {}  \
                -np -sp {} -gtcoords rel -detcoords rel -imgsize 1024,1024"

nms_instr="python /mnt/c/Users/haddo/object_detection_utils/metrics/lib/nms.py --path_in {} --path_out {} --thr 0.4"

training_folders=glob.glob(dest_dir+"/**/**")

for t_folder in training_folders:
    detections=t_folder+inference_folder
    results=t_folder+results_folder
    inf=inference_instr.format(detections,results)
    os.system(inf)
    nms=nms_instr.format(detections,detections+"/nms/")
    os.system(nms)
    inference=inference_instr.format(detections+"/nms/",results+"/nms/")
    os.system(inference)

#test 1 inference:




