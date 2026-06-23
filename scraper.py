import requests
from bs4 import BeautifulSoup
import argparse
import os
from urllib.parse import urljoin, urlparse
import time
from colorama import init, Fore, Style
import random

# Инициализация colorama для цветного вывода
init(autoreset=True)

# Список User-Agent для ротации
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
]

def search_in_page(url, search_text, headers=None, delay=1):
    """Ищет текст на странице"""
    print(f"{Fore.CYAN}🌐 Сканирую: {url}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}🔍 Ищу: '{search_text}'{Style.RESET_ALL}")
    
    if headers is None:
        headers = {'User-Agent': random.choice(USER_AGENTS)}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Получаем весь текст со страницы
        page_text = soup.get_text(separator=' ', strip=True)
        
        # Ищем все вхождения (регистронезависимо)
        search_lower = search_text.lower()
        text_lower = page_text.lower()
        
        occurrences = []
        start = 0
        while True:
            pos = text_lower.find(search_lower, start)
            if pos == -1:
                break
            # Находим начало и конец предложения/абзаца
            start_context = max(0, pos - 100)
            end_context = min(len(page_text), pos + len(search_text) + 100)
            # Обрезаем по границе слов
            context = page_text[start_context:end_context]
            occurrences.append(context)
            start = pos + 1

        time.sleep(delay) # Задержка между запросами
        return occurrences
        
    except requests.RequestException as e:
        print(f"{Fore.RED}❌ Ошибка при запросе к {url}: {e}{Style.RESET_ALL}")
        return []

def save_to_txt(url, search_text, occurrences, output_filename):
    """Сохраняет результаты в формате .txt"""
    output_dir = os.path.dirname(output_filename) or "."
    os.makedirs(output_dir, exist_ok=True)

    with open(output_filename, 'a', encoding='utf-8') as f: # 'a' для добавления в конец файла
        f.write(f"URL: {url}\n")
        f.write(f"Поиск: {search_text}\n")
        f.write("Найденные совпадения:\n")
        if occurrences:
            for i, context in enumerate(occurrences, 1):
                f.write(f"  [{i}] ...{context}...\n")
        else:
            f.write("  Совпадений не найдено.\n")
        f.write(f"Всего совпадений: {len(occurrences)}\n")
        f.write("-" * 50 + "\n") # Разделитель между результатами

def main():
    parser = argparse.ArgumentParser(description="Простой веб-скрапер (поиск текста)")
    parser.add_argument("--url", "-u", required=True, help="URL для сканирования")
    parser.add_argument("--search", "-s", required=True, help="Текст для поиска")
    parser.add_argument("--output", "-o", default="output/results.txt", help="Путь к файлу вывода (default: output/results.txt)")
    parser.add_argument("--delay", type=float, default=1.0, help="Задержка между запросами в секундах (default: 1.0)")

    args = parser.parse_args()

    url = args.url
    search_text = args.search
    output_file = args.output
    delay = args.delay

    # Поиск
    occurrences = search_in_page(url, search_text, delay=delay)

    # Вывод в терминал
    print(f"\n--- РЕЗУЛЬТАТЫ для {url} ---")
    print(f"URL: {url}")
    print(f"Поиск: {search_text}")
    print("Найденные совпадения:")
    if occurrences:
        for i, context in enumerate(occurrences, 1):
            print(f"  [{i}] ...{context}...")
    else:
        print("  Совпадений не найдено.")
    print(f"Всего совпадений: {len(occurrences)}")
    print("-" * 30)

    # Сохранение в файл
    save_to_txt(url, search_text, occurrences, output_file)
    print(f"{Fore.GREEN}✅ Результаты сохранены в: {output_file}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()