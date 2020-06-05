import os.path
import re
import requests


def create_outputs(url, directory=os.getcwd()):
    folder_name = re.sub(r"https://|http://", "", url)
    folder_name = re.sub(r"\W", "-", folder_name)

    try:
        os.mkdir(directory + "/" + folder_name)
    except FileExistsError:
        print(f"Directory '{folder_name}' is already existing")

    site_path = os.path.join(directory, folder_name + "/")
    return folder_name, site_path


def download_page(url, folder_name, site_path):
    r = requests.get(url)

    with open(site_path + folder_name + ".html", "w") as f:
        f.write(r.text)
    print(f"Page '{folder_name}' was downloaded here: {site_path}")



# s_dir, f_name, s_path = create_outputs(url)
# download_page('https://ru.wikipedia.org', f_name, s_path)
