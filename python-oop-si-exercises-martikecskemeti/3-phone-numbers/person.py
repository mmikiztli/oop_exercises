class Person():
    _name = None
    _phone_number = None

    def __init__(self, name, phone_number):
        self._name = name
        self._phone_number = phone_number

    def is_phone_number_matching(self, input_phone_number):
        return self._phone_number == input_phone_number

    def get_name(self):
        return self._name

    @staticmethod
    def normalize_phone_number(phone_number):
        char = [" ", "  ", "-", "--"]
        phone_num = ""
        for num in phone_number:
            if num not in char:
                phone_num += num
        return phone_num
