import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='white')

all_df = pd.read_csv("main_data.csv", delimiter=",")  

st.sidebar.title("BIKE SHARING DASHBOARD")
analysis_option = st.sidebar.selectbox("Select Analysis", ["Summary", "Holiday vs Workingday", "Monthly Trend", "Seasonal Influences", "Weather Influences", "Hourly Trend"])

def main():
    st.title("Simple Bike Rental Dashboard")

    st.subheader("Data Preview")
    st.write(all_df.head())

    if analysis_option == "Summary":
        st.subheader("Data Summary")
        st.write(all_df.describe())
        

    elif analysis_option == "Holiday vs Workingday":
        # Jumlah
        st.subheader("Number of Bike Rentals by Holiday and Workingday")
        sum_rentals = all_df.groupby(['workingday_y'])['cnt_y'].sum()

        fig, ax = plt.subplots(figsize=(10, 5))
        sns.barplot(x=[0,1], y=sum_rentals.values, hue=sum_rentals.index, palette=["red","green" ])
        ax.set_title('Number of Bike Rentals by Holiday and Workingday')
        ax.set_xlabel('Days Category')
        ax.set_ylabel('Total Rentals')
        ax.set_xticks(ticks=[1,0])
        ax.set_xticklabels(['Working Day', 'Holiday'])
        st.pyplot(fig)
        
        # Rata-rata
        st.subheader("Average Bike Rentals by Holiday and Workingday")
        avg_rentals = all_df.groupby(['workingday_y'])['cnt_y'].mean()

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
        all_df['yr_y'] = all_df['yr_y'].replace({0: 2011, 1: 2012})
        monthly_rentals = all_df.groupby(['yr_y', 'mnth_y'])['cnt_y'].sum().reset_index()
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.lineplot(data=monthly_rentals, x='mnth_y', y='cnt_y', hue='yr_y', marker='o', ax=ax)
        ax.set_title('Total Bike Rentals by Month (2011-2012)')
        ax.set_xlabel('Month')
        ax.set_ylabel('Total Rentals')
        ax.set_xticks(range(1, 13))
        st.pyplot(fig)

    elif analysis_option == "Seasonal Influences":
        # Jumlah
        st.subheader("Number of Bike Rentals by Season")
        sum_season = all_df.groupby(['season_y'])['cnt_y'].sum()

        fig, ax = plt.subplots(figsize=(10, 5))
        sns.barplot(x=[0,1,2,3], y=sum_season.values, hue=sum_season.index, palette=["pink"])
        ax.set_title('Number of Bike Rentals by Season')
        ax.set_xlabel('Season Category')
        ax.set_ylabel('Total Rentals')
        ax.set_xticks(ticks=[0,1,2,3])
        ax.set_xticklabels(['Spring', 'Summer', 'Fall', 'Winter'])
        st.pyplot(fig)
        
        # Rata-rata
        st.subheader("Average Bike Rentals by Season")
        avg_season = all_df.groupby(['season_y'])['cnt_y'].mean()

        fig, ax = plt.subplots(figsize=(10, 5))
        sns.barplot(x=[0,1,2,3], y=avg_season.values, hue=avg_season.index, palette=["pink"])
        ax.set_title('Average Bike Rentals by Season')
        ax.set_xlabel('Season Category')
        ax.set_ylabel('Average Rentals')
        ax.set_xticks(ticks=[0,1,2,3])
        ax.set_xticklabels(['Spring', 'Summer', 'Fall', 'Winter'])
        st.pyplot(fig)

    elif analysis_option == "Weather Influences":
        # Jumlah
        st.subheader("Number of Bike Rentals by Weather")
        sum_weather = all_df.groupby(['weathersit_x'])['cnt_x'].sum()

        fig, ax = plt.subplots(figsize=(10, 5))
        sns.barplot(x=[0,1,2,3], y=sum_weather.values, hue=sum_weather.index, palette=["cyan"])
        ax.set_title('Number of Bike Rentals by Weather')
        ax.set_xlabel('Weather Category')
        ax.set_ylabel('Total Rentals')
        ax.set_xticks(ticks=[0,1,2,3])
        ax.set_xticklabels(['Good Weather', 'Moderate Weather', 'Unfavorable Weather', 'Bad Weather'])
        st.pyplot(fig)
        
        # Rata-rata
        st.subheader("Average Bike Rentals by Weather")
        avg_weather = all_df.groupby(['weathersit_x'])['cnt_x'].mean()

        fig, ax = plt.subplots(figsize=(10, 5))
        sns.barplot(x=[0,1,2,3], y=avg_weather.values, hue=avg_weather.index, palette=["cyan"])
        ax.set_title('Average Bike Rentals by Weather')
        ax.set_xlabel('Weather Category')
        ax.set_ylabel('Average Rentals')
        ax.set_xticks(ticks=[0,1,2,3])
        ax.set_xticklabels(['Good Weather', 'Moderate Weather', 'Unfavorable Weather', 'Bad Weather'])
        st.pyplot(fig)

    elif analysis_option == "Hourly Trend":
        #jumlah
        st.subheader("Total Bike Rentals by Day Type (Working Day / Holiday)")
        all_df['workingday_x'] = all_df['workingday_x'].replace({0: "holiday", 1: "workingday"})
        hourly_rentals_sum = all_df.groupby(['hr', 'workingday_x'])['cnt_x'].sum().reset_index()
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.lineplot(data=hourly_rentals_sum, x='hr', y='cnt_x', hue='workingday_x', marker='o', ax=ax)
        ax.set_title("Total Bike Rentals by Day Type (Working Day / Holiday)")
        ax.set_xlabel('Hour\'s')
        ax.set_ylabel('Total Rentals')
        ax.set_xticks(range(0, 24))
        st.pyplot(fig)

        #Rata-rata
        st.subheader("Average Bike Rentals by Day Type (Working Day / Holiday)")
        all_df['workingday_x'] = all_df['workingday_x'].replace({0: "holiday", 1: "workingday"})
        hourly_rentals_avg = all_df.groupby(['hr', 'workingday_x'])['cnt_x'].mean().reset_index()
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.lineplot(data=hourly_rentals_avg, x='hr', y='cnt_x', hue='workingday_x', marker='o', ax=ax)
        ax.set_title("Average Bike Rentals by Day Type (Working Day / Holiday)")
        ax.set_xlabel('Hour\'s')
        ax.set_ylabel('Average Rentals')
        ax.set_xticks(range(0, 24))
        st.pyplot(fig)
if __name__ == "__main__":
    main()
