import os 

# # ------ TRAIN ------

# # ------ 1 ------
# command01="python train.py --img 1024 --batch 8 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name base_1  --single-cls --hyp data/hyps/final/hyp.base.yaml"
# command02="python train.py --img 1024 --batch 8 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name base_da_1  --single-cls --hyp data/hyps/final/hyp.base_da.yaml"
# command03="python train.py --img 1024 --batch 8 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name high3_1  --single-cls --hyp data/hyps/final/hyp.high3.yaml"
# command04="python train.py --img 1024 --batch 8 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name high3_da_1  --single-cls --hyp data/hyps/final/hyp.high3_da.yaml"
# command05="python train.py --img 1024 --batch 8 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name low3_1  --single-cls --hyp data/hyps/final/hyp.low3.yaml"
# command06="python train.py --img 1024 --batch 8 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name low3_da_1  --single-cls --hyp data/hyps/final/hyp.low3_da.yaml"
# command07="python train.py --img 1024 --batch 8 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name low9_1  --single-cls --hyp data/hyps/final/hyp.low9.yaml"
# command08="python train.py --img 1024 --batch 8 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name low9_da_1  --single-cls --hyp data/hyps/final/hyp.low9_da.yaml"
# command09="python train.py --img 1024 --batch 8 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name low27_1  --single-cls --hyp data/hyps/final/hyp.low27.yaml"
# command10="python train.py --img 1024 --batch 8 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name low27_da_1  --single-cls --hyp data/hyps/final/hyp.low27_da.yaml"
# os.system(command01)
# os.system(command02)
# os.system(command03)
# os.system(command04)
# os.system(command05)
# os.system(command06)
# os.system(command07)
# os.system(command08)
# os.system(command09)
# os.system(command10)


# # ------ 2 ------
# command01="python train.py --img 1024 --batch 8 --seed 2 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name base_2 --single-cls --hyp data/hyps/final/hyp.base.yaml"
# command02="python train.py --img 1024 --batch 8 --seed 2 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name base_da_2 --single-cls --hyp data/hyps/final/hyp.base_da.yaml"
# command03="python train.py --img 1024 --batch 8 --seed 2 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name high3_2 --single-cls --hyp data/hyps/final/hyp.high3.yaml"
# command04="python train.py --img 1024 --batch 8 --seed 2 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name high3_da_2 --single-cls --hyp data/hyps/final/hyp.high3_da.yaml"
# command05="python train.py --img 1024 --batch 8 --seed 2 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name low3_2 --single-cls --hyp data/hyps/final/hyp.low3.yaml"
# command06="python train.py --img 1024 --batch 8 --seed 2 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name low3_da_2 --single-cls --hyp data/hyps/final/hyp.low3_da.yaml"
# command07="python train.py --img 1024 --batch 8 --seed 2 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name low9_2 --single-cls --hyp data/hyps/final/hyp.low9.yaml"
# command08="python train.py --img 1024 --batch 8 --seed 2 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name low9_da_2 --single-cls --hyp data/hyps/final/hyp.low9_da.yaml"
# command09="python train.py --img 1024 --batch 8 --seed 2 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name low27_2 --single-cls --hyp data/hyps/final/hyp.low27.yaml"
# command10="python train.py --img 1024 --batch 8 --seed 2 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name low27_da_2 --single-cls --hyp data/hyps/final/hyp.low27_da.yaml"
# os.system(command01)
# os.system(command02)
# os.system(command03)
# os.system(command04)
# os.system(command05)
# os.system(command06)
# os.system(command07)
# os.system(command08)
# os.system(command09)
# os.system(command10)

# # ------ 3 ------
# command01="python train.py --img 1024 --batch 8 --seed 3 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name base_3 --single-cls --hyp data/hyps/final/hyp.base.yaml"
# command02="python train.py --img 1024 --batch 8 --seed 3 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name base_da_3 --single-cls --hyp data/hyps/final/hyp.base_da.yaml"
# command03="python train.py --img 1024 --batch 8 --seed 3 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name high3_3 --single-cls --hyp data/hyps/final/hyp.high3.yaml"
# command04="python train.py --img 1024 --batch 8 --seed 3 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name high3_da_3 --single-cls --hyp data/hyps/final/hyp.high3_da.yaml"
# command05="python train.py --img 1024 --batch 8 --seed 3 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name low3_3 --single-cls --hyp data/hyps/final/hyp.low3.yaml"
# command06="python train.py --img 1024 --batch 8 --seed 3 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name low3_da_3 --single-cls --hyp data/hyps/final/hyp.low3_da.yaml"
# command07="python train.py --img 1024 --batch 8 --seed 3 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name low9_3 --single-cls --hyp data/hyps/final/hyp.low9.yaml"
# command08="python train.py --img 1024 --batch 8 --seed 3 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name low9_da_3 --single-cls --hyp data/hyps/final/hyp.low9_da.yaml"
# command09="python train.py --img 1024 --batch 8 --seed 3 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name low27_3 --single-cls --hyp data/hyps/final/hyp.low27.yaml"
# command10="python train.py --img 1024 --batch 8 --seed 3 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name low27_da_3 --single-cls --hyp data/hyps/final/hyp.low27_da.yaml"
# os.system(command01)
# os.system(command02)
# os.system(command03)
# os.system(command04)
# os.system(command05)
# os.system(command06)
# os.system(command07)
# os.system(command08)
# os.system(command09)
# os.system(command10)

# # ------ 4 ------
# command01="python train.py --img 1024 --batch 8 --seed 4 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name base_4 --single-cls --hyp data/hyps/final/hyp.base.yaml"
# command02="python train.py --img 1024 --batch 8 --seed 4 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name base_da_4 --single-cls --hyp data/hyps/final/hyp.base_da.yaml"
# command03="python train.py --img 1024 --batch 8 --seed 4 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name high3_4 --single-cls --hyp data/hyps/final/hyp.high3.yaml"
# command04="python train.py --img 1024 --batch 8 --seed 4 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name high3_da_4 --single-cls --hyp data/hyps/final/hyp.high3_da.yaml"
# command05="python train.py --img 1024 --batch 8 --seed 4 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name low3_4 --single-cls --hyp data/hyps/final/hyp.low3.yaml"
# command06="python train.py --img 1024 --batch 8 --seed 4 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name low3_da_4 --single-cls --hyp data/hyps/final/hyp.low3_da.yaml"
# command07="python train.py --img 1024 --batch 8 --seed 4 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name low9_4 --single-cls --hyp data/hyps/final/hyp.low9.yaml"
# command08="python train.py --img 1024 --batch 8 --seed 4 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name low9_da_4 --single-cls --hyp data/hyps/final/hyp.low9_da.yaml"
# command09="python train.py --img 1024 --batch 8 --seed 4 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name low27_4 --single-cls --hyp data/hyps/final/hyp.low27.yaml"
# command10="python train.py --img 1024 --batch 8 --seed 4 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name low27_da_4 --single-cls --hyp data/hyps/final/hyp.low27_da.yaml"
# os.system(command01)
# os.system(command02)
# os.system(command03)
# os.system(command04)
# os.system(command05)
# os.system(command06)
# os.system(command07)
# os.system(command08)
# os.system(command09)
# os.system(command10)

# # ------ 5 ------
# command01="python train.py --img 1024 --batch 8 --seed 5 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name base_5 --single-cls --hyp data/hyps/final/hyp.base.yaml"
# command02="python train.py --img 1024 --batch 8 --seed 5 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name base_da_5 --single-cls --hyp data/hyps/final/hyp.base_da.yaml"
# command03="python train.py --img 1024 --batch 8 --seed 5 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name high3_5 --single-cls --hyp data/hyps/final/hyp.high3.yaml"
# command04="python train.py --img 1024 --batch 8 --seed 5 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name high3_da_5 --single-cls --hyp data/hyps/final/hyp.high3_da.yaml"
# command05="python train.py --img 1024 --batch 8 --seed 5 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name low3_5 --single-cls --hyp data/hyps/final/hyp.low3.yaml"
# command06="python train.py --img 1024 --batch 8 --seed 5 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name low3_da_5 --single-cls --hyp data/hyps/final/hyp.low3_da.yaml"
# command07="python train.py --img 1024 --batch 8 --seed 5 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name low9_5 --single-cls --hyp data/hyps/final/hyp.low9.yaml"
# command08="python train.py --img 1024 --batch 8 --seed 5 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name low9_da_5 --single-cls --hyp data/hyps/final/hyp.low9_da.yaml"
# command09="python train.py --img 1024 --batch 8 --seed 5 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name low27_5 --single-cls --hyp data/hyps/final/hyp.low27.yaml"
# command10="python train.py --img 1024 --batch 8 --seed 5 --epochs 200 --data halimeda.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/yolo_XL/ --name low27_da_5 --single-cls --hyp data/hyps/final/hyp.low27_da.yaml"
# os.system(command01)
# os.system(command02)
# os.system(command03)
# os.system(command04)
# os.system(command05)
# os.system(command06)
# os.system(command07)
# os.system(command08)
# os.system(command09)
# os.system(command10)


# # ------ INFERENCE ------

# # ------ 1 ------
# command01="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/base_1/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/base_1/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command02="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/base_da_1/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/base_da_1/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command03="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/high3_1/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/high3_1/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command04="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/high3_da_1/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/high3_da_1/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command05="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/low3_1/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/low3_1/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command06="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/low3_da_1/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/low3_da_1/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command07="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/low9_1/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/low9_1/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command08="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/low9_da_1/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/low9_da_1/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command09="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/low27_1/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/low27_1/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command10="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/low27_da_1/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/low27_da_1/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# os.system(command01)
# os.system(command02)
# os.system(command03)
# os.system(command04)
# os.system(command05)
# os.system(command06)
# os.system(command07)
# os.system(command08)
# os.system(command09)
# os.system(command10)

# # ------ 2 ------
# command01="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/base_2/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/base_2/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command02="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/base_da_2/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/base_da_2/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command03="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/high3_2/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/high3_2/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command04="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/high3_da_2/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/high3_da_2/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command05="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/low3_2/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/low3_2/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command06="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/low3_da_2/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/low3_da_2/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command07="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/low9_2/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/low9_2/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command08="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/low9_da_2/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/low9_da_2/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command09="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/low27_2/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/low27_2/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command10="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/low27_da_2/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/low27_da_2/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# os.system(command01)
# os.system(command02)
# os.system(command03)
# os.system(command04)
# os.system(command05)
# os.system(command06)
# os.system(command07)
# os.system(command08)
# os.system(command09)
# os.system(command10)

# # ------ 3 ------
# command01="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/base_3/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/base_3/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command02="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/base_da_3/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/base_da_3/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command03="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/high3_3/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/high3_3/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command04="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/high3_da_3/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/high3_da_3/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command05="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/low3_3/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/low3_3/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command06="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/low3_da_3/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/low3_da_3/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command07="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/low9_3/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/low9_3/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command08="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/low9_da_3/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/low9_da_3/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command09="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/low27_3/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/low27_3/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command10="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/low27_da_3/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/low27_da_3/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# os.system(command01)
# os.system(command02)
# os.system(command03)
# os.system(command04)
# os.system(command05)
# os.system(command06)
# os.system(command07)
# os.system(command08)
# os.system(command09)
# os.system(command10)

# # ------ 4 ------
# command01="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/base_4/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/base_4/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command02="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/base_da_4/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/base_da_4/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command03="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/high3_4/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/high3_4/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command04="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/high3_da_4/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/high3_da_4/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command05="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/low3_4/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/low3_4/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command06="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/low3_da_4/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/low3_da_4/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command07="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/low9_4/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/low9_4/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command08="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/low9_da_4/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/low9_da_4/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command09="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/low27_4/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/low27_4/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command10="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/low27_da_4/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/low27_da_4/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# os.system(command01)
# os.system(command02)
# os.system(command03)
# os.system(command04)
# os.system(command05)
# os.system(command06)
# os.system(command07)
# os.system(command08)
# os.system(command09)
# os.system(command10)

# # ------ 5 ------
# command01="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/base_5/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/base_5/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command02="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/base_da_5/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/base_da_5/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command03="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/high3_5/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/high3_5/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command04="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/high3_da_5/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/high3_da_5/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command05="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/low3_5/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/low3_5/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command06="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/low3_da_5/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/low3_da_5/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command07="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/low9_5/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/low9_5/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command08="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/low9_da_5/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/low9_da_5/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command09="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/low27_5/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/low27_5/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command10="python detect.py --weights projects/halimeda/final_trainings/yolo_XL/low27_da_5/weights/best.pt --project projects/halimeda/final_trainings/yolo_XL/low27_da_5/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# os.system(command01)
# os.system(command02)
# os.system(command03)
# os.system(command04)
# os.system(command05)
# os.system(command06)
# os.system(command07)
# os.system(command08)
# os.system(command09)
# os.system(command10)



# # ------ EVAL OD ------

# # ------ 1 ------
# command01="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_1/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_1/pascalvoc/"
# command02="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_da_1/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_da_1/pascalvoc/"
# command03="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_1/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_1/pascalvoc/"
# command04="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_da_1/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_da_1/pascalvoc/"
# command05="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_1/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_1/pascalvoc/"
# command06="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_da_1/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_da_1/pascalvoc/"
# command07="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_1/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_1/pascalvoc/"
# command08="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_da_1/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_da_1/pascalvoc/"
# command09="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_1/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_1/pascalvoc/"
# command10="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_da_1/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_da_1/pascalvoc/"
# os.system(command01)
# os.system(command02)
# os.system(command03)
# os.system(command04)
# os.system(command05)
# os.system(command06)
# os.system(command07)
# os.system(command08)
# os.system(command09)
# os.system(command10)

# # ------ 2 ------
# command01="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_2/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_2/pascalvoc/"
# command02="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_da_2/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_da_2/pascalvoc/"
# command03="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_2/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_2/pascalvoc/"
# command04="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_da_2/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_da_2/pascalvoc/"
# command05="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_2/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_2/pascalvoc/"
# command06="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_da_2/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_da_2/pascalvoc/"
# command07="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_2/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_2/pascalvoc/"
# command08="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_da_2/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_da_2/pascalvoc/"
# command09="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_2/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_2/pascalvoc/"
# command10="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_da_2/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_da_2/pascalvoc/"
# os.system(command01)
# os.system(command02)
# os.system(command03)
# os.system(command04)
# os.system(command05)
# os.system(command06)
# os.system(command07)
# os.system(command08)
# os.system(command09)
# os.system(command10)

# # ------ 3 ------
# command01="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_3/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_3/pascalvoc/"
# command02="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_da_3/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_da_3/pascalvoc/"
# command03="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_3/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_3/pascalvoc/"
# command04="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_da_3/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_da_3/pascalvoc/"
# command05="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_3/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_3/pascalvoc/"
# command06="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_da_3/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_da_3/pascalvoc/"
# command07="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_3/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_3/pascalvoc/"
# command08="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_da_3/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_da_3/pascalvoc/"
# command09="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_3/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_3/pascalvoc/"
# command10="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_da_3/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_da_3/pascalvoc/"
# os.system(command01)
# os.system(command02)
# os.system(command03)
# os.system(command04)
# os.system(command05)
# os.system(command06)
# os.system(command07)
# os.system(command08)
# os.system(command09)
# os.system(command10)

# # ------ 4 ------
# command01="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_4/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_4/pascalvoc/"
# command02="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_da_4/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_da_4/pascalvoc/"
# command03="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_4/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_4/pascalvoc/"
# command04="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_da_4/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_da_4/pascalvoc/"
# command05="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_4/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_4/pascalvoc/"
# command06="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_da_4/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_da_4/pascalvoc/"
# command07="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_4/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_4/pascalvoc/"
# command08="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_da_4/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_da_4/pascalvoc/"
# command09="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_4/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_4/pascalvoc/"
# command10="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_da_4/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_da_4/pascalvoc/"
# os.system(command01)
# os.system(command02)
# os.system(command03)
# os.system(command04)
# os.system(command05)
# os.system(command06)
# os.system(command07)
# os.system(command08)
# os.system(command09)
# os.system(command10)

# # ------ 5 ------
# command01="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_5/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_5/pascalvoc/"
# command02="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_da_5/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_da_5/pascalvoc/"
# command03="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_5/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_5/pascalvoc/"
# command04="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_da_5/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_da_5/pascalvoc/"
# command05="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_5/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_5/pascalvoc/"
# command06="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_da_5/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_da_5/pascalvoc/"
# command07="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_5/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_5/pascalvoc/"
# command08="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_da_5/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_da_5/pascalvoc/"
# command09="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_5/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_5/pascalvoc/"
# command10="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_da_5/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_da_5/pascalvoc/"
# os.system(command01)
# os.system(command02)
# os.system(command03)
# os.system(command04)
# os.system(command05)
# os.system(command06)
# os.system(command07)
# os.system(command08)
# os.system(command09)
# os.system(command10)


# # ------ COVERAGE ------

# # ------ GT ------
# command="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test --path_out /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --grid 10"
# os.system(command)


# # ------ 1 ------
# command01="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_1/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_1/inference_test/coverage/ --grid 10 "
# command02="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_da_1/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_da_1/inference_test/coverage/ --grid 10 " 
# command03="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_1/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_1/inference_test/coverage/ --grid 10 "
# command04="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_da_1/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_da_1/inference_test/coverage/ --grid 10 "   
# command05="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_1/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_1/inference_test/coverage/ --grid 10 "
# command06="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_da_1/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_da_1/inference_test/coverage/ --grid 10 "  
# command07="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_1/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_1/inference_test/coverage/ --grid 10 "
# command08="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_da_1/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_da_1/inference_test/coverage/ --grid 10 "    
# command09="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_1/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_1/inference_test/coverage/ --grid 10  "
# command10="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_da_1/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_da_1/inference_test/coverage/ --grid 10 "
# os.system(command01)
# os.system(command02)
# os.system(command03)
# os.system(command04)
# os.system(command05)
# os.system(command06)
# os.system(command07)
# os.system(command08)
# os.system(command09)
# os.system(command10)

# # ------ 2 ------
# command01="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_2/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_2/inference_test/coverage/ --grid 10 "
# command02="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_da_2/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_da_2/inference_test/coverage/ --grid 10 " 
# command03="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_2/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_2/inference_test/coverage/ --grid 10 "
# command04="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_da_2/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_da_2/inference_test/coverage/ --grid 10 "   
# command05="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_2/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_2/inference_test/coverage/ --grid 10 "
# command06="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_da_2/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_da_2/inference_test/coverage/ --grid 10 "  
# command07="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_2/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_2/inference_test/coverage/ --grid 10 "
# command08="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_da_2/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_da_2/inference_test/coverage/ --grid 10 "    
# command09="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_2/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_2/inference_test/coverage/ --grid 10  "
# command10="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_da_2/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_da_2/inference_test/coverage/ --grid 10 "
# os.system(command01)
# os.system(command02)
# os.system(command03)
# os.system(command04)
# os.system(command05)
# os.system(command06)
# os.system(command07)
# os.system(command08)
# os.system(command09)
# os.system(command10)

# # ------ 3 ------
# command01="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_3/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_3/inference_test/coverage/ --grid 10 "
# command02="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_da_3/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_da_3/inference_test/coverage/ --grid 10 " 
# command03="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_3/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_3/inference_test/coverage/ --grid 10 "
# command04="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_da_3/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_da_3/inference_test/coverage/ --grid 10 "   
# command05="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_3/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_3/inference_test/coverage/ --grid 10 "
# command06="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_da_3/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_da_3/inference_test/coverage/ --grid 10 "  
# command07="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_3/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_3/inference_test/coverage/ --grid 10 "
# command08="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_da_3/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_da_3/inference_test/coverage/ --grid 10 "    
# command09="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_3/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_3/inference_test/coverage/ --grid 10  "
# command10="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_da_3/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_da_3/inference_test/coverage/ --grid 10 "
# os.system(command01)
# os.system(command02)
# os.system(command03)
# os.system(command04)
# os.system(command05)
# os.system(command06)
# os.system(command07)
# os.system(command08)
# os.system(command09)
# os.system(command10)

# # ------ 4 ------
# command01="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_4/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_4/inference_test/coverage/ --grid 10 "
# command02="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_da_4/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_da_4/inference_test/coverage/ --grid 10 " 
# command03="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_4/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_4/inference_test/coverage/ --grid 10 "
# command04="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_da_4/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_da_4/inference_test/coverage/ --grid 10 "   
# command05="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_4/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_4/inference_test/coverage/ --grid 10 "
# command06="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_da_4/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_da_4/inference_test/coverage/ --grid 10 "  
# command07="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_4/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_4/inference_test/coverage/ --grid 10 "
# command08="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_da_4/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_da_4/inference_test/coverage/ --grid 10 "    
# command09="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_4/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_4/inference_test/coverage/ --grid 10  "
# command10="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_da_4/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_da_4/inference_test/coverage/ --grid 10 "
# os.system(command01)
# os.system(command02)
# os.system(command03)
# os.system(command04)
# os.system(command05)
# os.system(command06)
# os.system(command07)
# os.system(command08)
# os.system(command09)
# os.system(command10)

# # ------ 5 ------
# command01="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_5/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_5/inference_test/coverage/ --grid 10 "
# command02="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_da_5/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_da_5/inference_test/coverage/ --grid 10 " 
# command03="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_5/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_5/inference_test/coverage/ --grid 10 "
# command04="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_da_5/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_da_5/inference_test/coverage/ --grid 10 "   
# command05="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_5/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_5/inference_test/coverage/ --grid 10 "
# command06="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_da_5/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_da_5/inference_test/coverage/ --grid 10 "  
# command07="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_5/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_5/inference_test/coverage/ --grid 10 "
# command08="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_da_5/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_da_5/inference_test/coverage/ --grid 10 "    
# command09="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_5/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_5/inference_test/coverage/ --grid 10  "
# command10="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_da_5/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_da_5/inference_test/coverage/ --grid 10 "
# os.system(command01)
# os.system(command02)
# os.system(command03)
# os.system(command04)
# os.system(command05)
# os.system(command06)
# os.system(command07)
# os.system(command08)
# os.system(command09)
# os.system(command10)


# # ------ COVERAGE EVAL------

# # ------ 1 ------
# command01="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_1/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name base_1 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_1/inference_test --shape 1024"
# command02="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_da_1/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name base_da_1 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_da_1/inference_test --shape 1024"
# command03="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_1/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name high3_1 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_1/inference_test --shape 1024"
# command04="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_da_1/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name high3_da_1 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_da_1/inference_test --shape 1024"
# command05="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_1/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name low3_1 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_1/inference_test --shape 1024"
# command06="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_da_1/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name low3_da_1 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_da_1/inference_test --shape 1024"
# command07="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_1/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name low9_1 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_1/inference_test --shape 1024"
# command08="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_da_1/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name low9_da_1 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_da_1/inference_test --shape 1024"
# command09="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_1/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name low27_1 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_1/inference_test --shape 1024"
# command10="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_da_1/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name low27_da_1 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_da_1/inference_test --shape 1024"
# os.system(command01)
# os.system(command02)
# os.system(command03)
# os.system(command04)
# os.system(command05)
# os.system(command06)
# os.system(command07)
# os.system(command08)
# os.system(command09)
# os.system(command10)

# # ------ 2 ------
# command01="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_2/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name base_2 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_2/inference_test --shape 1024"
# command02="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_da_2/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name base_da_2 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_da_2/inference_test --shape 1024"
# command03="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_2/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name high3_2 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_2/inference_test --shape 1024"
# command04="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_da_2/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name high3_da_2 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_da_2/inference_test --shape 1024"
# command05="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_2/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name low3_2 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_2/inference_test --shape 1024"
# command06="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_da_2/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name low3_da_2 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_da_2/inference_test --shape 1024"
# command07="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_2/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name low9_2 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_2/inference_test --shape 1024"
# command08="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_da_2/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name low9_da_2 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_da_2/inference_test --shape 1024"
# command09="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_2/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name low27_2 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_2/inference_test --shape 1024"
# command10="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_da_2/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name low27_da_2 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_da_2/inference_test --shape 1024"
# os.system(command01)
# os.system(command02)
# os.system(command03)
# os.system(command04)
# os.system(command05)
# os.system(command06)
# os.system(command07)
# os.system(command08)
# os.system(command09)
# os.system(command10)

# # ------ 3 ------
# command01="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_3/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name base_3 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_3/inference_test --shape 1024"
# command02="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_da_3/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name base_da_3 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_da_3/inference_test --shape 1024"
# command03="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_3/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name high3_3 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_3/inference_test --shape 1024"
# command04="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_da_3/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name high3_da_3 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_da_3/inference_test --shape 1024"
# command05="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_3/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name low3_3 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_3/inference_test --shape 1024"
# command06="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_da_3/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name low3_da_3 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_da_3/inference_test --shape 1024"
# command07="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_3/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name low9_3 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_3/inference_test --shape 1024"
# command08="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_da_3/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name low9_da_3 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_da_3/inference_test --shape 1024"
# command09="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_3/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name low27_3 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_3/inference_test --shape 1024"
# command10="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_da_3/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name low27_da_3 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_da_3/inference_test --shape 1024"
# os.system(command01)
# os.system(command02)
# os.system(command03)
# os.system(command04)
# os.system(command05)
# os.system(command06)
# os.system(command07)
# os.system(command08)
# os.system(command09)
# os.system(command10)

# # ------ 4 ------
# command01="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_4/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name base_4 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_4/inference_test --shape 1024"
# command02="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_da_4/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name base_da_4 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_da_4/inference_test --shape 1024"
# command03="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_4/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name high3_4 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_4/inference_test --shape 1024"
# command04="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_da_4/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name high3_da_4 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_da_4/inference_test --shape 1024"
# command05="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_4/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name low3_4 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_4/inference_test --shape 1024"
# command06="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_da_4/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name low3_da_4 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_da_4/inference_test --shape 1024"
# command07="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_4/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name low9_4 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_4/inference_test --shape 1024"
# command08="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_da_4/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name low9_da_4 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_da_4/inference_test --shape 1024"
# command09="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_4/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name low27_4 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_4/inference_test --shape 1024"
# command10="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_da_4/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name low27_da_4 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_da_4/inference_test --shape 1024"
# os.system(command01)
# os.system(command02)
# os.system(command03)
# os.system(command04)
# os.system(command05)
# os.system(command06)
# os.system(command07)
# os.system(command08)
# os.system(command09)
# os.system(command10)

# # ------ 5 ------
# command01="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_5/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name base_5 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_5/inference_test --shape 1024"
# command02="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_da_5/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name base_da_5 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/base_da_5/inference_test --shape 1024"
# command03="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_5/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name high3_5 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_5/inference_test --shape 1024"
# command04="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_da_5/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name high3_da_5 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/high3_da_5/inference_test --shape 1024"
# command05="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_5/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name low3_5 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_5/inference_test --shape 1024"
# command06="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_da_5/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name low3_da_5 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low3_da_5/inference_test --shape 1024"
# command07="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_5/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name low9_5 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_5/inference_test --shape 1024"
# command08="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_da_5/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name low9_da_5 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low9_da_5/inference_test --shape 1024"
# command09="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_5/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name low27_5 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_5/inference_test --shape 1024"
# command10="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_da_5/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name low27_da_5 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_da_5/inference_test --shape 1024"


# command10="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py \
#     --pred_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test3/ \
#     --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test2/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/hp/labels/test/ \
#     --run_name low27_da_5 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL/low27_da_5/inference_test --shape 1024"

# os.system(command01)
# os.system(command02)
# os.system(command03)
# os.system(command04)
# os.system(command05)
# os.system(command06)
# os.system(command07)
# os.system(command08)
# os.system(command09)
# os.system(command10)


############################ K-FOLD ############################

# # ------ TRAIN ------

# # ------ 1 ------
# command01="python train.py --img 1024 --batch 8 --epochs 200 --data halimeda1.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/k-fold_training_2/ --name low27_da_1  --single-cls --hyp data/hyps/final/hyp.low27_da.yaml"
# command02="python train.py --img 1024 --batch 8 --epochs 200 --data halimeda2.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/k-fold_training_2/ --name low27_da_2  --single-cls --hyp data/hyps/final/hyp.low27_da.yaml"
# command03="python train.py --img 1024 --batch 8 --epochs 200 --data halimeda3.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/k-fold_training_2/ --name low27_da_3  --single-cls --hyp data/hyps/final/hyp.low27_da.yaml"
# command04="python train.py --img 1024 --batch 8 --epochs 200 --data halimeda4.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/k-fold_training_2/ --name low27_da_4  --single-cls --hyp data/hyps/final/hyp.low27_da.yaml"
# command05="python train.py --img 1024 --batch 8 --epochs 200 --data halimeda5.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/k-fold_training_2/ --name low27_da_5  --single-cls --hyp data/hyps/final/hyp.low27_da.yaml"
# command06="python train.py --img 1024 --batch 8 --epochs 200 --data halimeda6.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/k-fold_training_2/ --name low27_da_6  --single-cls --hyp data/hyps/final/hyp.low27_da.yaml"
# command07="python train.py --img 1024 --batch 8 --epochs 200 --data halimeda7.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/k-fold_training_2/ --name low27_da_7  --single-cls --hyp data/hyps/final/hyp.low27_da.yaml"
# command08="python train.py --img 1024 --batch 8 --epochs 200 --data halimeda8.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/k-fold_training_2/ --name low27_da_8  --single-cls --hyp data/hyps/final/hyp.low27_da.yaml"
# command09="python train.py --img 1024 --batch 8 --epochs 200 --data halimeda9.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/k-fold_training_2/ --name low27_da_9  --single-cls --hyp data/hyps/final/hyp.low27_da.yaml"
# command10="python train.py --img 1024 --batch 8 --epochs 200 --data halimeda10.yaml --weights yolov5x.pt --project projects/halimeda/final_trainings/k-fold_training_2/ --name low27_da_10  --single-cls --hyp data/hyps/final/hyp.low27_da.yaml"
# os.system(command01)
# os.system(command02)
# os.system(command03)
# os.system(command04)
# os.system(command05)
# os.system(command06)
# os.system(command07)
# os.system(command08)
# os.system(command09)
# os.system(command10)

# # ------ INFERENCE ------

# # ------ 1 ------
# command01="python detect.py --weights projects/halimeda/final_trainings/k-fold_training_2/low27_da_1/weights/best.pt --project projects/halimeda/final_trainings/k-fold_training_2/low27_da_1/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command02="python detect.py --weights projects/halimeda/final_trainings/k-fold_training_2/low27_da_2/weights/best.pt --project projects/halimeda/final_trainings/k-fold_training_2/low27_da_2/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command03="python detect.py --weights projects/halimeda/final_trainings/k-fold_training_2/low27_da_3/weights/best.pt --project projects/halimeda/final_trainings/k-fold_training_2/low27_da_3/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command04="python detect.py --weights projects/halimeda/final_trainings/k-fold_training_2/low27_da_4/weights/best.pt --project projects/halimeda/final_trainings/k-fold_training_2/low27_da_4/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command05="python detect.py --weights projects/halimeda/final_trainings/k-fold_training_2/low27_da_5/weights/best.pt --project projects/halimeda/final_trainings/k-fold_training_2/low27_da_5/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command06="python detect.py --weights projects/halimeda/final_trainings/k-fold_training_2/low27_da_6/weights/best.pt --project projects/halimeda/final_trainings/k-fold_training_2/low27_da_6/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command07="python detect.py --weights projects/halimeda/final_trainings/k-fold_training_2/low27_da_7/weights/best.pt --project projects/halimeda/final_trainings/k-fold_training_2/low27_da_7/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command08="python detect.py --weights projects/halimeda/final_trainings/k-fold_training_2/low27_da_8/weights/best.pt --project projects/halimeda/final_trainings/k-fold_training_2/low27_da_8/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command09="python detect.py --weights projects/halimeda/final_trainings/k-fold_training_2/low27_da_9/weights/best.pt --project projects/halimeda/final_trainings/k-fold_training_2/low27_da_9/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# command10="python detect.py --weights projects/halimeda/final_trainings/k-fold_training_2/low27_da_10/weights/best.pt --project projects/halimeda/final_trainings/k-fold_training_2/low27_da_10/  --name inference_test/ --data data/halimeda.yaml --source  datasets/halimeda/images/test --save-txt --save-conf"
# os.system(command01)
# os.system(command02)
# os.system(command03)
# os.system(command04)
# os.system(command05)
# os.system(command06)
# os.system(command07)
# os.system(command08)
# os.system(command09)
# os.system(command10)


# # ------ EVAL OD ------

# # ------ 1 ------
# command01="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_1/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_1/pascalvoc/"
# command02="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_2/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_2/pascalvoc/"
# command03="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_3/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_3/pascalvoc/"
# command04="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_4/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_4/pascalvoc/"
# command05="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_5/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_5/pascalvoc/"
# command06="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_6/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_6/pascalvoc/"
# command07="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_7/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_7/pascalvoc/"
# command08="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_8/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_8/pascalvoc/"
# command09="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_9/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_9/pascalvoc/"
# command10="python /mnt/c/Users/haddo/object_detection_utils/metrics/pascalvoc.py -tiou 0.5 -tconf 0.1 -gtcoords rel -detcoords rel -imgsize 1024,1024 -gtformat=xywh -detformat=xywh -gt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test -det /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_10/inference_test/labels/ -np -sp /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_10/pascalvoc/"
# os.system(command01)
# os.system(command02)
# os.system(command03)
# os.system(command04)
# os.system(command05)
# os.system(command06)
# os.system(command07)
# os.system(command08)
# os.system(command09)
# os.system(command10)


# # ------ COVERAGE ------

# # ------ GT ------
# # command="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test --path_out /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --grid 10"
# # os.system(command)


# # ------ 1 ------
# command01="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_1/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_1/inference_test/coverage/ --grid 10 "
# command02="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_2/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_2/inference_test/coverage/ --grid 10 "
# command03="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_3/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_3/inference_test/coverage/ --grid 10 "
# command04="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_4/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_4/inference_test/coverage/ --grid 10 "
# command05="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_5/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_5/inference_test/coverage/ --grid 10 "
# command06="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_6/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_6/inference_test/coverage/ --grid 10 "
# command07="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_7/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_7/inference_test/coverage/ --grid 10 "
# command08="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_8/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_8/inference_test/coverage/ --grid 10 "
# command09="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_9/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_9/inference_test/coverage/ --grid 10 "
# command10="python /mnt/c/Users/haddo/object_detection_utils/metrics/coverage.py --shape 1024 --path_txt /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_10/inference_test/labels/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_10/inference_test/coverage/ --grid 10 "
# os.system(command01)
# os.system(command02)
# os.system(command03)
# os.system(command04)
# os.system(command05)
# os.system(command06)
# os.system(command07)
# os.system(command08)
# os.system(command09)
# os.system(command10)


# # ------ COVERAGE EVAL------

# # ------ 1 ------
# command01="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_1/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name low27_da_1 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_1/inference_test --shape 1024"
# command02="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_2/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name low27_da_2 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_2/inference_test --shape 1024"
# command03="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_3/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name low27_da_3 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_3/inference_test --shape 1024"
# command04="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_4/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name low27_da_4 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_4/inference_test --shape 1024"
# command05="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_5/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name low27_da_5 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_5/inference_test --shape 1024"
# command06="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_6/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name low27_da_6 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_6/inference_test --shape 1024"
# command07="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_7/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name low27_da_7 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_7/inference_test --shape 1024"
# command08="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_8/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name low27_da_8 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_8/inference_test --shape 1024"
# command09="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_9/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name low27_da_9 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_9/inference_test --shape 1024"
# command10="python /mnt/c/Users/haddo/object_detection_utils/metrics/eval_ss.py --pred_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_10/inference_test/coverage --gt_im_path  /mnt/c/Users/haddo/yolov5/datasets/halimeda/coverage/test/ --gt_label_path /mnt/c/Users/haddo/yolov5/datasets/halimeda/labels/test/ --run_name low27_da_10 --save_path /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/k-fold_training_2/low27_da_10/inference_test --shape 1024"
# os.system(command01)
# os.system(command02)
# os.system(command03)
# os.system(command04)
# os.system(command05)
# os.system(command06)
# os.system(command07)
# os.system(command08)
# os.system(command09)
# os.system(command10)


