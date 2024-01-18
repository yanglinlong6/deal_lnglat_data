import json

import os


def parse_json():
    path = "H:\PythonWorkSpaces\deal_lnglat_data"
    files = os.listdir(path)
    s = []
    for file in files:
        print(file)
        # 读取文件
        # f = open("biz-gps-kafka-pazlpush.log.2023-07-28.99", 'r', encoding='UTF-8')
        # lines = f.readlines()
        # for line in lines:
        #     print(line)
        #     # print(type(line))
        # f.close()
        # json_str = json.dumps(data)
        # print("Python 原始数据：", repr(data))
        # print("JSON 对象：", json_str)


def print_hi(name):
    print(f'Hi, {name}')


class demoFindLogClass(object):
    def __init__(self):
        pass

    def demoFindLog(self):
        deault_lng = 110.35
        deault_lat = 34.62
        with open("biz-gps-kafka-pazlpush.log.2023-07-28.99", "r", encoding='UTF-8') as f:
            content_list = f.readlines()

        for content_line in content_list:
            if "定位数据推送数据的实体===" in content_line:
                _, data = content_line.split("定位数据推送数据的实体===")
                temp_data = json.loads(data)
                for d in temp_data:
                    lat = d["lat"]
                    lng = d["lng"]
                    imei = d["imei"]
                    loctype = d["loctype"]
                    if (not (lat - deault_lat > 0 and lng - deault_lng > 0)) and loctype == 1:
                        print("imei = %s, loctype = %s, lat = %s, lng = %s " % (imei, loctype, lat, lng))


if __name__ == '__main__':
    # print_hi('PyCharm')
    # parse_json()
    demoFindLogClass().demoFindLog()
