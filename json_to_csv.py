import json
import sys
import os
import csv

def main(file_name, csv_writer):
    json_file = open(file_name, 'r')
    json_data = json.load(json_file)
    json_file.close()

    target_id = int(sys.argv[2])

    # print(json_data)
    for people in json_data["people"]:
        if people["person_id"][0] == target_id:
            # print(people["person_id"])
            # print(people["pose_keypoints_2d"][0]) 
            # print(people["pose_keypoints_2d"][1])
            csv_writer.writerow(people["pose_keypoints_2d"])
        else:
            csv_writer.writerow([-1]*75)


if __name__ == "__main__":
    args = sys.argv
    json_dir = args[1]
    json_files = os.listdir(json_dir)

    written_csv_path = args[3]
    written_csv_file = open(written_csv_path, 'w')
    csv_writer = csv.writer(written_csv_file)

    for json_file in sorted(json_files):
        print(json_dir + json_file)
        main(json_dir + json_file, csv_writer)

    written_csv_file.close()
