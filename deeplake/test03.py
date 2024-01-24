import os


def get_files_in_directory(directory):
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    return file_paths


directory_path = "H:\\WorkSpaces\\temp\\develop\\car-service-ordercenter"
files = get_files_in_directory(directory_path)

# 打印文件路径
for file in files:
    print(file)
