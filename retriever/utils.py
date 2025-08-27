class Utils:

    @staticmethod
    def correct_the_id(result):
        for organ in result:
            organ['_id'] = str(organ['_id'])
            organ['CreateDate'] = str(organ['CreateDate'])
        return result