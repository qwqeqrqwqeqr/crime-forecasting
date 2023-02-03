#!/bin/bash
target_folder="/data/safety/"
python_file="./report_app.py"

today=$(date "+%Y%m%d")
file=POL_01_${today}_M.csv

echo `date`
echo traget file :${target_folder}${file}
python3 ${python_file} ${target_folder}${file}


