import re

def clean_resume(text):
    clean_text = text
    clean_text = re.sub(r'â', '', clean_text)
    clean_text = re.sub(r'http\S+\s', '', clean_text)
    clean_text = re.sub(r'http\S+\s', '', clean_text)
    clean_text = re.sub(r'@\S+\s', '', clean_text)
    clean_text = re.sub(r'#\S+\s', '', clean_text)
    clean_text = re.sub(r'RT[\s]+', '', clean_text)
    clean_text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), '', clean_text)
    clean_text = re.sub('\s+', ' ', clean_text)

    return clean_text

def read_category_from_json(file_name):
    import json
    import os

    if not os.path.isfile(file_name):
        raise FileNotFoundError(file_name + " not found")

    with open(file_name, 'r') as f:
        data = json.load(f)

    return data

def get_category_by_id(id):
    return read_category_from_json("category.json").get(str(id), "Unknown")
