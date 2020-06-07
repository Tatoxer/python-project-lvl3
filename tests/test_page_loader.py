from page_loader.page import create_outputs, download_page
import tempfile


def test_folder_name():
    url = "https://ru.wikipedia.org"
    folder_name, site_path = create_outputs(url, tempfile.TemporaryDirectory().name)
    expect = "ru-wikipedia-org"
    assert expect == folder_name
