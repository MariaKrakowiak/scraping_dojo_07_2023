import sys
from webbrowser import Chrome
import requests
from bs4 import BeautifulSoup
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import re
import json
import time
import os
from preparation.GetDetails import retrieve_authors, retrieve_texts, retrieve_tags, retrieve_list_of_dict
import settings


def browser_settings():
    """
    Browser settings
    :return:
    """
    ChromeOptions()
    Chrome(ChromeDriverManager().install())


def data_preparation():
    """
    1. Check the amount of websites that are available for given address (if content has no 'Next' button - stop searching)
    2. Find the key word 'Script' for each subpage and retrieve data matching the pattern
    3. Define temporary lists for data for each page
    4. Retrieve authors, tags and texts for each page
    5. Add authors, tags and texts for global list
    5. Prepare dictionary for data for each page
    6. Add dictionary for global list
    :return:
    """
    for i in range(1, sys.maxsize):
        url = str(os.getenv('INPUT_URL')) + 'page/{i}/'.format(i=i)
        time.sleep(15)
        content = str(requests.get(url).content)
        if 'Next' not in content:
            break
        else:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            script_tag = soup.find("script", src=None)

            pattern = "var data =(.+?);\n"
            raw_data = re.findall(pattern, script_tag.string, re.S)

            data = []
            author = []
            tag = []
            text = []

            if raw_data:
                data = json.loads(raw_data[0])

            settings.all_data.append(data)

            retrieve_authors(data, author)
            retrieve_tags(data, tag)
            retrieve_texts(data, text)

            settings.all_authors.append(author)
            settings.all_tags.append(tag)
            settings.all_texts.append(text)

            single_dict = retrieve_list_of_dict(author, tag, text)

            settings.overall_dict.extend(single_dict)

            i += 1
