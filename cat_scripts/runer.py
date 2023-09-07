
import os 

sizes_dict={"yolo_small":"yolov5s.pt","yolo_medium":"yolov5m.pt","yolo_large":"yolov5l.pt"}


training_instruction="python train.py --img 1024 --batch 8 --epochs 200 --data halimeda_temp.yaml --weights {}  \
                    --project /mnt/c/Users/haddo/yolov5/projects/halimeda/ --name {}  \
                    --single-cls --hyp data/hyps/final/hyp.low27_da.yaml --patience 20"


inference_instruction="python detect.py --weights /mnt/c/Users/haddo/yolov5/projects/halimeda/{}/weights/best.pt --imgsz 1024 \
                    --project /mnt/c/Users/haddo/yolov5/projects/halimeda/{}/  --name inference_test/ --data data/halimeda_temp.yaml \
                    --source  /mnt/c/Users/haddo/yolov5/datasets/halimeda/kfold/images/test  --save-txt --save-conf --conf-thres 0 --line-thickness 1"

pascalvoc_instruction="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py \
                    -tiou 0.5 -tconf 0 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh \
                    -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/kfold/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/{}/inference_test/labels/ \
                    -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/{}/pascalvoc/"


coverage_instruction="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 \
                    --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/{}/inference_test/labels/ \
                    --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/{}/inference_test/coverage/ --grid 10 "



eval_ss2_instruction="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss2.py \
                    --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/{}/inference_test/coverage/ \
                    --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ \
                    --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/kfold/labels/test \
                    --run_name {} --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/{}/inference_test --shape 1024"




for model_name,weights_path in sizes_dict.items():

    print("MODEL IS: ",model_name)
    os.system(training_instruction.format(weights_path,model_name))
    
    print("MODEL IS: ",model_name)
    os.system(inference_instruction.format(model_name,model_name))
    
    print("MODEL IS: ",model_name)
    os.system(pascalvoc_instruction.format(model_name,model_name))
    
    print("MODEL IS: ",model_name)
    os.system(coverage_instruction.format(model_name,model_name))
    
    print("MODEL IS: ",model_name)
    os.system(eval_ss2_instruction.format(model_name,model_name,model_name))