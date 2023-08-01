import argparse
import datetime
import json
import os
import shutil
import random
import subprocess
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--dataset-path', type=str, required=True,
    )
    arguments = parser.parse_args()

    python = f'{sys.executable} tools/infer/predict_system.py'
    # image_arg = '--image_dir="./doc/imgs_en/254.jpg"'
    image_arg = f'--image_dir="{arguments.dataset_path}"'
    model_args = '--det_model_dir="./inference/det/en_PP-OCRv3_det_infer/" --cls_model_dir="./inference/cls/ch_ppocr_mobile_v2.0_cls_infer/" --rec_model_dir="./inference/reg/en_PP-OCRv3_rec_infer/"  --rec_char_dict_path="./ppocr/utils/en_dict.txt"'

    commands = [f'{python} {image_arg} {model_args}']

    subprocess.run(
        commands, check=True, shell=True,
        #stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )

