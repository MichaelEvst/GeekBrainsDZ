TUTORS = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
CLASSES = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def list_zip():
    for index in range(len(TUTORS)):
        try:
            yield TUTORS[index], CLASSES[index]
        except IndexError:
            yield TUTORS[index], None


generator = list_zip()
print(*generator)