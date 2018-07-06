import os

result = []


# get file count
def get_all_file_counts(dir):
    # get the file list of dir
    name_list = os.listdir(dir)
    for i in name_list:
        sub_dir = os.path.join(dir, i)
        if os.path.isdir(sub_dir):
            get_all_file_counts(sub_dir)
        else:
            file_name = os.path.basename(i)
            print(file_name)
            result.append(file_name)
    print('Total files count: ', len(result))


if __name__ == '__main__':
    get_all_file_counts(os.getcwd())
