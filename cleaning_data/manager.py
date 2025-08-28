from cleaning_data.cleaning.cleaning_data import CleaningData
from cleaning_data.pub.producer import Producer

class Manager:

    def __init__(self):
        self.cleaning = CleaningData()
        self.producer = Producer()
        self.data_cleaning = []
        self.data = None


    async def start_the_cleaning_process(self, data_list : list):
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

        await self.send_data_cleaning_to_mongodb()

    def change_name_column_text(self,row):
        row['original_text'] = row.pop('text')
        return row

    async def send_data_cleaning_to_mongodb(self):
        await self.producer.send_message(self.get_topic_to_send_antisemitic(), self.data_cleaning)
        await self.producer.send_message(self.get_topic_to_send_not_antisemitic(), self.data_cleaning)

    @staticmethod
    def get_topic_to_send_antisemitic():
        return 'preprocessed_tweets_antisemitic'

    @staticmethod
    def get_topic_to_send_not_antisemitic():
        return 'preprocessed_tweets_not_antisemitic'

