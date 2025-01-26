# Используем официальный образ Python
FROM python:3.10

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта
COPY . .

# Устанавливаем Playwright и браузеры
RUN pip install playwright
RUN playwright install --with-deps

# Запускаем тесты
CMD ["pytest", "tests/"]