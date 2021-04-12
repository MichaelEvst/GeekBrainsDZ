import sys
from itertools import zip_longest


def unite_users_with_hobbies(hobbies_file, users_file, output_file):
    with open(hobbies_file, 'r', encoding='utf-8') as hobbies_f, \
         open(users_file, 'r', encoding='utf-8') as user_f, \
         open(output_file, 'a', encoding='utf-8') as write_to_f:

        for initials, hobbies in zip_longst(user_f,hobbies_f):
            if initial is None:
                exit(1)
            else:
                initial = initials.strip()
                if hobbies is not None:
                    hobbies = hobbies.strip()
                write_to_f.write(f'{initials}: {hobbies}\n')


if __name__ == "__main__":
    _script_name, hobbies_file, users_file, output_file = sys.argv
    unite_users_with_hobbies(hobbies_file, users_file, output_file)
