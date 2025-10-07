from http.server import HTTPServer, BaseHTTPRequestHandler
import os


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            template_file = 'templates/index.html'
        elif self.path == '/catalog':
            template_file = 'templates/catalog.html'
        elif self.path == '/category':
            template_file = 'templates/category.html'
        elif self.path == '/contacts':
            template_file = 'templates/contacts.html'
        else:
            template_file = 'templates/index.html'

        try:
            with open(template_file, 'r', encoding='utf-8') as file:
                html_content = file.read()

            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(html_content.encode('utf-8'))

        except FileNotFoundError:
            self.send_error(404, "File not found")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        print("POST данные получены:")
        print("=" * 50)
        print(post_data.decode('utf-8'))
        print("=" * 50)

        try:
            with open('templates/contacts.html', 'r', encoding='utf-8') as file:
                html_content = file.read()

            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(html_content.encode('utf-8'))

        except FileNotFoundError:
            self.send_error(404, "File not found")


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class) # type: ignore
    print('Сервер запущен на http://localhost:8000')
    print('Доступные страницы:')
    print('- http://localhost:8000/ (Главная)')
    print('- http://localhost:8000/catalog (Каталог)')
    print('- http://localhost:8000/category (Категория)')
    print('- http://localhost:8000/contacts (Контакты)')
    httpd.serve_forever()


if __name__ == '__main__':
    run()
