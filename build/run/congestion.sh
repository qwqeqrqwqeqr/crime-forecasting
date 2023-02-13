#!/bin/bash


report_target_folder="/data/safety/"
life_population_target_folder="/data/population/"
month=$(date --date '1 month ago' "+%Y%m")/


report_dir=${report_target_folder}${month}
life_population_dir=${life_population_target_folder}${month}

python_file="./congestion_app.py"


python3 ${python_file} ${report_dir} ${life_population_dir}

