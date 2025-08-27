from bson import ObjectId
from cleaning.cleaning_data import Cleaning_data
from pub.producer import Producer

class Manager:

    def __init__(self, topic):
        self.cleaning = Cleaning_data()
        self.producer = Producer()
        self.data_cleaning = []
        self.data = None
        self.topic = topic


    def start_the_cleaning_process(self, data_list : list):
        self.data = data_list
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
            print(self.data_cleaning)

        self.send_data_cleaning_to_mongodb()

    def change_name_column_text(self,row):
        row['original_text'] = row.pop('text')
        return row

    def send_data_cleaning_to_mongodb(self):
        self.producer.send_message(self.topic, self.data_cleaning)


