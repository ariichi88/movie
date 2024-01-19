#! /usr/bin/env python3
# coding: UTF-8

import os
import sys
import datetime
import shutil
import re

FromDir = ''
ToDir = ''


def CheckDateFormat(date):
    res = re.match(r'20[0-9][0-9]/[0-1][0-9]/[0-3][0-9]', date)
    if res:
        return True
    else:
        return False


def CopyMp4Files(date, newname):
    datestr = date.replace('/', '-')
    fromfiles = [f for f in os.listdir(FromDir) if datestr in f]
    fromfiles.sort()
    for count, fromfile in enumerate(fromfiles):
        _, ext = os.path.splitext(fromfile)
        if 'jpg' in ext:
            pass
        else:
            tofile = newname + '-' + format(count + 1, '02') + ext
            shutil.copy2(FromDir + fromfile, ToDir + '/' + tofile)


if __name__ == '__main__':
    arg = sys.argv
    if len(arg) == 2:
        dt = datetime.datetime.now()
        date = dt.strftime('%Y/%m/%d')
        name = arg[1]
    elif len(arg) == 3:
        date = arg[1]
        name = arg[2]
    else:
        print('使用法　movie.py [date] newname')
        print('日付のフォーマットyyyy/mm/dd')
        sys.exit(1)
    if CheckDateFormat(date):
        CopyMp4Files(date, name)
    else:
        print('日付のフォーマットが違います')
        print('フォーマット yyyy/mm/dd')
        sys.exit(1)
