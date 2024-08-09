from argparse import ArgumentParser


def init_argument_parser(parser: ArgumentParser):
    parser.add_argument("--root_dir",
                        help="Root directory containing files to split.",
                        type=str,
                        required=True)

    parser.add_argument("--output_dir",
                        help="Output directory for resulting files.",
                        type=str,
                        required=True)
