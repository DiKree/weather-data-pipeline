Описание проекта
Название проекта:
"Автоматизированный сбор, анализ и визуализация погодных данных"

Цель проекта:
Создание автоматизированного пайплайна для сбора, предобработки, анализа и хранения погодных данных из внешнего API с возможностью визуализации через интерактивный дашборд. Это позволит анализировать погодные данные для конкретного города, хранить их для долгосрочного использования, а также предоставлять доступ к ключевым метрикам в удобной форме.

Этапы выполнения:
1. Сбор данных:
Данные о погоде собираются с использованием OpenWeather API.
Запросы отправляются автоматически с заданной периодичностью (ежедневно), а результаты сохраняются.
2. Предобработка данных:
Удаление дубликатов.
Заполнение пропущенных значений средними/медианными показателями.
Приведение формата даты и времени к стандартному ISO 8601.
3. Исследовательский анализ данных:
Расчет базовых статистик (средние значения, медианы, стандартное отклонение и т.д.).
Построение графиков распределения температуры для визуального анализа.
4. Метрики качества данных:
Оценка качества данных ведется по следующим критериям:

Полнота: Отсутствие пропущенных значений после обработки.
Достоверность: Сравнение данных с фактическими условиями.
Согласованность: Единые форматы данных и отсутствие дублирующих записей.
5. Разработка базы данных:
Реализовано хранение данных в базе SQLite.
Структура базы данных включает следующие столбцы:
"город", "температура", "влажность", "давление", "состояние погоды", "время записи".
6. Автоматизация пайплайна:
Все этапы автоматизированы с использованием библиотеки schedule.
Скрипт выполняется ежедневно в заданное время, автоматически собирая данные, обрабатывая их и сохраняя в базу данных.
7. Визуализация через интерактивный дашборд:
Интерактивный дашборд разработан с использованием библиотеки Streamlit.
Основные возможности дашборда:
Отображение таблицы собранных данных в реальном времени.
Визуализация графиков:
Температура: Построение тренда температуры по времени.
Влажность: Анализ изменения влажности в течение времени.
Бизнес-ценность проекта:
Проект предоставляет инструмент для анализа погодных данных, который может быть полезен:

Для мониторинга погодных условий в реальном времени.
Для компаний, чья деятельность зависит от погоды (аграрный сектор, логистика, туризм и т.д.).
Для построения долгосрочных аналитических моделей на основе исторических данных о погоде.
Для визуализации и принятия решений на основе графического представления данных.
Технологии, использованные в проекте:
Язык программирования: Python.
Библиотеки:
requests – для работы с API.
pandas – для работы с табличными данными.
matplotlib – для базовой визуализации.
sqlite3 – для работы с базой данных SQLite.
schedule – для автоматизации пайплайна.
streamlit – для разработки интерактивного дашборда.
Как использовать проект:
Клонируйте репозиторий:

git clone https://github.com/DiKree/weather-data-pipeline.git
Установите зависимости:

pip install -r requirements.txt
Запустите основной скрипт для сбора данных:

python weather_script.py
Запустите дашборд для визуализации данных:


streamlit run dashboard.py
Анализируйте данные через интерактивный дашборд или файл weather_data.db.

Этот проект является отличной основой для дальнейшего расширения, включая добавление прогнозов погоды и интеграцию с более сложными аналитическими системами.
