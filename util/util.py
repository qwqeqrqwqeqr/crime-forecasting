import os

from util.constants import *


def init():
    print("========== 검사를 수행합니다. ==========")
    check_file()
    check_directory()
    print("========== 검사를 완료하였습니다. ==========")


# 파일들의 존재 여부에 대하여 검사 합니다.
def check_file():
    print("요구되는 파일들을 검사합니다.")
    for file in FILE_LIST:
        if not os.path.isfile(file):
            raise Exception("Error: 다음 파일이 존재하지 않습니다. [%s]"%(file.split('/')[-1]))

 # 디렉터리 존재여부를 검사합니다.
def check_directory():
    print("디렉터리를 설정합니다.")
    for path in PATH_LIST:
        create_directory(path)


# 디렉터리가 존재하지 않으면 생성합니다.
def create_directory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: 디렉터리 생성을 실패 하였습니다. [%s]'%(directory.split('/')[-1]))
