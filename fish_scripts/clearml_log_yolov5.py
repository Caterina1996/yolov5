from clearml import Task, Logger
# from ultralytics import YOLO
# from models.yolo import Model
import argparse
# import torch

'''
# -------------------------- Default config -------------------------------------
python clearml_log_yolov5.py --project_name "Peces" --task_name "Argparse test" \
--model_size "n" --dataset "/mnt/c/Users/Uib/Documents/peces/dataset/data.yaml" \
--optimizer "SGD" --epochs 200 --batch 8 --patience 20 \
--yolo_proj "./train_argparse_test/" --yolo_name "test"

# --------------------------- Custom config -------------------------------------
python clearml_log_yolov5.py --project_name "Peces" --task_name "Argparse test" \
--model_size "n" --config "./config.yaml" --dataset "./dataset/data.yaml" \
--optimizer "SGD" --epochs 200 --batch 8 --patience 20 \
--yolo_proj "./train_argparse_test/" --yolo_name "test"
'''

parser = argparse.ArgumentParser()
parser.add_argument('--project_name', help='ClearML Project Name')
parser.add_argument('--task_name', help='ClearML Task Name')
parser.add_argument('--model_size', help='yolov5 Model Size', 
                    choices=['n', 's', 'm', 'l', 'x'], default=None)
parser.add_argument('--pre_trained', help='Wheter to use YOLO pretrained weights or not',
                    default=True, type=bool)
parser.add_argument('--config', help='config.yaml path', default=None)
parser.add_argument('--dataset', help='dataset.yaml path')
parser.add_argument('--epochs', help='Number of epochs to train the model', type=int)
parser.add_argument('--optimizer', help='Optimizer to use during training',default="SGD")
parser.add_argument('--batch', help='Batch size during training', type=int)
parser.add_argument('--patience', help='Patience during training', default=None, type=int)
parser.add_argument('--yolo_proj', help='yolov5 project name where train will be saved')
parser.add_argument('--yolo_name', help='yolov5 save folder name')
parser.add_argument('--lr', help='Initial learning rate', type=float, default=None)
parser.add_argument('--seed', help='Seed during training', type=int, default=42)

args = parser.parse_args()

project_name = args.project_name
task_name = args.task_name
model_size = args.model_size
pretrained = args.pre_trained
config = args.config
dataset = args.dataset
epochs = args.epochs
optimizer = args.optimizer
batch = args.batch
patience = args.patience
yolo_proj = args.yolo_proj
yolo_name = args.yolo_name
lr = args.lr
seed = args.seed


# def on_fit_epoch_end(trainer):
#     # Log loss data to ClearML
#     for loss_type in ('box_loss', 'cls_loss', 'dfl_loss'):
#         for split, dict in zip(('train', 'val'), (trainer.label_loss_items(trainer.tloss), trainer.metrics)):
#             key = f'{split}/{loss_type}'
#             if key in dict.keys():
#                 Logger.current_logger().report_scalar(
#                     f'{loss_type}',
#                     key,
#                     iteration=trainer.epoch + 1,
#                     value=dict[key]
#                 )

#     # Log F1 Score data to ClearML
#     if 'metrics/precision(B)' in trainer.metrics.keys() and 'metrics/recall(B)' in trainer.metrics.keys():
#         precision = trainer.metrics['metrics/precision(B)']
#         recall = trainer.metrics['metrics/recall(B)']
#         f1 = 2*(precision*recall)/(precision + recall)
#         Logger.current_logger().report_scalar(
#             'F1-Score',
#             'F1',
#             iteration=trainer.epoch + 1,
#             value=f1
#         )

#     # Log fitness values to ClearML (it is also logged in train graphic)
#     Logger.current_logger().report_scalar(
#         'Fitness',
#         'Fitness function',
#         iteration=trainer.epoch + 1,
#         value=trainer.fitness
#     )



task = Task.init(
    project_name=project_name,
    task_name=task_name,
    output_uri=True # To upload the model and weights to ClearML.
)

# model_size = 'x'
model_variant = f'YOLOv5{model_size}-seg'
task.set_parameter('model_variant', model_variant)


train_args =  dict(
    data=dataset,
    optimizer=optimizer,
    epochs=epochs,
    patience=patience,
    batch=batch,
    project=yolo_proj,
    name=yolo_name,
    seed=seed
)
if config is not None:
    train_args['cfg'] = config
    task.connect_configuration(train_args['cfg'], 'Config_file')
if patience is not None:
    train_args['patience'] = patience
if lr is not None: 
    train_args['lr0'] = lr

task.connect(train_args)

task.connect_configuration(train_args['data'], 'Dataset yaml')

task.close()