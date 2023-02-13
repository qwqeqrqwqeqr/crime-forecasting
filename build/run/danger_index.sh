#!/bin/bash


report_target_folder="/data/safety/"
life_population_target_folder="/data/population/"
month=$(date --date '1 month ago' "+%Y%m")/
year=$(date --date '1 year ago' "+%Y%m")/


report_dir=${report_target_folder}${year}
life_population_dir=${life_population_target_folder}${month}

python_file="./danger_index.py"


python3 ${python_file} ${report_dir} ${life_population_dir}

