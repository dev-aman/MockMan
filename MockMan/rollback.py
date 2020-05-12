# This is rollback.py
import os
import shutil


def rollback():
    try:
        shutil.rmtree("../../mock-man/MockMan")
        shutil.move("../mock-man-backup/MockMan", "../../mock-man")
        shutil.rmtree("../mock-man-backup")
        print("As we have removed the MockMan Directory and replaced with the last backup files. Please change the path to MockMan.")
        print("run cd ..")
        print("run cd MockMan")
    except Exception as e:
        print(e)

rollback()