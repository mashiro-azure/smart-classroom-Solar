import pandas as pd

if __name__ == '__main__':
        df = pd.read_csv('C:/Users/Lenovo\'s user/Desktop/Solar_Mani/raw.csv')
        df = df.fillna(0)
        for col in ['Vpv','Chg_cur','Chg_power','acc_kWh_hi','acc_kWh_lo','acc_kWh_Total','acc_kWh_Today','Chg_status','Bat_Volt','Bat_Cur','Ebat_dischrToday','Ebat_dischrTotal','work_status','OP_Watt','OP_VAH','OutputVolt','OutputCur','OutputPower','OutputFreq','OP_day','OP_hr','OP_min','OP_Warn','OP_Err','OP_PVEdaily','OP_Money','OP_CO2','PMV1','PMI1','PMHz','PMP1','PMPF','PMS1','PMQ1','WhL1','VAhL1','VARhL1','THD_I','Solar','W_Dir','W_Speed','Press','Out_Temp']:
                df[col] = df[col].astype(float)
        df.to_csv('C:/Users/Lenovo\'s user/Desktop/Solar_Mani/padded.csv', index=False)
