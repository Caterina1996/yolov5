import os
import json

project_path = r"D:\yolov5\projects\fish\17_species"
dataset_path = r"D:\yolov5\datasets\fish\17_species"
raw_val_data = {}

for fold_idx in range(1, 6):

    os.system(f'python val.py --task val --weights {os.path.join(project_path, "extra_large", "fold_" + str(fold_idx), "weights", "best.pt")} \
               --project {os.path.join(project_path, "extra_large", "fold_" + str(fold_idx))} --name val/  --data {os.path.join(dataset_path, "data_fold_" + str(fold_idx) + ".yaml")} \
                  --img 1280 --exist-ok')
    
    with open(os.path.join(fr"D:\yolov5\projects\fish\17_species\extra_large\fold_{fold_idx}", "val", "metrics_data.json"), "r") as json_file:
        data = json.load(json_file)

    raw_val_data[f"fold_{fold_idx}"] = data

with open(os.path.join(r"D:\yolov5\projects\fish\17_species\extra_large", "raw_val_data.json"), 'w') as f:
    json.dump(raw_val_data, f, indent=4)