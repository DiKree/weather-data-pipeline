import sqlite3

# Подключение к базе данных
conn = sqlite3.connect("C:/Users/Диана/Desktop/weather_data.db")
cursor = conn.cursor()

# Шаг 1: Проверка существующих таблиц
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Существующие таблицы:", tables)

# Шаг 2: Проверка содержимого таблицы
if ('weather',) in tables:
    cursor.execute("SELECT * FROM weather;")
    rows = cursor.fetchall()
    print("Содержимое таблицы weather:")
    for row in rows:
        print(row)
else:
    print("Таблица 'weather' не найдена.")

# Шаг 3: Проверка структуры таблицы
cursor.execute("PRAGMA table_info(weather);")
columns = cursor.fetchall()
print("Структура таблицы weather:")
for column in columns:
    print(column)

# Закрытие соединения
conn.close()
