@ECHO OFF
xcopy "C:\Users\Lenovo's user\Desktop\Dashboard data\raw.csv" "C:\Users\Lenovo's user\Desktop\Solar_Mani\raw.csv" /y /v
timeout 2
"C:\Users\Lenovo's user\Desktop\Solar_Mani\venv\Scripts\python.exe" "C:\Users\Lenovo's user\Desktop\Solar_Mani\padding.py"
"C:\Program Files\InfluxData\telegraf\telegraf.exe" --config "C:\Program Files\InfluxData\telegraf\solar_data_retrieve.conf" --once --debug"
