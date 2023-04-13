from pathlib import WindowsPath
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("C:\\Users\\pbarv\\OneDrive\\Desktop\\wsup\\vgsales.csv")
data = data.dropna()

st.sidebar.write(
    "change height and width of the last plot")
width = st.sidebar.slider("Width", min_value=6, max_value=20, value=10)
height = st.sidebar.slider("Height", min_value=1, max_value=10, value=3)







# # 7 Top 10 Stats in Tables
st.subheader("TOP 10 Games")
left, right = st.columns(2)

# 7.1 Top 10 Games by Platform
platform = sorted(data['Platform'].unique())
p = left.selectbox("Select platform", platform)
left.subheader("Top 10 Highest Grossing Games by platform")
# Making new dataframe with Platform equal to required platform
df = data.query("Platform == @p")
# Sorting the dataframe in decending order on GlobalSales
df = df.sort_values(by=['Global_Sales'], ascending=False)
df = df.iloc[:10]
df = df[['Name', 'Global_Sales']]
left.table(df)

# 7.2 Top 10 Games by Genre
genre = sorted(data['Genre'].unique())
g = right.selectbox("Select genre", genre, index=6)
right.subheader("Top 10 Highest Grossing Games by genre")
# making new dataframe with Genre equal to required genre
df01 = data.query("Genre == @g")
# sorting in decending order on GLobalSales
df01 = df01.sort_values(by=['Global_Sales'], ascending=False)
df01 = df01.iloc[:10]
df01 = df01[['Name', 'Global_Sales']]
right.table(df01)

st.markdown('###')

# # 8 Comparing Sales Data of 2 PUblishers
st.subheader("Comparing Salesdata of two Publishers")
publisher = sorted(data['Publisher'].unique())
left, right = st.columns(2)
# selecting two publishers
c1 = left.selectbox("Select 1st Publisher", publisher, index=21)
c2 = right.selectbox("Select 2nd Publisher", publisher, index=359)

# creating dataframes of 2 selected publishers
df1 = data.query("Publisher == @c1")
df2 = data.query("Publisher == @c2")

# Grouping the data by years
group1 = df1.groupby("Year").sum()
group2 = df2.groupby("Year").sum()

# Now Plotting
fig, ax = plt.subplots(figsize=(width, height))

ax.bar(group1.index-0.2, group1['Global_Sales'], 0.4, label=c1, color="red")
ax.bar(group2.index+0.2, group2['Global_Sales'],
       0.4, label=c2, color="blue")
ax.set_xlabel("Year")
ax.set_ylabel("Total Global Sales")
ax.legend()
st.pyplot(fig)
