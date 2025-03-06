import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='white')

day_df = pd.read_csv("main_data.csv", delimiter=",")  

st.sidebar.title("BIKE SHARING DASHBOARD")
analysis_option = st.sidebar.selectbox("Select Analysis", ["Summary", "Holiday vs Workingday", "Monthly Trend"])

def main():
    st.title("Simple Bike Rental Dashboard")

    st.subheader("Data Preview")
    st.write(day_df.head())

    if analysis_option == "Summary":
        st.subheader("Data Summary")
        st.write(day_df.describe())

    elif analysis_option == "Holiday vs Workingday":
        st.subheader("Average Bike Rentals by Holiday and Workingday")
        avg_rentals = day_df.groupby(['workingday'])['cnt'].mean()

        fig, ax = plt.subplots(figsize=(10, 5))
        sns.barplot(x=[0,1], y=avg_rentals.values, hue=avg_rentals.index, palette=["red","green" ])
        ax.set_title('Average Bike Rentals by Holiday and Workingday')
        ax.set_xlabel('Days Category')
        ax.set_ylabel('Average Rentals')
        ax.set_xticks(ticks=[1,0])
        ax.set_xticklabels(['Working Day', 'Holiday'])
        st.pyplot(fig)
        
    elif analysis_option == "Monthly Trend":
        st.subheader("Total Bike Rentals by Month (2011-2012)")
        monthly_rentals = day_df.groupby(['yr', 'mnth'])['cnt'].sum().reset_index()
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.lineplot(data=monthly_rentals, x='mnth', y='cnt', hue='yr', marker='o', ax=ax)
        ax.set_title('Total Bike Rentals by Month (2011-2012)')
        ax.set_xlabel('Month')
        ax.set_ylabel('Total Rentals')
        ax.set_xticks(range(1, 13))
        st.pyplot(fig)

if __name__ == "__main__":
    main()