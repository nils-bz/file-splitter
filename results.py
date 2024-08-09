import os
from typing import List


def write_results(splitting_result: List[str], output_directory: str, common_filename: str, original_filename: str):
    successful_written_files = 0

    for idx, file_content in enumerate(splitting_result):
        file_name = common_filename + f"_{idx}.txt"

        file_to_write = open(os.path.join(output_directory, file_name), "w")
        file_to_write.write(file_content)
        file_to_write.close()

        successful_written_files += 1

    print(f"Successfully wrote {successful_written_files} files to \'{output_directory}\' for \'{original_filename}\'.")
