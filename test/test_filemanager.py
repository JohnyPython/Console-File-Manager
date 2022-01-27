# console file manager functions test
from victory import date_to_str
from main_main import separator
from filemanager import author_info
from console_functions import directory_content


def test_date_str_one():
    assert (date_to_str('26.06.1799')) == 'двадцать шестое июня 1799 года'


def test_date_str_two():
    assert (date_to_str('04.02.1960')) == 'четвертое февраля 1960 года'


def test_separator():
    assert separator(4) == '****'


def test_separator_two():
    assert type(separator(4)) == str


def test_author_info():
    assert author_info() == 'Leonid Orlov'


def test_author_info_two():
    assert type(author_info()) == str


def test_directory_content():
    assert type(directory_content()) == list


