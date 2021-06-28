# Kaggle upload

An unofficial wrapper around kaggle-api

## Features
* upload a folder as dataset in one command
```
kaggleupload --dataname kaggledatasetname --folder .
```
* zip the folder then upload (this is much faster if you have many small files in the root folder)
```
kaggleupload --dataname kaggledatasetname --folder . --zip_folder
```
*  keep the root folder (will add another empty file at the same level with the root folder)
```
kaggleupload --dataname kaggledatasetname --folder . --keep_folder
```


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
