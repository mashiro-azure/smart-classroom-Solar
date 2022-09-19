# Smart Classroom Solar

**Not for public use.**

This repo is meant for internal testing only. Those who know, know.

## Infrastructure
- InfluxDB \- Storing Data
- Grafana \- Dashboard

## Use case of each files
- command.txt \- For manual triggering and debugging 
- copy.bat \- Copying the Original CSV File From the Data Source to a Separate Folder for Save Keeping
- padding.py \- Coverting the Original CSV File to a Usable CSV File for influxDB
- solar_data_retrieve.conf \- Configure Telegraf