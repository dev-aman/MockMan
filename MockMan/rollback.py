import os
import shutil


def rollback():
    try:
        shutil.rmtree("../../mock-man/MockMan")
        shutil.move("../mock-man-backup/MockMan", "../../mock-man")
        shutil.rmtree("../mock-man-backup")
    except Exception as e:
        print(e)

rollback()