from Preprocessor.additional_features.additionalfeatures import AdditionalFeatures
from Preprocessor.preprocessor_pub.preprocessor_producer import Producer


class Manager:

    def __init__(self):
        self.additional = AdditionalFeatures()
        self.producer = Producer()
        self.data = None
        self.antisemietic = False

    def start_the_cleaning_process(self, data_list : list):
        self.data = data_list
        if self.data[0]["Antisemitic"] == 1:
            self.antisemietic = True
        else:
            self.antisemietic = False
        for i in self.data:
            text = i["clean_text"]
            i["sentiment"] = self.additional.find_text_sentiment(text)
            i["weapons_detected"] = self.additional.check_if_weapons_exists(text)
            i["relevant_timestamp"] = self.additional.is_date(text)
        print(self.data)

        self.send_data_cleaning_to_mongodb()

    def send_data_cleaning_to_mongodb(self):
        if self.antisemietic:
            self.producer.send_message(self.get_topic_to_send_antisemitic(), {"result":self.data})
        else:
            self.producer.send_message(self.get_topic_to_send_not_antisemitic(), {"result":self.data})


    @staticmethod
    def get_topic_to_send_antisemitic():
        return 'enriched_preprocessed_tweets_antisemitic'

    @staticmethod
    def get_topic_to_send_not_antisemitic():
        return 'enriched_preprocessed_tweets_not_antisemitic'