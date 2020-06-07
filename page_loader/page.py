import os.path
import re
import requests


def create_outputs(url, directory=os.getcwd()):
    folder_name = re.sub(r"https://|http://", "", url)
    folder_name = re.sub(r"\W", "-", folder_name)

    try:
        os.mkdir(directory + "/" + folder_name)
    except FileExistsError:
        print(f"Page was placed at '{folder_name}'")

    site_path = os.path.join(directory, folder_name + "/")
    return folder_name, site_path


def download_page(url, directory=os.getcwd()):
    try:
        r = requests.get(url)
        folder_name, site_path = create_outputs(url, directory)
        with open(site_path + folder_name + ".html", "w") as f:
            f.write(r.text)
        print(f"Page '{folder_name}' was downloaded here: {site_path}")

    except requests.exceptions.ConnectionError:
        print("Something went wrong, check your URL")
