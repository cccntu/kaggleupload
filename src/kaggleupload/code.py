import json
import shutil
import tempfile
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


def _create_dataset_keep_folder(
    dataname, folder, public=False, quiet=False, convert_to_csv=False, dir_mode="zip"
):
    with tempfile.TemporaryDirectory() as tmpdirname:
        zipfilename = str(Path(tmpdirname) / (Path(folder).name))
        shutil.make_archive(zipfilename, "zip", folder)
        # need more than 1 file otherwise kaggle will ignore the root dir
        with open(Path(tmpdirname) / "empty.txt", "w") as f:
            f.write("")
        folder = tmpdirname
        return _create_dataset(
            dataname, folder, public, quiet, convert_to_csv, dir_mode
        )


def create_dataset(
    dataname,
    folder,
    keep_folder=False,
    public=False,
    quiet=False,
    convert_to_csv=False,
    dir_mode="zip",
):
    if keep_folder:
        fn = _create_dataset_keep_folder
    else:
        fn = _create_dataset
    return fn(dataname, folder, public, quiet, convert_to_csv, dir_mode)
