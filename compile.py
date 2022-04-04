"""
Compiles library to dist.
"""

import shutil
import os

for f_ in ('dist', 'dist/commonunicode/', 'dist/commonunicode/doc', 'dist/commonunicode/latex'):
    if os.path.isdir(f_):
        continue
    os.mkdir(f_)


def copy_file(f: str, path: str) -> None:
    """
    Copy file to path.
    """
    shutil.copyfile(f, f'{path}/{f}')


copy_file('commonunicode.tex', 'dist/commonunicode/doc')
copy_file('commonunicode.pdf', 'dist/commonunicode/doc')
copy_file('commonunicode.sty', 'dist/commonunicode/latex')
copy_file('LICENSE', 'dist/commonunicode/')
copy_file('README.md', 'dist/commonunicode/')

shutil.make_archive('commonunicode', 'zip', 'dist')
