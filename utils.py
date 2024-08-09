def is_blank(to_check: str) -> bool:
    return to_check.strip() == ""


def remove_file_ending(filename: str) -> str:
    return filename.rsplit(".", 1)[0]


def is_empty(to_check: str) -> bool:
    return to_check == ""
