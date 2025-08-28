import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import os
import spacy
from date_spacy import find_dates
nltk.download('vader_lexicon', quiet=True)


class AdditionalFeatures:
    def __init__(self):
        nltk_dir = "/tmp/nltk_data"
        os.makedirs(nltk_dir, exist_ok=True)
        nltk.data.path.append(nltk_dir)
        nltk.download('vader_lexicon', download_dir=nltk_dir, quiet=True)
        self.analyzer = SentimentIntensityAnalyzer()
        self.weapons = None
        self.name_file_weapons = "../additional_features/data_weapons/weapon_list.txt"


    def find_text_sentiment(self, text):
            score = SentimentIntensityAnalyzer().polarity_scores(text)["compound"]
            if score > .5:
                return "positive"
            elif score > -.5:
                return "neutral"
            else:
                return "negative"


    def check_if_weapons_exists(self, text):
        weapons = []
        if not self.weapons:
            self.read_weapons()
        for weapon in self.weapons:
            if weapon in text:
                weapons.append(weapon)
        if weapons:
            return weapons
        else:
            return ""

    def is_date(self, text):
        """

        """
        list_date = []
        nlp = spacy.blank('en')
        nlp.add_pipe('find_dates')

        doc = nlp(f"""{text}""")

        for ent in doc.ents:
            if ent.label_ == 'DATE':
                list_date.append(ent._.date)
        if list_date:
            return str(max(list_date))[:-9]
        else:
            return ""

    def read_weapons(self):
        weapons = []
        with open(self.name_file_weapons, "r", encoding='utf-8-sig') as f:
            while True:
                line = f.readline().strip("\n")
                if line == "":
                    break
                weapons.append(line)
        self.weapons = weapons
