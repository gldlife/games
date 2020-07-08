import shutil
import os
from loguru import logger

old_path = r'D:\03databack\weixin\WeChat Files\smileoflife\FileStorage\File\2020-06'

def move_file(old_path):
    logger.info(old_path)
    # logger.info(new_path)
    file_list = os.listdir(old_path)
    for file in file_list:
        src = os.path.join(old_path,file)
        if(file.endswith('.doc') or file.endswith('.docx')):
            new_path = r'D:\03databack\files\doc'
            dst = os.path.join(new_path,file)
            shutil.move(src,dst)
            logger.info('move {} to doc'.format(file))
        elif(file.endswith('.xls') or file.endswith('.xlsx')):
            new_path = r'D:\03databack\files\xls'
            dst = os.path.join(new_path,file)
            shutil.move(src,dst)
            logger.info('move {} to xls'.format(file))
        elif(file.endswith('.pdf')):
            new_path = r'D:\03databack\files\pdf'
            dst = os.path.join(new_path,file)
            shutil.move(src,dst)
            logger.info('move {} to pdf'.format(file))
        elif(file.endswith('.zip') or file.endswith('.rar')):
            new_path = r'D:\03databack\files\zip'
            dst = os.path.join(new_path,file)
            shutil.move(src,dst)
            logger.info('move {} to zip'.format(file))
        else:
            new_path = r'D:\03databack\files\other'
            dst = os.path.join(new_path,file)
            shutil.move(src,dst)
            logger.info('move {} to other'.format(file))
if __name__ == '__main__':
    move_file(old_path)
    