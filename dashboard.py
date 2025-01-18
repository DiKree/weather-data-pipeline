import sqlite3
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Заголовок дашборда
st.title("Дашборд данных о погоде")

# Подключение к базе данных
conn = sqlite3.connect("weather_data.db")
query = "SELECT * FROM weather"
df = pd.read_sql_query(query, conn)

# Отображение данных
st.subheader("Таблица данных")
st.dataframe(df)

# Визуализация данных
st.subheader("Графики данных")

# Температура
fig, ax = plt.subplots()
ax.plot(pd.to_datetime(df["datetime"]), df["temperature"], label="Температура (°C)")
ax.set_xlabel("Дата")
ax.set_ylabel("Температура (°C)")
ax.legend()
st.pyplot(fig)

# Влажность
fig, ax = plt.subplots()
ax.plot(pd.to_datetime(df["datetime"]), df["humidity"], label="Влажность (%)", color="blue")
ax.set_xlabel("Дата")
ax.set_ylabel("Влажность (%)")
ax.legend()
st.pyplot(fig)

# Закрытие соединения с БД
conn.close()
