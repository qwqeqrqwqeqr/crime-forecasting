#!/bin/bash
(crontab -l; echo "45 8 8 * * /bin/sh /seoul/move_file_by_month.sh") | crontab
(crontab -l; echo "45 8 8 * * /bin/sh /seoul/move_file_by_year.sh") | crontab
(crontab -l; echo "45 8 * * * /bin/sh /seoul/report.sh >> /seoul/log/report.log 2>&1") | crontab
(crontab -l; echo "45 8 * * * /bin/sh /seoul/hangang.sh >> /seoul/log/hangang.log 2>&1") | crontab
(crontab -l; echo "45 8 * * * /bin/sh /seoul/tourist.sh >> /seoul/log/tourist.log 2>&1") | crontab
(crontab -l; echo "45 8 * * * /bin/sh /seoul/subway.sh >> /seoul/log/subway.log 2>&1") | crontab


service cron restart
