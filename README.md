# Kaggle upload

An unofficial wrapper around kaggle-api

## Features
* upload a folder as dataset in one command
```
kaggleupload --dataname kaggledatasetname --folder .
````

## installation
```
pip install kaggleupload
```

## TODO
* support creating new version
* support uploading the folder while preserving the folder
* feel free to open an issue

## Usage

```
kaggleupload --help
usage: kaggleupload [<args>]

optional arguments:
  -h, --help            show this help message and exit
  -p FOLDER, --folder FOLDER
                        folder
  --dataname DATANAME   name for the dataset
  -d DIR_MODE, --dir_mode DIR_MODE
                        dir mode
  --convert_to_csv      Whether or convert to csv.
```

## copyright notice
* package structure & setup.py modified from https://github.com/huggingface/accelerate
