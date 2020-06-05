import os.path
import re
import requests


url = 'https://ru.wikipedia.org'
folder_name = re.sub(r"https://|http://", "", url)
folder_name = re.sub(r"\W", "-", folder_name)
current_directory = os.getcwd()
try:
    os.mkdir(folder_name)
except FileExistsError:
    print(f"Directory '{folder_name}' is already existing")

site_path = os.path.join(current_directory, folder_name + "/")
r = requests.get(url)

with open(site_path + folder_name + ".html", "w") as f:
    f.write(r.text)
