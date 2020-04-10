import streamlit as st
import pandas as pd
import requests
from datetime import date
st.title("Covid 19 Tracker India")
st.text("Crowd Sourced Initiative")

url = "https://api.covid19india.org/data.json"

data = requests.get(url).json()
df = pd.DataFrame(data['statewise'])
df_2 = df[['state', 'confirmed', 'active', 'recovered', 'deaths', 'deltaconfirmed']]
df_2.columns = ['State', 'Confirmed Cases', 'Active Cases', 'Recovered Cases', 'Deaths', 'New Cases']
lastUpdate = str(df.loc[(df['statecode']=='TT')]['lastupdatedtime'].values)[1:-1]

total = df_2.loc[df_2['State']=='Total']
confirmed = int(total['Confirmed Cases'].values)
active = int(total['Active Cases'].values)
recovered = int(total['Recovered Cases'].values)
deaths = int(total['Deaths'].values)
new =  int(total['New Cases'].values)
st.write("Last Update: %s" %lastUpdate)
st.warning("Total Confirmed Cases: %s" %confirmed)
st.warning("Total Active Cases: %s" %active)
st.success("Total Recovered Cases: %s" %recovered)
st.error("Total Deseased: %s" %deaths)
st.info("New Cases Today: %s" %new)
st.header("Statewise Tracking")
Total = df_2.loc[df_2['State']=='Total']
#st.dataframe(df_2)
st.table(df_2.tail((len(df_2.index)-1)))