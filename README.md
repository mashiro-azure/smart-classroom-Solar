# Smart Classroom Solar

**Not for public use.**

This repo is meant for internal testing only. Those who know, know.

## Infrastructure
- InfluxDB \- Storing Data
- Grafana \- Dashboard

## Use case of each files
- command.txt \- For manual triggering and debugging 
- copy.bat \- Copying the original CSV file from the data source to a separate folder for safekeeping
- padding.py \- Coverting the original CSV file to a usable CSV file for InfluxDB
- solar_data_retrieve.conf \- Configure Telegraf