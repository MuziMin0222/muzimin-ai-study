import multiprocessing
import os


def copy(fileName, source_dir, dest_dir):
    source_path = source_dir + "/" + fileName
    dest_path = dest_dir + "/" + fileName

    with open(source_path, "rb") as source_file:
        with open(dest_path, "wb") as dest_file:
            while True:
                data = source_file.read(1024)
                if data:
                    dest_file.write(data)
                else:
                    break


if __name__ == '__main__':
    source_dir = "/Users/muzimin/Downloads"
    dest_dir = "/Users/muzimin/temp"

    try:
        os.mkdir(dest_dir)
    except:
        print("目标文件夹已经存在")

    file_list = os.listdir(source_dir)
    for file in file_list:
        sub_process = multiprocessing.Process(target=copy, args=(file, source_dir, dest_dir))
        sub_process.start()
