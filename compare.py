import argparse
import datetime
import json
import os
import shutil
import random
import subprocess
import sys
import glob

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset-path', type=str, required=True)
    parser.add_argument('--results-path', type=str, required=True)
    arguments = parser.parse_args()

    dataset_file_names = []
    for full_file_path in glob.glob(os.path.join(arguments.dataset_path, '*')):
        file_name = full_file_path.split(os.sep)[-1]
        if file_name.endswith('.json'):
            continue

        if not file_name.endswith('.pdf'):
            dataset_file_names.append(file_name)
            continue

        file_split = file_name.split('.')
        file_name = '.'.join(file_split[:-1]) + '_0.png'

        dataset_file_names.append(file_name)

    results_file_names = []
    for full_file_path in glob.glob(os.path.join(arguments.results_path, '*')):
        file_name = full_file_path.split(os.sep)[-1]

        if not file_name.endswith('.json'):
            continue
        
        file_name = file_name[:-len('.json')]
        results_file_names.append(file_name)

    results_file_names = set(results_file_names)
    dataset_file_names = set(dataset_file_names)

    print(len(results_file_names))
    print(len(dataset_file_names))
    print(len(results_file_names.intersection(dataset_file_names)))

    # print('Files that have results but no image:', results_file_names.difference(dataset_file_names))
    print('Images without results:', dataset_file_names.difference(results_file_names))
