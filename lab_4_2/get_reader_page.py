###########################
###########################
######## Задание 2 ########
###########################
###########################

from jinja2 import Template
import sqlite3
from model.reader_book_model import *

# задаем id читателя, для которого формируем страницу
reader_id = 3

conn = sqlite3.connect("../library.sqlite")
# выбираем записи о том, какие книги брал читатель с параметром reader_id
# столбцы назвать Название, Авторы, Дата_выдачи, Дата_сдачи
df_book_reader = get_book_reader(conn, reader_id)

# выбираем записи из таблицы reader для формирования поля со списком
df_reader = get_reader(conn)
conn.close()

f_template = open("../template/reader_book_templ.html")
html = f_template.read()
f_template.close()

# создаем объект-шаблон
template = Template(html)

result_html = template.render(
    reader_id=reader_id,
    combo_box=df_reader,
    book_reader=[df_book_reader],
    table_name=["Карточка"],
    len=len,
    zip=zip
)

f = open('../reader_book.html', 'w', encoding='utf-8-sig')
f.write(result_html)
f.close()
