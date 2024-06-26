import os
from pathlib import Path
import logging
from collections import namedtuple

LOG_FILENAME = 'log.log'

logging.basicConfig(filename=LOG_FILENAME,
                    filemode='w',
                    encoding='utf-8',
                    level=logging.INFO,
                    format='[ {levelname} ] {asctime}: {funcName} -> {msg}',
                    style='{')

logger = logging.getLogger(__name__)


def dir_parser(directory=None):
    base_dir = Path.cwd()
    object_list = []
    OsObject = namedtuple('OsObject', ["object_name", "extension", "parent_dir"])

    if directory:
        base_dir = Path(directory)

    if not base_dir.exists():
        logger.error(f'error - path "{base_dir}" does not exist')
        return object_list

    for root, dirs, files in os.walk(base_dir):

        for file in files:
            file_attrs = file.split('.')
            obj = OsObject(file_attrs[0] if len(file_attrs) == 1 else '.'.join(file_attrs[:-1]),
                           None if len(file_attrs) == 1 else file_attrs[-1],
                           root.split('/')[-1])
            logger.info(f'find OS object - {obj}')
            object_list.append(obj)

        for dir_ in dirs:
            obj = OsObject(dir_, 'dir', root.split('/')[-1])
            logger.info(f'find OS object - {obj}')
            object_list.append(obj)

    return object_list


if __name__ == '__main__':
    print(dir_parser())
