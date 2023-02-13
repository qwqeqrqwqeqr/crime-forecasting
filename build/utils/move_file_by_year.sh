#!/bin/bash
year=$(date --date '1 year ago' "+%Y")

mkdir /data/safety/${year}

find /data/safety/*${year}*.csv -exec cp '{}' /data/safety/${year}/ \;





