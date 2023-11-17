##########################
###########################
######## Задание 1 ########
###########################
###########################

from jinja2 import Template
import sqlite3
from model.library_model import *



conn = sqlite3.connect("../library.sqlite")

df_publisher = get_publisher(conn)
df_genre = get_genre(conn)
df_book = get_book(conn)
df_author = get_author(conn)
df_book_author = get_book_author(conn)
df_book_reader = get_book_reader(conn)
df_reader = get_reader(conn)

conn.close()

# открываем шаблон из файла library_templ.html и читаем информацию
f_template = open("../template/library_templ.html")
html = f_template.read()
f_template.close()

# создаем объект-шаблон
template = Template(html)
# генерируем результат на основе шаблона
result_html = template.render(
    relations=[df_publisher, df_genre, df_reader, df_author, df_book, df_book_author, df_book_reader],
    table_name=["publisher", "genre", "reader", "author", "book", "book_author", "book_reader"],
    len=len,
    zip=zip
)

# создаем файл для HTML-страницы
f = open('../library.html', 'w', encoding='utf-8-sig')
# выводим сгенерированную страницу в файл
f.write(result_html)
f.close()
