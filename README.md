# Q️A-web-test-task

Откройте ссылку https://s3.eu-central-1.amazonaws.com/qa-web-test-task/1.html
На странице присутствует ссылка, которая ведёт на следующую страницу.
И так далее до последней страницы, на которой написано, что она последняя.
Проверьте все страницы на наличие ссылок. Если есть страницы без ссылок, укажите их номера.
Опишите выбранный вами способ проверки по шагам, чтобы любой пользователь смог воспроизвести ваши действия.

### 📓 Description

Для решения задачи написан скрипт на python (aiohttp, asyncio), который асинхронно запрашивает и собирает содержимое веб-страниц, проверяет html-заголовки на наличие ссылки на следующую страницу и выдает результат в терминал: время исполнения скрипта и номера страниц без ссылок. 

### ❗ Prerequisites 
* Python 3.7+ installed
* Git, Cmd, Python basics understanding

### 🛠️ Installation steps 

1. Clone the repository

```
git clone https://github.com/hx-m/qa-web-test-task
```

2. Change the working directory

```
cd qa-web-test-task
```

3. Install the requirements

```
pip install -r requirements.txt
```

4. Run the app using terminal

```
python qa-web-test-task.py
```

### 🚀 Run example

**\qa-web-test-task> python qa-web-test-task.py**   
```
Sending requests and collecting responses...

Preparing of result...

Web test #0 completed:
Execution time: 8.453 seconds
List of page numbers with missed links: [8543, 9999]
```
