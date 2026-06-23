 Simple Web Text Searcher

Простой и мощный инструмент командной строки для поиска текста на веб-страницах.
 Особенности

- 🔍 Поиск по ключевому слову или фразе на указанной веб-странице.
- 🖥️ Интерфейс командной строки (CLI) для быстрого запуска.
- 📄 Сохранение результатов в текстовый файл.
- 🌐 Поддержка задержки между запросами для этичного сканирования.
- 🎨 Цветной вывод в терминале для лучшей читаемости.
- 🌍 Регистронезависимый поиск.

 Установка

Windows:
1. Скачайте и установите Python:
	Перейдите на официальный сайт Python(https://www.python.org/downloads/).
	Скачайте последнюю версию для Windows.
	ВАЖНО: При установке поставьте галочку "Add Python to PATH".
2. Скачайте проект:
	Нажмите зеленую кнопку Code на странице репозитория.
	Выберите "Download ZIP".
	Распакуйте архив в удобное место.
3. Откройте терминал:
	Перейдите в папку с проектом(где лежит scraper.py).
	Нажмите ПКМ и выберите "Открыть в терминале".
4. Установите зависимости: 
	pip install -r requirements.txt
5. Готово!

Linux(Ubuntu/Debian):
1. Установите Python(если еще не установлен):
	sudo apt update
	sudo apt install python3 python-pip
2. Скачайте проект:
	git clone https://github.com/Yarik528/Parser.git
	cd Parser
3. Установите зависимости:
	pip3 install -r requirements.txt(Или python3 -m pip install -r requirements.txt)
4. Готово!

Termux(Android):
1. Установите Python:
	pkg update 
	pkg install python
2. Клонируйте проект:
	pkg install git
	git clone https://github.com/Yarik528/Parser.git
	cd Parser
3. Установите зависимости:
	pip install -r requirements.txt
4. Готово!

	Использование: 
	python scraper.py --url <URL> --search "<текст для поиска>" [опциональные аргументы]
	
	Аргументы: 
	Аргумент	Сокращение	Описание										
	--url			-u				URL веб-страницы.
	--search 	-s 				Текст для поиска на странице.
	--output		-o				Путь к файлу для сохранения результатов. (по умолчанию: output/results.txt)
	--delay						Задержка между запросами в секундах. (по умолчанию: 1.0)
	
	Примеры:
Простой поиск: 
	python scraper.py --url "https://httpbin.org/html" --search "HTTPBin"
Поиск с сохранением в файл:
	python scraper.py --url "https://example.com" --search "More information" --output output/example_search.txt
Поиск с увеличенной задержкой:
	python scraper.py --url "https://slow-site.com" --search "news" --delay 3.0
	
	Результаты:
В терминале отображаються найденные совпадения с контекстом.
Всё, что найдено, сохраняется в указанный файл .txt.
Формат файла:
URL: <адрес сайта>
Поиск: <текст поиска>
Найденные совпадения:
  [1] ...<контекст до> <искомый текст> <контекст после>...
  ...
Всего совпадений: <число>
--------------------------------------------------