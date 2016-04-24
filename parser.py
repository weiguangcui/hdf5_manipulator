"""
Command line parser for HDF5 MANIPULATOR
"""

import argparse


def get_args_split():

    """parse arguments for split"""

    parser = argparse.ArgumentParser(
        description="HDF5 MANIPULATOR (split)",
        usage="./split.py <options>"
        )

    parser.add_argument(
        "--prefix", action="store", dest="prefix",
        metavar="[path/to/filename_base]", default=None,
        help="prefix for splitted files (base on input file if not defined)"
        )

    parser.add_argument(
        "--filelist", action="store", dest="filelist",
        metavar="[path/to/filelist]", default=None,
        help="save output files list in txt file"
        )

    required = parser.add_argument_group("required arguments")

    required.add_argument(
        "--input", action="store", dest="input",
        metavar="[path/to/input_file]", required=True,
        help="path to input hdf5 file"
    )

    required.add_argument(
        "--size", action="store", dest="size", metavar="[int]", required=True,
        help="number of entries per file"
    )

    return parser.parse_args()


def get_args_merge():

    """parse arguments for merge"""

    parser = argparse.ArgumentParser(
        description="HDF5 MANIPULATOR (merge)",
        usage="./merge.py <options>"
        )

    required = parser.add_argument_group("required arguments")

    required.add_argument(
        "--input", action="store", dest="input_files",
        metavar="[list of input files]", required=True,
        help="path to input hdf5 files to merge ('file1, file2,...' \
              will look for all files starts with file1 and file2 \
              and ends with .hdf5)"
    )

    required.add_argument(
        "--output", action="store", dest="output",
        metavar="[path/to/filename]", required=True,
        help="path to output hdf5 file"
        )

    return parser.parse_args()


def get_args_extract():

    """parse arguments for extract"""

    parser = argparse.ArgumentParser(
        description="HDF5 MANIPULATOR (extract)",
        usage="./extract.py <options>"
        )

    required = parser.add_argument_group("required arguments")

    required.add_argument(
        "--input", action="store", dest="input",
        metavar="[path/to/filename]", required=True,
        help="path to input hdf5 file"
    )

    required.add_argument(
        "--output", action="store", dest="output",
        metavar="[path/to/filename]", required=True,
        help="path to output hdf5 file"
        )

    required.add_argument(
        "--keys", action="store", dest="keys", metavar="['key1, key2, ...']",
        required=True,
        help="list of datasets to be saved in the output file"
        )

    return parser.parse_args()