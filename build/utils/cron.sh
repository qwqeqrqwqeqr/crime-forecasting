#!/bin/bash
(crontab -l; echo "0 7 * * * /bin/sh /seoul/report.sh >> /seoul/log/report.log 2>&1") | crontab
(crontab -l; echo "0 7 * * * /bin/sh /seoul/hangang.sh >> /seoul/log/hangang_.log 2>&1") | crontab
(crontab -l; echo "0 7 * * * /bin/sh /seoul/tourist.sh >> /seoul/log/tourist_.log 2>&1") | crontab
(crontab -l; echo "0 7 * * * /bin/sh /seoul/subway.sh >> /seoul/log/subway_.log 2>&1") | crontab

service cron restart
