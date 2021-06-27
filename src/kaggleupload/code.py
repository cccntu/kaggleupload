import json

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


def dataset_create_new(
    folder, public=False, quiet=False, convert_to_csv=False, dir_mode="zip"
):
    return api.dataset_create_new(folder, public, quiet, convert_to_csv, dir_mode)
