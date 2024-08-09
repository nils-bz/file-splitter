import os
from typing import List

from results import write_results
from utils import is_blank, remove_file_ending, is_empty


def handle_line(line: str, current_buffer: str, file_buffers: List[str]) -> str:
    if is_blank(line):
        if not is_blank(current_buffer):
            file_buffers.append(current_buffer)
        return ""

    return current_buffer + line


def split_into_files(lines: list) -> List[str]:
    file_buffers: List[str] = list()

    current_buffer: str = ""
    for line in lines:
        current_buffer = handle_line(line, current_buffer, file_buffers)
    file_buffers.append(current_buffer)

    return file_buffers


def split_files(root_directory: str, output_directory: str):
    files = os.listdir(root_directory)

    if len(files) == 0:
        print("Given root directory is empty.")
        return

    for file in files:
        if os.path.isdir(os.path.join(root_directory, file)):
            print(f'File \'{file}\' in \'{root_directory}\' represents directory and therefore can not be split, '
                  f'will skip it.')
            continue

        opened_file = open(os.path.join(root_directory, file), 'r')

        splitting_result = split_into_files(opened_file.readlines())

        common_filename = remove_file_ending(os.path.basename(opened_file.name))
        write_results(splitting_result, output_directory, common_filename, opened_file.name)
