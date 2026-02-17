# UI Automation Sandbox Practice 🚀

Репозиторий содержит набор автоматизированных UI-тестов для отработки навыков тестирования веб-интерфейсов на платформе [AQA-Proka4 Sandbox](https://aqa-proka4.org/sandbox/web#forms).

**Стек технологий:**
*   **Language:** Python 3.12+
*   **Framework:** [Pytest](https://docs.pytest.org/)
*   **Automation Tool:** [Playwright](https://playwright.dev/python/)

---

## Установка и настройка 🛠

1. **Клонируйте репозиторий:**
   ```
   git clone https://github.com/sharaplnr/web-elements-practice-playwright.git
   cd aqa-sandbox-practice

2. **Создайте и активируйте виртуальное окружение:**
    ```
    python -m venv venv
    source venv/bin/activate  # для macOS/Linux
    venv\Scripts\activate     # для Windows

3. **Установите зависимости:**
    ```bash
    pip install -r requirements.txt

4. **Установите браузеры Playwright:**
    ```bash
   playwright install chromium

## Запуск тестов 🚀

1. **Локальный запуск (в обычном режиме):**
    ````
    pytest

2. **Запуск тестов в режиме Headed (с визуализацией):**
    ````
    pytest --headed
   
3. **Генерация Allure-отчета:**
    ````
    pytest --alluredir=allure-results
    allure serve allure-results