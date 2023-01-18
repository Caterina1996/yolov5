import os 

training_1="python detect.py --weights projects/halimeda/final_trainings/yolo_X6/hyp_low_2_a/weights/best.pt --project projects/halimeda/final_trainings/yolo_X6/hyp_low_2_a/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
os.system(training_1)
training_1="python detect.py --weights projects/halimeda/final_trainings/yolo_X6/hyp_low_2_lr2_a/weights/best.pt --project projects/halimeda/final_trainings/yolo_X6/hyp_low_2_lr2_a/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
os.system(training_1)
training_1="python detect.py --weights projects/halimeda/final_trainings/yolo_X6/hyp_high_a/weights/best.pt --project projects/halimeda/final_trainings/yolo_X6/hyp_high_a/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
os.system(training_1)
training_1="python detect.py --weights projects/halimeda/final_trainings/yolo_X6/hyp_high_lr2_a/weights/best.pt --project projects/halimeda/final_trainings/yolo_X6/hyp_high_lr2_a/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
os.system(training_1)
training_1="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/hyp_low_2_a/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/hyp_low_2_a/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
os.system(training_1)
training_1="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/hyp_low_2_lr2_a/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/hyp_low_2_lr2_a/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
os.system(training_1)
training_1="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/hyp_high_a/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/hyp_high_a/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
os.system(training_1)
training_1="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/hyp_high_lr2_a/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/hyp_high_lr2_a/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
os.system(training_1)


training_1="python train.py --img 1024 --batch 8 --epochs 200 --data halimeda.yaml --weights yolov5x6.pt --project projects/halimeda/final_trainings/yolo_X6/ --name hyp_low_2_b --single-cls --hyp data/hyps/hyp.scratch-low_2.yaml"
os.system(training_1)
training_1="python train.py --img 1024 --batch 8 --epochs 200 --data halimeda.yaml --weights yolov5x6.pt --project projects/halimeda/final_trainings/yolo_X6/ --name hyp_low_2_lr2_b --single-cls --hyp data/hyps/hyp.scratch-low_2_lr2.yaml"
os.system(training_1)
training_1="python train.py --img 1024 --batch 8 --epochs 200 --data halimeda.yaml --weights yolov5x6.pt --project projects/halimeda/final_trainings/yolo_X6/ --name hyp_high_b --single-cls --hyp data/hyps/hyp.scratch-high.yaml"
os.system(training_1)
training_1="python train.py --img 1024 --batch 8 --epochs 200 --data halimeda.yaml --weights yolov5x6.pt --project projects/halimeda/final_trainings/yolo_X6/ --name hyp_high_lr2_b --single-cls --hyp data/hyps/hyp.scratch-high_lr2.yaml"
os.system(training_1)
training_1="python train.py --img 1024 --batch 8 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name hyp_low_2_b --single-cls --hyp data/hyps/hyp.scratch-low_2.yaml"
os.system(training_1)
training_1="python train.py --img 1024 --batch 8 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name hyp_low_2_lr2_b --single-cls --hyp data/hyps/hyp.scratch-low_2_lr2.yaml"
os.system(training_1)
training_1="python train.py --img 1024 --batch 8 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name hyp_high_b --single-cls --hyp data/hyps/hyp.scratch-high.yaml"
os.system(training_1)
training_1="python train.py --img 1024 --batch 8 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name hyp_high_lr2_b --single-cls --hyp data/hyps/hyp.scratch-high_lr2.yaml"
os.system(training_1)


training_1="python detect.py --weights projects/halimeda/final_trainings/yolo_X6/hyp_low_2_b/weights/best.pt --project projects/halimeda/final_trainings/yolo_X6/hyp_low_2_b/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
os.system(training_1)
training_1="python detect.py --weights projects/halimeda/final_trainings/yolo_X6/hyp_low_2_lr2_b/weights/best.pt --project projects/halimeda/final_trainings/yolo_X6/hyp_low_2_lr2_b/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
os.system(training_1)
training_1="python detect.py --weights projects/halimeda/final_trainings/yolo_X6/hyp_high_b/weights/best.pt --project projects/halimeda/final_trainings/yolo_X6/hyp_high_b/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
os.system(training_1)
training_1="python detect.py --weights projects/halimeda/final_trainings/yolo_X6/hyp_high_lr2_b/weights/best.pt --project projects/halimeda/final_trainings/yolo_X6/hyp_high_lr2_b/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
os.system(training_1)
training_1="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/hyp_low_2_b/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/hyp_low_2_b/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
os.system(training_1)
training_1="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/hyp_low_2_lr2_b/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/hyp_low_2_lr2_b/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
os.system(training_1)
training_1="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/hyp_high_b/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/hyp_high_b/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
os.system(training_1)
training_1="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/hyp_high_lr2_b/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/hyp_high_lr2_b/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
os.system(training_1)
