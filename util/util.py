import os





def create_directory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: 디렉터리 생성을 실패 하였습니다, 디렉터리 명 :' + directory)