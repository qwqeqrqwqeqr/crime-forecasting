#!/bin/bash
month=$(date --date '1 month ago' "+%Y%m")

mkdir /data/population/${month}
mkdir /data/safety/${month}

find /data/population/*${month}*.csv -exec cp '{}' /data/population/${month}/ \;
find /data/safety/*${month}*.csv -exec cp '{}' /data/safety/${month}/ \;





