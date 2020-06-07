from page_loader.page import create_outputs, download_page
import tempfile

LINKS = [
    ("https://ru.wikipedia.org", "ru-wikipedia-org"),
    ("https://yandex.ru", "yandex-ru"),
    ("https://www.kinopoisk.ru/media/rubric/31", "www-kinopoisk-ru-media-rubric-31"),
    ("https://yandex.ru/collections/card/5d68233ec9270d3cec923c7f/",
     "yandex-ru-collections-card-5d68233ec9270d3cec923c7f-"),

]


def test_folder_name():
    for (link, result) in LINKS:
        url = link
        temp_dir = tempfile.TemporaryDirectory()
        folder_name, site_path = create_outputs(url, temp_dir.name)
        expect = result
        assert expect == folder_name
