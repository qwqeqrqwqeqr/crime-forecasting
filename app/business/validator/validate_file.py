import os


def init():
    check_data_file()
    create_data_directory()

def check_data_file():
    from app.utils.constants import FILE_LIST
    for file in FILE_LIST:
        check_file(file)

def create_data_directory():
    from app.utils.constants import PATH_LIST
    for path in PATH_LIST:
        create_directory(path)


def check_file(file):
    import os
    if not os.path.isfile(file):
        from log import logger
        logger.info("[Error] file does not exist [%s]" % (file.split('/')[-1]))
        raise Exception


def create_directory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        from log import logger
        logger.info("[Error] can not create directory [%s]"%(directory.split('/')[-1]))





