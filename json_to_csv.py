import json
import sys
import os
import csv


def check_id(json_data, target_id):
    rslt = False
    for people in json_data["people"]:
        if people["person_id"][0] == target_id:
            rslt = True
    return rslt


def main(file_name, csv_writer):
    # jsonファイルをロード
    json_file = open(file_name, 'r')
    json_data = json.load(json_file)
    json_file.close()

    # ターゲットとする人物のIDを指定
    target_id = int(sys.argv[2])

    # target_idが今読み込んでいるフレームに存在するか判定
    if check_id(json_data, target_id):
        # 存在する場合
        for people in json_data["people"]:
            # idが一致するデータをCSVに書き込み
            if people["person_id"][0] == target_id:
                csv_writer.writerow[people["pose_keypoints_2d"]
    else:
        # 存在しない場合
        csv_writer.writerow([-1]*75)
    
    # for people in json_data["people"]:
    #     if people["person_id"][0] == target_id:
    #         # print(people["person_id"])
    #         # print(people["pose_keypoints_2d"][0]) 
    #         # print(people["pose_keypoints_2d"][1])
    #         if mode == 0:
    #             csv_writer.writerow(people["pose_keypoints_2d"])
    #         elif mode == 1:
    #             csv_writer.writerow(people["face_keypoints_2d"])
    #         elif mode == 2:
    #             csv_writer.writerow(people["hand_left_keypoints_2d"])
    #         elif mode == 3:
    #             csv_writer.writerow(people["hand_right_keypoints_2d"])
    #     else:
    #         if mode == 0:
    #             csv_writer.writerow([-1]*75)
    #         elif mode == 1:
    #             csv_writer.writerow([-1]*68)
    #         elif mode == 2 or mode == 3:
    #             csv_writer.writerow([-1]*21)


if __name__ == "__main__":
    args = sys.argv

    # JSONファイルのディレクトリを読み込み
    json_dir = args[1]
    json_files = os.listdir(json_dir)

    # 出力用CSVを開く
    written_csv_path = args[3]
    written_csv_file = open(written_csv_path, 'w')
    csv_writer = csv.writer(written_csv_file)
    
    # 各jsonファイルに対してmainを実行
    for json_file in sorted(json_files):
        print(json_dir + json_file)
        main(json_dir + json_file, csv_writer)

    written_csv_file.close()

