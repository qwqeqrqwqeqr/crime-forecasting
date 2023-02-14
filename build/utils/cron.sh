#!/bin/bash
(crontab -l; echo "45 8 8 * * sh /move_file_by_month.sh") | crontab
(crontab -l; echo "45 8 8 * * sh /move_file_by_year.sh") | crontab
(crontab -l; echo "45 8 * * * sh /report.sh >> /log/report.log 2>&1") | crontab
(crontab -l; echo "45 8 * * * sh /hangang.sh >> /log/hangang.log 2>&1") | crontab
(crontab -l; echo "45 8 * * * sh /tourist.sh >> /log/tourist.log 2>&1") | crontab
(crontab -l; echo "45 8 * * * sh /subway.sh >> /log/subway.log 2>&1") | crontab
(crontab -l; echo "45 8 8 * * sh /congestion.sh >> /log/congestion.log 2>&1") | crontab
(crontab -l; echo "45 8 8 * * sh /danger_index.sh >> /log/danger_index.log 2>&1") | crontab


service cron restart
