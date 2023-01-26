#!/bin/bash
target_folder="./"
python_file="./hangang_app.py"

today=$(date "+%Y%m%d")
file=POL_01_${today}_M.csv

echo
echo
echo
echo
echo _______________[한강경찰대]_______________
echo
echo
echo
echo
echo

echo `date`
echo 대상파일 : ${file}
python ${python_file} ${target_folder}${file}


