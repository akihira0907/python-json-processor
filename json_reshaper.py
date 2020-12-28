import json
import sys
import glob

# jsonが格納されているフォルダ名を取得
dir_path = sys.argv[1]

# jsonファイル名を取得
json_files = glob.glob(dir_path + "*.json")

for json_file in json_files:

    with open(json_file, "r+") as f:
        data = json.load(f, strict=False)
        json.dump(data, f, indent=4, strict=False)
