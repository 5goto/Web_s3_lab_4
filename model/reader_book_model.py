import pandas as pd


def get_reader(conn):
    return pd.read_sql("SELECT * FROM reader", conn)


def get_book_reader(conn, reader_id):
    return pd.read_sql(f'''
        WITH concat_authors AS
        (SELECT book_id, title AS Название_книги, GROUP_CONCAT(author_name, ', ') as author_name
        FROM book
        natural JOIN book_author
        natural JOIN author
        GROUP BY title)
        select title as Название, concat_authors.author_name as Авторы ,borrow_date as Дата_выдачи, return_date as Дата_сдачи from book_reader
            natural join reader
            natural join book
            natural join concat_authors
            where reader_id = {reader_id}
    ''', conn)