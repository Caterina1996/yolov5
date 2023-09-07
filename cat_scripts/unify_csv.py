
import os
import re
import numpy as np
import argparse
import sys
from natsort import natsorted
import pandas as pd

"""
Call example:

python unify_csv.py --path_in /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/final_trainings/yolo_XL --lookfor "results_pascalvoc_2"

python unify_csv.py --path_in /mnt/c/Users/haddo/yolov5/projects/halimeda/k-fold_training/ --path_out /mnt/c/Users/haddo/yolov5/projects/halimeda/k-fold_training/ --lookfor "results_pascalvoc"

"""

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--path_in', help='path to the run folder.')
    parser.add_argument('--path_out', help='path to the run folder.')
    parser.add_argument('--lookfor', help='csv name to look for.')

    parsed_args = parser.parse_args(sys.argv[1:])

    path_in = parsed_args.path_in
    path_out = parsed_args.path_out
    lookfor = parsed_args.lookfor

    rows_data_list = list()
    rows_name_list = list()

    for root, dirs, files in os.walk(path_in):
        for file in enumerate(sorted(files)):     

            if re.search("\.(csv)$", file[1]):    # csv

                if lookfor in file[1]:
                    print("CSV FOUND!!",file[1],"\n")
                    
                    columns_name_list = list()

                    path_file = os.path.join(root, file[1])
                    excel =  pd.read_csv(path_file)    # excel = pd.ExcelFile(path_file, engine='openpyxl') # excel =  pd.read_csv(path_file)

                    columns_name_list.append(excel)

                    data = pd.DataFrame(excel)

                    data_np = data.to_numpy()

                    name = os.path.join(root, file[1])

                    rows_name_list.append(name)
                    for i in range(data_np.shape[0]-1):
                        rows_name_list.append(" ")
                    rows_data_list.append(data_np)

    rows_data = np.vstack(rows_data_list)
    df = pd.DataFrame(data=rows_data, index=rows_name_list, columns=columns_name_list)
    filepath = os.path.join(path_out, lookfor + "_unified_2.xlsx") # the 2 can be removed
    df.to_excel(filepath, index=True)


if __name__ == "__main__":
    main()