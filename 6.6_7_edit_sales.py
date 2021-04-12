import sys

LINE_LENGTH = 7


def edit_sales(line_from, new_rec):
    line_from -= 1  # required to be 1-indexed
    with open('bakery.csv', 'r+', encoding='utf-8') as f:
        f.seek(line_from * LINE_LENGTH)
        if not f.readline():
            print('Record does not exist')
            return
        f.seek(line_from * LINE_LENGTH)
        f.write(new_rec)


if __name__ == '__main__':
    _script_name, edit_from_line_from, new_rec = sys.argv
    edit_sales(int(edit_from_line_from), new_rec)
