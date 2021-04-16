import os
from pathlib import Path


def parse_yaml():
    with open('config.yaml', 'r', encoding='utf-8') as f:
        current_folder_path = Path.cwd()
        current_nest = 0
        for line in f:
            processed_line = line.strip('- : \n\r')
            if line.endswith(':\n'):
                if line.index('-') or current_nest == 0:
                    current_folder_path = current_folder_path.joinpath(processed_line)
                elif line.index('-') < current_nest * 2:
                    current_folder_path = Path(current_folder_path).parents[current_nest]
                os.mkdir(current_folder_path)
            else:
                file_name = current_folder_path.joinpath(processed_line)
                if not os.path.exists(file_name):
                    open(file_name, 'w').close()


if __name__ == '__main__':
    parse_yaml()
