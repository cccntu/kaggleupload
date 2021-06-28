import dataclasses
from argparse import ArgumentParser

from kaggleupload.code import create_dataset


def add_args(parser):
    parser.add_argument(
        '-p',"--folder",
        dest='folder',
        default='.',
        help="folder",
    )
    parser.add_argument(
        "--dataname", default='dataname', type=str,help="name for the dataset"
    )
    parser.add_argument(
        "-d","--dir_mode", default='zip', type=str,help="dir mode"
    )
    parser.add_argument(
        "--convert_to_csv", default=False, action="store_true", help="Whether to convert to csv."
    )
    parser.add_argument(
        "-z", "--zip_folder", default=False, action="store_true", help="Whether to zip the folder and upload. (will be faster for folder with a lot of small files)."
    )
    parser.add_argument(
        "-k", "--keep_folder", default=False, action="store_true", help="Whether to keep the root folder."
    )
    return parser

def main():
    parser = ArgumentParser("kaggleupload CLI tool", usage="kaggleupload [<args>]")
    parser = add_args(parser)
    args = parser.parse_args()
    create_dataset(dataname=args.dataname, folder=args.folder, zip_folder=args.zip_folder, keep_folder=args.keep_folder, convert_to_csv=args.convert_to_csv, dir_mode=args.dir_mode)

if __name__ == "__main__":
    main()
