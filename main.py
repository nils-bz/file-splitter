import argparse
import os.path
import sys

from arguments import init_argument_parser
from splitting import split_files


def resolve_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    init_argument_parser(parser)

    return parser.parse_args()


if __name__ == '__main__':
    arguments = resolve_arguments()

    if not os.path.exists(arguments.root_dir):
        print("Given root directory does not exist. Exiting.")
        sys.exit(1)

    if arguments.output_dir == arguments.root_dir:
        print("Output directory needs to differ from root directory.")
        sys.exit(1)

    if not os.path.exists(arguments.output_dir):
        os.makedirs(arguments.output_dir)

    split_files(arguments.root_dir, arguments.output_dir)
