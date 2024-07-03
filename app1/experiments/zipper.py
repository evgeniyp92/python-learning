import os
import sys
import zipfile
import pathlib


def make_arch(filepaths, dest):
    dest_path = pathlib.Path(dest, 'compressed.zip')
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath)


if __name__ == '__main__':
    make_arch(filepaths=["bonus1.py", "b2.py", "bonus3.py"], dest=os.getcwd())
