#!/bin/bash
(crontab -l; echo "0 9 * * * /bin/sh /seoul/report.sh >> /seoul/log/report.log 2>&1") | crontab
(crontab -l; echo "0 9 * * * /bin/sh /seoul/hangang.sh >> /seoul/log/hangang.log 2>&1") | crontab
(crontab -l; echo "0 9 * * * /bin/sh /seoul/tourist.sh >> /seoul/log/tourist.log 2>&1") | crontab
(crontab -l; echo "0 9 * * * /bin/sh /seoul/subway.sh >> /seoul/log/subway.log 2>&1") | crontab
(crontab -l; echo "0 9 8 * * /bin/sh /seoul/movefile.sh") | crontab

service cron restart
