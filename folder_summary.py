"""
WRITES TO A FILE A SUMMARY OF THE PROJECT JUST READ
"""
import json

from folder_visualizer import Folder, File


file_types = {}


def summarize_pr(klasses, files_dict):
    """summarises the project"""
    print("Summarising")
    folders = [obj for obj in klasses[1:] if isinstance(obj, Folder)]
    files = [assign_file_type(obj, files_dict) for obj in klasses if isinstance(obj, File)]
    total_lines = sum(
        [nums[-1] for nums in list(file_types.values())]
    )
    file_name = "{}_SUMMARY.txt".format(str(klasses[0]))
    write_summary(file_name, str(klasses[0]), len(folders), len(files), total_lines)
    print("Summary to {} done".format(file_name))


def update_file_types(file_obj):
    """updates the global dict 'file_types' for every file"""
    c_values = file_types.setdefault(file_obj.file_type, [0, 0])
    c_values[0] += 1
    c_values[-1] += file_obj.number_of_lines
    file_types[file_obj.file_type] = c_values


def load_file_types():
    """
    loads file names and associated extensions from data.json
    This function is called first before changing directory
    """
    with open('data.json', 'r') as data_file:
        files = json.load(data_file)
    return files


def assign_file_type(file_obj, files):
    """Adds a full named file type property to a File object"""
    for type_, list_ in files.items():
        if file_obj.file_extension in list_:
            file_obj.file_type = type_
            update_file_types(file_obj)
            break

    return file_obj


def write_summary(file_name, title_folder, total_folders, total_files, total_lines):
    """Writes the summary to file"""
    with open(file_name, 'w') as summary_file:
        # title
        print("Summary for {folder}".format(folder=title_folder), file=summary_file)
        # folders
        print("Folders: {}".format(str(total_folders)), file=summary_file)
        # files
        print("Files: {}".format(str(total_files)), file=summary_file)
        # every file type
        print("\t" + "-"*43, file=summary_file)
        print("\t|File type{space_1}| File Count{space_2}| Total lines{space_3}|".format(
            space_1=" "*(15-len("FILE type")),
            space_2=" "*(10-len("File Count")),
            space_3=" "*(12-len("Total lines"))
        ), file=summary_file)
        print("\t" + "-" * 43, file=summary_file)
        for file_type, count_list in file_types.items():
            print("\t|{file_type_name}{space_1}| {num_of_files}{space_2}| {total_file_type_lines}{space_3}|".format(
                file_type_name=file_type,
                num_of_files=count_list[0],
                total_file_type_lines=count_list[-1],
                space_1=" "*(15-len(file_type)),
                space_2=" "*(10-len(str(count_list[0]))),
                space_3=" "*(12-len(str(count_list[-1])))
            ), file=summary_file)
        print("\t" + "-" * 43, file=summary_file)
        # total lines
        print("Total number of lines: {}".format(str(total_lines)), file=summary_file)
