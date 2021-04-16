import os
from shutil import copyfile


def templates_recording(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.html'):
                dir name = os.path.join('templates', os.path.basename(root))
                if not os.path.exists(dir_name):
                    os.makedirs(dir_name)
                copyfile(os.path.join(root, file), os.path.join(dir_name, file))

if __name__ == '__main__':
    templates_recording('7.1_2/my_project')