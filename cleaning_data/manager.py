from cleaning_data.cleaning.cleaning_data import CleaningData
from cleaning_data.pub.producer import Producer

class Manager:

    def __init__(self):
        self.cleaning = CleaningData()
        self.producer = Producer()
        self.data_cleaning = []
        self.data = None
        self.antisemietic = False



    def start_the_cleaning_process(self, data_list : list):
        self.data = data_list
        if self.data[0]["Antisemitic"] == 1:
            self.antisemietic = True
        else:
            self.antisemietic = False
        for i in self.data:
            text = i["text"]
            text = self.cleaning.removing_punctuation_marks(text)
            text = self.cleaning.removing_special_characters(text)
            text = self.cleaning.removing_unnecessary_whitespace(text)
            text = self.cleaning.converting_text_to_lowercase(text)
            text = self.cleaning.removing_stop_words(text)
            text = self.cleaning.lemtization(text)

            new_i = self.change_name_column_text(i)

            self.data_cleaning.append(new_i)

            self.data_cleaning[-1]['clean_text'] = text

        self.send_data_cleaning_to_mongodb()

    def change_name_column_text(self,row):
        row['original_text'] = row.pop('text')
        row['id'] = row.pop('_id')
        return row

    def send_data_cleaning_to_mongodb(self):
        if self.antisemietic:
            self.producer.send_message(self.get_topic_to_send_antisemitic(), {"result": self.data})
        else:
            self.producer.send_message(self.get_topic_to_send_not_antisemitic(), {"result": self.data})

    @staticmethod
    def get_topic_to_send_antisemitic():
        return 'preprocessed_tweets_antisemitic'

    @staticmethod
    def get_topic_to_send_not_antisemitic():
        return 'preprocessed_tweets_not_antisemitic'

