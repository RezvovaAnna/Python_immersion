import csv
import json
import os
import pickle

code_to_write = ""
def get_dir_size(start_path='.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
        for d in dirnames:
            dp = os.path.join(dirpath, d)
            total_size += get_dir_size(dp)
    return total_size

def traverse_directory(path=' '):
    directory = []
    for root, dirs, files in os.walk(path):
        for filename in files:
            info ={}
            info['Path'] = os.path.join(root, filename)
            if os.path.isfile(os.path.join(root, filename)):
                info['Type'] = "file"
            else:
                info['Type'] = "directory"
            directory.append(info)
            info['Size'] = get_dir_size(path)
    return directory


def save_results_to_json(data):
    with open('res.json', 'w') as f:
        json.dump(data, f)


def save_results_to_cvs(data):
    keys = data[0].keys()
    with open('res.csv', 'w', newline='', encoding='utf-8') as f:
        dict_writer = csv.DictWriter(f, fieldnames=['Path','Size', 'Type'],dialect='excel')
        dict_writer.writerows(data)
        dict_writer.writeheader()


def save_results_to_pickle(data):
    with open('res.pickle', 'wb') as f:
        pickle.dump(data, f)


result = traverse_directory(r'C:\Users\ANNA\Desktop\educational\Python (immersion)\Python_practic\Python_immersion\test_dic')
print(result)


# def get_dir_size(start_path='.'):
#     total_size = 0
#     for dirpath, dirnames, filenames in os.walk(start_path):
#         for f in filenames:
#             fp = os.path.join(dirpath, f)
#             total_size += os.path.getsize(fp)
#         for d in dirnames:
#             dp = os.path.join(dirpath, d)
#             total_size += get_dir_size(dp)
#     return total_size
#
# def save_results_to_json(results, file_name):
#     with open(file_name, 'w') as f:
#         json.dump(results, f)
#
# def save_results_to_csv(results, file_name):
#     with open(file_name, 'w', newline='') as f:
#         writer = csv.writer(f)
#         writer.writerow(['Path', 'Type', 'Size'])
#         for result in results:
#             writer.writerow([result['Path'], result['Type'], result['Size']])
#
# def save_results_to_pickle(results, file_name):
#     with open(file_name, 'wb') as f:
#         pickle.dump(results, f)
#
# def traverse_directory(directory):
#     results = []
#     for root, dirs, files in os.walk(directory):
#         for name in files:
#             path = os.path.join(root, name)
#             size = os.path.getsize(path)
#             results.append({'Path': path, 'Type': 'File', 'Size': size})
#         for name in dirs:
#             path = os.path.join(root, name)
#             size = get_dir_size(path)
#             results.append({'Path': path, 'Type': 'Directory', 'Size': size})
#     return results

with open('_init_.py', 'w') as init_file:
    init_file.write(code_to_write)

