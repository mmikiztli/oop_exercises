import csv
import sys
from person import Person


def open_csv(file_name):
    with open(file_name) as f:
        rows = f.readlines()
    lines = [row.split(",") for row in rows]
    return [Person(person[0], person[1]) for person in lines]


def get_csv_file_name(argv_list):
    try:
        return argv_list[1]
    except IndexError:
        return None


def format_output(person):
    if person != None:
        return "This number belongs to: " + person.get_name()
    else:
        return 'No match found.'


def get_person_by_phone_number(person_list, user_input_phone_number):
    for person in person_list:
        if person.is_phone_number_matching(user_input_phone_number):
            return person


def get_person_by_chunk_number(person_list, user_input_chunk_number):  # Extra feature
    owners = []
    for person in person_list:
        if person.is_phone_number_matching_start(user_input_chunk_number):
            owners.append(person.get_name())
    return owners


def main():
    file_name = get_csv_file_name(sys.argv)
    if file_name is None:
        print('No database file was given.')
        sys.exit(0)

    person_list = open_csv(file_name)
    user_input_phone_number = input('Please enter the phone number: ')
    match_person = get_person_by_phone_number(
        person_list, user_input_phone_number)

    print(format_output(match_person))

if __name__ == '__main__':
    main()
