import json
import shutil
import tempfile
from functools import partial
from pathlib import Path

from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()


def dataset_initialize(dataname, folder):
    metadata_path = api.dataset_initialize(folder=folder)
    with open(metadata_path) as f:
        metadata = json.load(f)
    metadata["title"] = dataname
    metadata["id"] = metadata["id"].split("/")[0] + "/" + dataname

    with open(metadata_path, "w") as f:
        json.dump(obj=metadata, fp=f)
    return metadata_path


def _create_dataset(
    dataname, folder, public=False, quiet=False, convert_to_csv=False, dir_mode="zip"
):

    metadata_path = dataset_initialize(dataname, folder)
    return api.dataset_create_new(folder, public, quiet, convert_to_csv, dir_mode)


def _create_dataset_zip(
    dataname, folder, public=False, quiet=False, convert_to_csv=False, dir_mode="zip", keep_folder=False,
):
    with tempfile.TemporaryDirectory() as tmpdirname:
        zipfilename = str(Path(tmpdirname) / (Path(folder).name))
        shutil.make_archive(zipfilename, "zip", folder)
        # need more than 1 file otherwise kaggle will ignore the root dir
        if keep_folder:
            with open(Path(tmpdirname) / "empty.txt", "w") as f:
                f.write("")
        folder = tmpdirname
        return _create_dataset(
            dataname, folder, public, quiet, convert_to_csv, dir_mode
        )


def create_dataset(
    dataname,
    folder,
    zip_folder=False,
    keep_folder=False,
    public=False,
    quiet=False,
    convert_to_csv=False,
    dir_mode="zip",
):
    # modified from https://github.com/Kaggle/kaggle-api/blob/master/kaggle/api/kaggle_api_extended.py
    """ create a new dataset
    Args:
        dataname: kaggle dataset name to be created
        folder: the folder to upload
        zip_folder: if True, will zip the whole folder and upload, ignoring the dir_mode argument
        keep_folder: if True, behaves like zip_folder, except will add an empty file so the root folder will be preserved.
        public: should the dataset be public?
        quiet: suppress verbose output (default is False)
        convert_to_csv: if True, convert data to comma separated value
        dir_mode: What to do with directories: "skip" - ignore; "zip" - compress and upload
    """
    if keep_folder:
        fn = partial(_create_dataset_zip, keep_folder=True)
    elif zip_folder:
        fn = _create_dataset_zip
    else:
        fn = _create_dataset
    return fn(dataname, folder, public, quiet, convert_to_csv, dir_mode)
