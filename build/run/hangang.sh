#!/bin/bash
target_folder="/data/safety/"
python_file="./hangang_app.py"

today=$(date "+%Y%m%d")
file=POL_01_${today}.csv

echo `date`
echo traget file :${target_folder}${file}
line=`grep 'END_CD' ${target_folder}${file} | wc -l`
if [ $line -eq 0 ]
then
    perl -p -i -e '$.==1 and print "RECV_NO,DAY,TIME,EVT_CL_CD,RECV_EMG_CD,RPTER_SEX,TRC_TYPE,HPPN_Y_SW,HPPN_X_SW,HPPN_Y_NE,HPPN_X_NE,HPPN_Y_NW,HPPN_X_NW,HPPN_Y_SE,HPPN_X_SE,END_CD\n"' ${target_folder}${file}
fi
python3 ${python_file} ${target_folder}${file}


