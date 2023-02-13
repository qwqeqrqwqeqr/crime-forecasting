#!/bin/bash
(crontab -l; echo "45 8 8 * * /bin/sh /seoul/move_file_by_month.sh") | crontab
(crontab -l; echo "45 8 8 * * /bin/sh /seoul/move_file_by_year.sh") | crontab
(crontab -l; echo "45 8 * * * /bin/sh /seoul/report.sh >> /seoul/log/report/report.log 2>&1") | crontab
(crontab -l; echo "45 8 * * * /bin/sh /seoul/hangang.sh >> /seoul/log/hangang/hangang.log 2>&1") | crontab
(crontab -l; echo "45 8 * * * /bin/sh /seoul/tourist.sh >> /seoul/log/tourist/tourist.log 2>&1") | crontab
(crontab -l; echo "45 8 * * * /bin/sh /seoul/subway.sh >> /seoul/log/subway/subway.log 2>&1") | crontab
(crontab -l; echo "45 8 8 * * /bin/sh /seoul/congestion.sh >> /seoul/log/congestion/congestion.log 2>&1") | crontab
(crontab -l; echo "45 8 8 * * /bin/sh /seoul/danger_index.sh >> /seoul/log/congestion/danger_index 2>&1") | crontab


service cron restart
