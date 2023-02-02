#!/bin/bash

###############################################
# setting
###############################################
target_folder="/home/ncyc-admin/crime_forecasting/test/data/report/"
python_file="/home/ncyc-admin/crime_forecasting/tourist_app.py"

today=$(date "+%Y%m%d")
file=POL_01_20220101_M.csv
#file=POL_01_${today}_M.csv

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


#echo `date`
#echo 대상파일 : ${file}
python3 ${python_file} ${target_folder}${file}


