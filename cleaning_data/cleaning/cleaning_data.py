import re
import nltk
import string
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger_eng')


class CleaningData:

    def __init__(self):
        pass

    def removing_punctuation_marks(self, text):
        # Create translation table
        translator = str.maketrans('', '', string.punctuation)

        # Remove punctuation
        clean_text = text.translate(translator)
        return clean_text

    def removing_special_characters(self, text):
        res = re.sub(r'[^a-zA-Z0-9]', ' ', text)
        return res

    def removing_unnecessary_whitespace(self, text):
        """
        ○ Removing unnecessary whitespace characters (tabs, long space sequences, all kinds of end-of-line characters).
        :return:
        """
        res = " ".join(text.split())
        return res

    def converting_text_to_lowercase(self, text):
        res = text.lower()
        return res

    def removing_stop_words(self, text):

        # Get English stopwords and tokenize
        stop_words = set(stopwords.words('english'))
        tokens = word_tokenize(text.lower())

        # Remove stopwords
        filtered_tokens = [word for word in tokens if word not in stop_words]

        res = " ".join(filtered_tokens)
        return res

    def lemtization(self, text):
        """
        ○ Lemtization (finding roots)
        :return:
        """
        lemmatizer = WordNetLemmatizer()

        tokens = word_tokenize(text)

        tagged_tokens = pos_tag(tokens)

        def get_wordnet_pos(tag):
            if tag.startswith('J'):
                return 'a'
            elif tag.startswith('V'):
                return 'v'
            elif tag.startswith('N'):
                return 'n'
            elif tag.startswith('R'):
                return 'r'
            else:
                return 'n'

        lemmatized_sentence = []

        for word, tag in tagged_tokens:
            if word.lower() == 'are' or word.lower() in ['is', 'am']:
                lemmatized_sentence.append(word)
            else:
                lemmatized_sentence.append(lemmatizer.lemmatize(word, get_wordnet_pos(tag)))

        res = " ".join(lemmatized_sentence)
        return res