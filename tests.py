from main import BooksCollector
import pytest


class TestBooksCollector:

    #добавляем 2 книги в библиотеку
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre) == 2

    #добавляем недопустимо длинное название
    def test_add_new_book_add_book_with_long_name(self):
        collector = BooksCollector()
        collector.add_new_book('очень длинное название произведениия которое не должен пропустить метод')
        collector.add_new_book('Нормальное название')
        assert len(collector.books_genre) != 2

    #добавляем уже добавленную книгу
    def test_add_new_book_add_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_new_book('1984')
        assert len(collector.books_genre) != 2

    #присваиваем жанр книге
    def test_set_book_genre_set_existing_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.books_genre.get('Гарри Поттер') == 'Фантастика'

    #присваиваем несуществующий жанр
    def test_set_book_genre_not_existing_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Нуар')
        assert not collector.get_book_genre('Гарри Поттер')

    #присваиваем жанр несуществующей книге
    def test_set_book_genre_not_existing_book(self):
        collector = BooksCollector()
        collector.set_book_genre('Властелин колец', 'Фантастика')
        assert not collector.get_book_genre('Властелин колец')

    #проверяем вывод двух книг одного жанра
    def test_get_books_with_specific_genre_two_books_with_one_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert len(collector.get_books_with_specific_genre('Фантастика')) == 2

    #проверка возврата пустого списка для пустой библиотки
    @pytest.mark.parametrize('genre', ['Фантастика', 'Комиксы'])
    def test_get_books_with_specific_genre_empty_book_list_nonexistent_genre(self, genre):
        collector = BooksCollector()
        assert collector.get_books_with_specific_genre(genre) == []

    #проверка вывода книг для детей
    def test_get_books_for_children_two_books_in_library(self):
        collector = BooksCollector()
        collector.add_new_book('Колобок')
        collector.add_new_book('Оно')
        collector.set_book_genre('Колобок', 'Мультфильмы')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_books_for_children() == ['Колобок']

    #проверка вывода пустого списка для пустой библиотеки
    def test_get_books_for_children_empty_list(self):
        collector = BooksCollector()
        assert collector.get_books_for_children() == []

    #проверка доюавления книги в избранное
    def test_add_book_in_favorites_add_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Первая научная история войны 1812 года')
        collector.add_book_in_favorites('Первая научная история войны 1812 года')
        assert collector.get_list_of_favorites_books() == ['Первая научная история войны 1812 года']

    #пустой список при попытке добавить несуществующую книгу
    def test_add_book_in_favorites_nonexistent_book(self):
        collector = BooksCollector()
        collector.add_new_book('Первая научная история войны 1812 года')
        collector.add_book_in_favorites('Гарри Поттер')
        assert collector.get_list_of_favorites_books() == []

    #проверка повторного добавления книги в избранное
    def test_add_book_in_favorites_add_same_book(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Оно')
        collector.add_book_in_favorites('Оно')
        assert len(collector.get_list_of_favorites_books()) == 1

    #удаление книги из избранного
    def test_delete_book_from_favorites_delete_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Колобок')
        collector.add_new_book('Оно')
        collector.delete_book_from_favorites('Оно')
        assert 'Оно' not in collector.get_list_of_favorites_books()
