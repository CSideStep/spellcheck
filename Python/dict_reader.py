class dict_reader():
    path = "C:\\Info\\Projects\\spellcheck\\dictionary.txt"
    data = []
    def __init__(self):
        with open(self.path) as f:
            self.data = [word[:-2].lower() for word in f if not (word[:-2].lower() == "")]
    def get_data(self):
        return self.data