import os

from util.constants import *


# 파일들의 존재 여부에 대하여 검사 합니다.
def check_file() -> bool:
    for file in FILE_LIST:
        if os.path.isfile(file):
            return False
    return True


# 디렉터리 존재여부를 검사합니다.
def check_and_create_directory():
    for path in PATH_LIST:
        create_directory(path)



# 디렉터리가 존재하지 않으면 생성합니다.
def create_directory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: 디렉터리 생성을 실패 하였습니다, 디렉터리 명 :' + directory)