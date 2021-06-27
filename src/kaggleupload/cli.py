import dataclasses
from argparse import ArgumentParser

from kaggleupload.code import dataset_create_new, dataset_initialize


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
        "--convert_to_csv", default=False, action="store_true", help="Whether or convert to csv."
    )
    return parser

def main():
    parser = ArgumentParser("kaggleupload CLI tool", usage="kaggleupload [<args>]")
    parser = add_args(parser)
    args = parser.parse_args()
    metadata_path = dataset_initialize(folder=args.folder, dataname=args.dataname)
    dataset_create_new(folder=args.folder, convert_to_csv=args.convert_to_csv, dir_mode=args.dir_mode)

if __name__ == "__main__":
    main()
