import requests
import pandas as pd
import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt
import schedule
import time

# Function to fetch weather data
def fetch_weather_data(api_key, city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()

    weather_data = {
        "city": data["name"],
        "temperature": data["main"]["temp"] - 273.15,  # Convert from Kelvin to Celsius
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "weather": data["weather"][0]["description"],
        "datetime": datetime.now()
    }
    return weather_data

# Function to preprocess data
def preprocess_data(df):
    # Remove duplicates
    df = df.drop_duplicates()

    # Fill missing values
    df.fillna({
        "temperature": df["temperature"].mean(),
        "humidity": df["humidity"].median(),
        "pressure": df["pressure"].mean()
    }, inplace=True)

    # Ensure datetime format
    df["datetime"] = pd.to_datetime(df["datetime"])

    return df

# Function to save data to SQLite
def save_to_database(df, db_name, table_name):
    conn = sqlite3.connect(db_name)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()

# Function to analyze and visualize data
def analyze_data(df):
    print("Data Summary:\n", df.describe())

    # Plot temperature distribution
    plt.figure(figsize=(10, 5))
    plt.hist(df["temperature"], bins=15, color="skyblue", edgecolor="black")
    plt.title("Temperature Distribution")
    plt.xlabel("Temperature (°C)")
    plt.ylabel("Frequency")
    plt.show()

# Main function to automate the entire process
def main_process():
    API_KEY = '21c70daa2323041dca6bc3162953d9f3'  # Replace with your OpenWeather API key
    CITY = 'Almetyevsk'

    # Step 1: Fetch data
    weather_data = fetch_weather_data(API_KEY, CITY)
    
    # Step 2: Load data into DataFrame
    try:
        df = pd.read_csv("C:/Users/Диана/Desktop/ljvfir/weather_data.csv")
        df = pd.concat([df, pd.DataFrame([weather_data])], ignore_index=True)
    except FileNotFoundError:
        df = pd.DataFrame([weather_data])

    # Step 3: Preprocess data
    df = preprocess_data(df)

    # Step 4: Save processed data to CSV
    df.to_csv("C:/Users/Диана/Desktop/ljvfir/weather_data.csv", index=False)

    # Step 5: Save to database
    save_to_database(df, "C:/Users/Диана/Desktop/ljvfir/weather_data.db", "weather")

    # Step 6: Analyze data
    analyze_data(df)

# Execute the process once for testing
main_process()

# Uncomment for automated scheduling
# schedule.every().day.at("09:00").do(main_process)

# Uncomment below to keep the scheduler running
while True:
    schedule.run_pending()
    time.sleep(1)

print("Script executed once. Exiting.")
