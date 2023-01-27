#!/bin/bash

###############################################
# setting
###############################################
target_folder="./"
python_file="./tourist_app.py"

today=$(date "+%Y%m%d")
file=POL_01_${today}_M.csv

list=$(find ${target_folder} -type f -name "*.csv")

echo ${list}

echo
echo
echo
echo
echo _______________[관광지경찰대]_______________
echo
echo
echo
echo
echo

#echo `date`
#echo 대상파일 : ${file}
#python ${python_file} ${target_folder}${file}


