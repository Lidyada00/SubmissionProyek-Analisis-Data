import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt

# load data 
@st.cache_data
def loaddata(filepath):
    data = pd.read_csv(filepath)
    data["dteday"] = pd.to_datetime(data["dteday"])
    return data

data = loaddata("./data/day.csv")

# create title 
st.title('Dashboard')

st.sidebar.header("select day ranges")

startdate = st.sidebar.date_input('startdate',data['dteday'].min())
enddate = st.sidebar.date_input('startdate',data['dteday'].max())

startdate = pd.to_datetime(startdate)
enddate = pd.to_datetime(enddate)
filterdata = data[(data['dteday'] >= startdate) & (data['dteday'] <= enddate)]
st.write('### rawdata')
st.write(filterdata.head())

# visualisasi data 
st.write('### Berapa banyak peminjaman sepeda di kondisi cuaca salju ?')
plt.figure(figsize=(8,4))
plt.bar(filterdata['weathersit'].value_counts().index, filterdata['weathersit'].value_counts().values, tick_label=['Cerah','Mendung','Salju'], color=['#dfdfdf', 'grey','blue'])
plt.xlabel("weather condition", fontsize = "x-large")
plt.ylabel("count of rented bike", fontsize = "x-large")
st.pyplot(plt)

# visualisasi data 2 
st.write('### Berapa banyak peminjaman sepeda saat libur ?')
plt.figure(figsize=(8,4))
plt.bar(filterdata['workingday'].value_counts().index, filterdata['workingday'].value_counts().values, tick_label=['weekday', 'weekend'], color=['grey','blue'])
plt.xlabel("Workingday Condition", fontsize = "x-large")
plt.ylabel("count of Rental Bike", fontsize = "x-large")
st.pyplot(plt)

st.write("### Conclusion")
st.write("##### 1. Jumlah peminjaman di sepeda dicuaca Salju sebanyak 21.")
st.write("##### 2. Jumlah peminjaman di hari libur sebanyak 231.")