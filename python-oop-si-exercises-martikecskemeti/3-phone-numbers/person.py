class Person():
    _name = None
    _phone_number = None

    def __init__(self, name, phone_number):
        self._name = name
        self._phone_number = self.normalize_phone_number(phone_number)

    def is_phone_number_matching(self, input_phone_number):
        return self._phone_number == self.normalize_phone_number(input_phone_number)

    def is_phone_number_matching_start(self, input_phone_number_start):
        normalized_start = self.normalize_phone_number(
            input_phone_number_start)
        return self._phone_number[:len(normalized_start)] == normalized_start

    def get_name(self):
        return self._name

    def get_phone_number(self):
        return self._phone_number

    @staticmethod
    def normalize_phone_number(phone_number):
        return phone_number.replace("-", "").replace(" ", "")
