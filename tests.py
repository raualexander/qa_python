from main import BooksCollector
import pytest


class TestBooksCollector:

    """проверяем добавление книг в пределах допустимых границ длинны имени"""
    valid_names = ['a', 'ум',
                   'Спокойствие внутри, вдохновение вокруг.',
                   'Спокойствие внутри, вдохновение вокруг.2'
                  ]

    @pytest.mark.parametrize('book', valid_names)
    def test_add_new_book_add_two_books(self, book):
        collector = BooksCollector()
        collector.add_new_book(book)
        assert len(collector.get_books_genre()) == 1

    """проверяем добавление книг в границах недопустимой длинны имен"""
    invalid_names = ['',
                     'В мире чудес открываются двери к новым пр',
                     'В мире чудес открываются двери к новым при'
                    ]
    @pytest.mark.parametrize('book', invalid_names)
    def test_add_new_book_add_book_with_long_name(self, book):
        collector = BooksCollector()
        collector.add_new_book(book)
        assert len(collector.get_books_genre()) == 0

    """добавляем уже добавленную книгу"""
    def test_add_new_book_add_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_new_book('1984')
        assert len(collector.get_books_genre()) == 1

    """присваиваем жанр книге"""
    def test_set_book_genre_set_existing_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'

    """присваиваем несуществующий жанр"""
    def test_set_book_genre_not_existing_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Нуар')
        assert collector.get_book_genre('Гарри Поттер') is ''

    """присваиваем жанр несуществующей книге"""
    def test_set_book_genre_not_existing_book(self):
        collector = BooksCollector()
        collector.set_book_genre('Властелин колец', 'Фантастика')
        assert collector.get_book_genre('Властелин колец') is None

    """проверяем фильтрацию по жанру"""
    def test_get_books_with_specific_genre_two_books_with_one_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Властелин колец', 'Комедии')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Гарри Поттер']

    """проверка возврата пустого списка для пустой библиотки"""
    def test_get_books_with_specific_genre_empty_book_list_nonexistent_genre(self):
        collector = BooksCollector()
        assert collector.get_books_with_specific_genre('Фантастика') == []

    """проверка вывода книг для детей"""
    def test_get_books_for_children_two_books_in_library(self):
        collector = BooksCollector()
        collector.add_new_book('Колобок')
        collector.add_new_book('Оно')
        collector.set_book_genre('Колобок', 'Мультфильмы')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_books_for_children() == ['Колобок']

    """проверка вывода пустого списка для пустой библиотеки"""
    def test_get_books_for_children_empty_list(self):
        collector = BooksCollector()
        assert collector.get_books_for_children() == []

    """проверка доюавления книги в избранное"""
    def test_add_book_in_favorites_add_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Первая научная история войны 1812 года')
        collector.add_book_in_favorites('Первая научная история войны 1812 года')
        assert collector.get_list_of_favorites_books() == ['Первая научная история войны 1812 года']

    """пустой список при попытке добавить несуществующую книгу"""
    def test_add_book_in_favorites_nonexistent_book(self):
        collector = BooksCollector()
        collector.add_new_book('Первая научная история войны 1812 года')
        collector.add_book_in_favorites('Гарри Поттер')
        assert collector.get_list_of_favorites_books() == []

    """проверка повторного добавления книги в избранное"""
    def test_add_book_in_favorites_add_same_book(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Оно')
        collector.add_book_in_favorites('Оно')
        assert len(collector.get_list_of_favorites_books()) == 1

    """удаление книги из избранного"""
    def test_delete_book_from_favorites_delete_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Колобок')
        collector.add_new_book('Оно')
        collector.delete_book_from_favorites('Оно')
        assert 'Оно' not in collector.get_list_of_favorites_books()
