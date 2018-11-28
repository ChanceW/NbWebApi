import re


class Utilites:
    def preprocess_string(str_arg):
        cleaned_str = re.sub('[^a-z\s]+', ' ', str_arg, flags=re.IGNORECASE)
        cleaned_str = re.sub('(\s+)', ' ', cleaned_str)
        cleaned_str = cleaned_str.lower()
        return cleaned_str
