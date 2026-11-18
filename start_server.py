# -*- coding: utf-8 -*-
"""
Lightweight local server for testing World of Warcraft 5.5e Reference Guide.
Finds an available port, serves index.html, and automatically launches the browser.
"""

import sys
import os
import socket
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler

def find_free_port(start_port=8080, max_port=8100):
    for port in range(start_port, max_port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('127.0.0.1', port)) != 0:
                return port
    return 0

def run():
    # Ensure current directory is the project directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    port = find_free_port(8080)
    if not port:
        print("[!] Не удалось найти свободный порт. Открываем index.html напрямую в браузере...")
        webbrowser.open("file://" + os.path.join(script_dir, "index.html"))
        return

    url = f"http://localhost:{port}/index.html"
    
    print("=" * 66)
    print("  World of Warcraft 5.5e • D&D 2024 Reference Guide")
    print("=" * 66)
    print(f"\n[+] Сервер успешно запущен на: {url}")
    print("[+] Открываем страницу в вашем браузере по умолчанию...")
    print("[*] Чтобы завершить работу сервера, нажмите Ctrl + C или закройте это окно.\n")

    # Open browser
    webbrowser.open(url)

    # Start HTTP Server
    server_address = ('127.0.0.1', port)
    class QuietHandler(SimpleHTTPRequestHandler):
        extensions_map = SimpleHTTPRequestHandler.extensions_map.copy()
        extensions_map['.webp'] = 'image/webp'

        def log_message(self, format, *args):
            # Print clean request logs
            sys.stdout.write(f"[{self.log_date_time_string()}] {args[0]} {args[1]}\n")

    httpd = HTTPServer(server_address, QuietHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[*] Сервер остановлен пользователем.")
        httpd.server_close()

if __name__ == "__main__":
    run()
