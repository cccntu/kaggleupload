# Kaggle upload

An unofficial wrapper around kaggle-api

## Features
* upload a folder as dataset in one command
```
kaggleupload --dataname kaggledatasetname --folder .
````
* keep the folder (will zip the whole folder then upload, which is much faster if there are a lot of small files in the root of folder)
```
kaggleupload --dataname kaggledatasetname --folder . --keep_folder
````


## installation
```
pip install kaggleupload
```

## TODO
* support creating new version
* feel free to open an issue

## Usage

```
$kaggleupload --help
usage: kaggleupload [<args>]

optional arguments:
  -h, --help            show this help message and exit
  -p FOLDER, --folder FOLDER
                        folder
  --dataname DATANAME   name for the dataset
  -d DIR_MODE, --dir_mode DIR_MODE
                        dir mode
  --convert_to_csv      Whether to convert to csv.
  -k, --keep_folder     Whether to keep the folder. (will be faster for folder with a lot of
                        small files).
```

## copyright notice
* package structure & setup.py modified from https://github.com/huggingface/accelerate
