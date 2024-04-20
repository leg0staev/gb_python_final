import os
from pathlib import Path
from collections import namedtuple


def dir_parser(directory=None):
    base_dir = Path.cwd()
    object_list = []
    OsObject = namedtuple('OsObject', ["object_name", "extension", "parent_dir"])

    if directory:
        base_dir = Path(directory)

    if not base_dir.exists():
        return object_list

    for root, dirs, files in os.walk(base_dir):
        for file in files:
            file_attrs = file.split('.')
            file_name = file_attrs[0]

            try:
                file_ext = file_attrs[1]
            except IndexError:
                file_ext = None

            obj = OsObject(file_name, file_ext, root.split('/')[-1])
            object_list.append(obj)

        for dir_ in dirs:
            obj = OsObject(dir_, 'dir', root.split('/')[-1])
            object_list.append(obj)

    return object_list


if __name__ == '__main__':
    print(dir_parser())
