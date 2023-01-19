#!/bin/bash
target_folder="./"
python_file="./subway_app.py"


today=$(date "+%Y%m%d")
file=POL_01_${today}_M.csv
echo ============ 112신고 빈도데이터 [지하철 경찰대] ===========
echo `date`
echo 대상폴더 : ${target_folder}
echo 대상파일 : ${file}

python ${python_file} ${target_folder}${file}

